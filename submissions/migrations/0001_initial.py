# Generated by Django 5.1.2 on 2024-12-16 15:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '0004_solvedproblem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Wrong Answer', 'Wrong Answer'), ('Runtime Error', 'Runtime Error'), ('Time Limit Exceeded', 'Time Limit Exceeded')], max_length=20)),
                ('language', models.CharField(choices=[('Python', 'Python'), ('C++', 'C++'), ('Java', 'Java'), ('JavaScript', 'JavaScript')], max_length=20)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='problems.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
