from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user_app.models import Team,Tasks

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['team_name','id']