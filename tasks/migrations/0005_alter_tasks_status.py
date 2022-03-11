# Generated by Django 4.0.3 on 2022-03-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('Assigned', 'Assigned'), ('InProgress', 'InProgress'), ('UnderReview', 'UnderReview'), ('Done', 'Done')], default='Done', max_length=20),
        ),
    ]
