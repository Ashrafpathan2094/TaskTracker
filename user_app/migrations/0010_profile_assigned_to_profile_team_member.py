# Generated by Django 4.0.3 on 2022-03-12 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_team_assigned_to'),
        ('user_app', '0009_remove_profile_team_remove_profile_team_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='tasks.team'),
        ),
        migrations.AddField(
            model_name='profile',
            name='team_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to='tasks.tasks'),
        ),
    ]
