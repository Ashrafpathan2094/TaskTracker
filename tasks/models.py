from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.team_name   

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
    task_name = models.CharField(max_length=50)
    priority = models.CharField(max_length=1, choices = PRIORITY, default='M')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices = STATUS,)
     
     
    def __str__(self):
        return self.task_name 