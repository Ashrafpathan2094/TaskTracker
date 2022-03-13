from django.db import models
from django.contrib.auth.models import User
from tasks.models import Tasks, Team

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    is_team_leader = models.BooleanField(default=False)
    assign_to_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True)
    assign_to_task = models.ForeignKey(
        Tasks, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username + ' ' + str(self.is_team_leader)
