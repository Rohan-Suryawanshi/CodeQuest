from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    TAGS=[
        ('Array', 'Array'),
        ('String', 'String'),
        ('Dynamic Programming', 'Dynamic Programming'),
        ('Tree', 'Tree'),
        ('Graph', 'Graph'),
        ('Backtracking', 'Backtracking'),
        ('Linked List', 'Linked List'),
        ('Binary Search', 'Binary Search')
    ]

    title = models.CharField(max_length=255)
    problem_statement = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    tags = models.CharField(max_length=255,choices=TAGS)
    time_limit = models.IntegerField(help_text="Time limit in milliseconds")
    memory_limit = models.IntegerField(help_text="Memory limit in kilobytes")
    input_format = models.TextField()
    output_format = models.TextField()
    constraints = models.TextField()
    sample_test_cases = models.JSONField(help_text="Provide sample test cases in JSON format (e.g., [{'input': '[2,7,11,15], 9', 'output': '[0,1]'}]).")
    hidden_test_cases = models.JSONField(help_text="Provide hidden test cases in JSON format for evaluation (e.g., [{'input': '[1,5,3,7,11], 16', 'output': '[3,4]'}]).")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class SolvedProblem(models.Model):
    # Status choices for problem-solving attempts
    STATUS_CHOICES = [
        ('solved', 'Solved'),
        ('attempted', 'Attempted'),
        ('not_attempted', 'Not Attempted'),
    ]
    
    # Foreign key relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solved_problems')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solved_by')
    
    # Problem status (whether the user has solved or attempted the problem)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Todo')
    
    # Date when the problem was solved or attempted
    solved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.problem.title} - {self.get_status_display()}'
