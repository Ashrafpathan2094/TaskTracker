# Generated by Django 4.0.3 on 2022-03-11 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_team_team_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_member',
        ),
    ]
