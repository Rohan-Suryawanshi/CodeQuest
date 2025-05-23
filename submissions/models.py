from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem

class Submission(models.Model):
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Wrong Answer', 'Wrong Answer'),
        ('Runtime Error', 'Runtime Error'),
        ('Time Limit Exceeded', 'Time Limit Exceeded'),
    ]

    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"
