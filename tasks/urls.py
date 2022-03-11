from django.urls import path
from tasks.views import (TeamCreate,Availablilty,Task,UpdateTask,Report)
urlpatterns = [
    
    path('<int:pk>/team-create/',TeamCreate.as_view(),name='team-create'),
    
    path('availability/',Availablilty.as_view(),name='availability'),
    
    path('task/',Task.as_view(),name='task'),
    
    path('update-task/',UpdateTask.as_view(),name='update-task'),
    
    path('report/',Report.as_view(),name='report'),
    
]