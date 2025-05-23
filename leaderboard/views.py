from django.shortcuts import render
from django.http import JsonResponse
from account.models import Account

def leaderboard(request):
    # Get all account records
    accounts = Account.objects.all()

    # Prepare the leaderboard data
    leaderboard_data = [{
        "rank": idx + 1,
        "name": data.user.username,
        "easy": data.easy,
        "medium": data.medium,
        "hard": data.hard,
        "total": data.total_solved
    } for idx, data in enumerate(accounts)]

    
    # Otherwise, render the page
    return render(request, 'leaderboard/leaderboard.html',{"data":leaderboard_data})
