from tasks.serializers import TeamSerializer
from user_app.models import Team,Tasks

from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated





# Create your views here.


class TeamCreate(generics.CreateAPIView):
    
    def post(self, request):
        serializer = TeamSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

class Availablilty(generics.CreateAPIView):
    pass

class Task(generics.CreateAPIView):
    pass

class UpdateTask(generics.UpdateAPIView):
    pass

class Report(generics.ListAPIView):
    pass