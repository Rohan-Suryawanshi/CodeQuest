from django.urls import path
from .views import *
from core.views import home
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
]
