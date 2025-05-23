from django.contrib import admin
from .models import Problem

@admin.register(Problem)
class Problem(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'created_at')
    search_fields = ('title', 'tags', 'difficulty')
