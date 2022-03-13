# Generated by Django 4.0.3 on 2022-03-12 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_team_assigned_to'),
        ('user_app', '0010_profile_assigned_to_profile_team_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='team_member',
        ),
        migrations.AddField(
            model_name='profile',
            name='assign_to_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_to_task', to='tasks.tasks'),
        ),
        migrations.AddField(
            model_name='profile',
            name='assign_to_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_to_task', to='tasks.team'),
        ),
    ]
