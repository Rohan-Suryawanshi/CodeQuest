from django.urls import path
from .views import *
urlpatterns = [
    path('submit_code/<int:id>/',submit_code, name='submit_code'),
]
