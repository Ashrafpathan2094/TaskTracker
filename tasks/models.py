from django.db import models
from user_app.models import Team 


# Create your models here.

class Tasks(models.Model):
    
    STATUS = (('Assigned','Assigned'),
              ('InProgress','InProgress'),
              ('UnderReview','UnderReview'),
              ('Done','Done')
              )
    PRIORITY = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
        )    
    task_name = models.CharField(max_length=20)
    priority = models.CharField(max_length=1, choices = PRIORITY, default='H')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    team_leader = models.OneToOneField(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices = STATUS,default='Done')
     
     
    def __str__(self):
        return self.task_name 