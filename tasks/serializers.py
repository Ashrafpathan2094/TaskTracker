from rest_framework import serializers
from tasks.models import Team,Tasks
from user_app.models import Profile



# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Profile
#         fields ='__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Team
        fields = ['team_name',]
        
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
  
