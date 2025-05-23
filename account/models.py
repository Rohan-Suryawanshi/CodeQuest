from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="account")  # Links to the default User model
    easy = models.IntegerField(default=0)  # To track the number of easy problems solved
    medium = models.IntegerField(default=0)  # To track the number of medium problems solved
    hard = models.IntegerField(default=0)  # To track the number of hard problems solved
    total_solved = models.IntegerField(default=0)  # To track the total problems solved

    def update_total_solved(self):
        self.total_solved = self.easy + self.medium + self.hard
        self.save()

    def __str__(self):
        return self.user.username
