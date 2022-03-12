from django.db import models
from django.contrib.auth.models import User
from tasks.models import Tasks,Team

# Create your models here.

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    is_team_leader = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(Team,on_delete=models.CASCADE,null=True, related_name="assigned_to")
    team_member = models.ForeignKey(Tasks,on_delete=models.CASCADE,null=True,related_name="team_member")
    
    def __str__(self):
        return self.user.username + ' ' + str(self.is_team_leader)
    