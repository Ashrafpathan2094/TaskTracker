from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from tasks.models import Team

from user_app.models import Profile,Tasks

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        Team_ = serializers.StringRelatedField(read_only=True)
        model = Team
        fields = ['team_name','id']
        
        
