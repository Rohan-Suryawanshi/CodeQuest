from django.urls import path
from .views import *
urlpatterns = [
    path('',leaderboard, name='leaderboard'),
]
