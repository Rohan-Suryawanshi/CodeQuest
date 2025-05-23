from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account
from submissions.models import Submission


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

      
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')


        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        Account.objects.create(user=user)

        login(request, user)

        messages.success(request, 'Registration successful')
        return redirect('home')

    return render(request, 'account/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'account/login.html')


@login_required
def home(request):
    return render(request, 'account/home.html')



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

def profile(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('login')  
    else:
        data = Account.objects.get(user_id=user) 
        submissions = Submission.objects.filter(user=request.user).order_by('-id')[:5]
        context = {
            'data': data,
            'submissions': submissions
        }

    return render(request, 'account/profile.html', context)

