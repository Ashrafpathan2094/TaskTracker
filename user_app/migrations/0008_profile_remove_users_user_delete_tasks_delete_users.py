# Generated by Django 4.0.3 on 2022-03-12 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_initial'),
        ('user_app', '0007_rename_team_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_team_leader', models.BooleanField(default=False)),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='tasks.team')),
                ('team_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to='tasks.tasks')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
