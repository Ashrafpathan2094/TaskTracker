from tasks.serializers import TeamSerializer,TaskSerializer
from user_app.models import Profile
from tasks.models import Team, Tasks


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


class TeamCreate(APIView):
    

    def get(self, request):
        TeamList = Team.objects.all()
        serializer = TeamSerializer(TeamList,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        user = self.request.user
        
        if user.is_team_leader:
            serializer = TeamSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)


class Availablilty(APIView):
    
    def get(self, request,pk):
        try:
            team_details = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(team_details)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class TaskCreate(APIView):
    def get(self, request):
        TeamList = Tasks.objects.all()
        serializer = TaskSerializer(TeamList,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
        
class TaskUpdate(APIView):
    def get(self, request,pk):
        try:
            task_details = Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task_details)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        task_details = Tasks.objects.get(pk=pk)
        serializer = TaskSerializer(task_details,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


class Report(APIView):
    def get(self, request,pk):
        try:
            task_details = Tasks.objects.get(start_date=pk)
        except Tasks.DoesNotExist:
            return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task_details)
        return Response(serializer.data,status=status.HTTP_200_OK)      
    
