# Generated by Django 5.1.2 on 2024-11-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='easy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='hard',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='total_solved',
            field=models.IntegerField(default=0),
        ),
    ]
