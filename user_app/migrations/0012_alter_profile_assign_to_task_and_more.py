# Generated by Django 4.0.3 on 2022-03-13 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_rename_name_tasks_task_name'),
        ('user_app', '0011_remove_profile_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='assign_to_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='assign_to_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.team'),
        ),
    ]
