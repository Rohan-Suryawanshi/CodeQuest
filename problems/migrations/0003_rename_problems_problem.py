# Generated by Django 5.1.2 on 2024-11-26 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problems_delete_leetcodequestion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Problems',
            new_name='Problem',
        ),
    ]
