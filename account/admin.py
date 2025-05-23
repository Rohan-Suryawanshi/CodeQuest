# admin.py
from django.contrib import admin
from .models import User  # Import the custom User model

class UserAdmin(admin.ModelAdmin):
    # Define the fields you want to display in the admin interface
    list_display = ['username', 'useremail', 'easy', 'medium', 'hard', 'total_solved']

    # Optional: Define search fields (if you want to search for users in admin)
    search_fields = ['username', 'useremail']

    # Optional: Define filtering options
    list_filter = ['easy', 'medium', 'hard']
