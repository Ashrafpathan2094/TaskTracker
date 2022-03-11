from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    is_team_leader = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username + ' ' + str(self.is_team_leader)
    
 
 
 
 
 
 
    
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
    team_leader =models.OneToOneField(Team,on_delete=models.CASCADE,blank=True, related_name='team_leader')
    team_member = models.ForeignKey(Team,on_delete=models.CASCADE,blank=True, related_name="team_members")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    
    status = models.CharField(max_length=20, choices = STATUS,default='Done')
     
     
    def __str__(self):
        return self.task_name 