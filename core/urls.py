from django.urls import path
from core.views import *
from problems.views import *
urlpatterns = [
    path('',home,name="home"),
    path('problem/',problem_list,name="problem"),
]
