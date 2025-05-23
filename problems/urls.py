from django.urls import path
from .views import *
urlpatterns = [
    path('solve/<int:id>/',solve, name='solve'),
    path('problem_list',problem_list, name='problem_list'),
    path("pick_random",pick_random, name='pick_random'),
]
