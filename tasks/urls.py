from django.urls import path
from tasks.views import (TeamCreate,Availablilty,TaskCreate,TaskUpdate,Report)
urlpatterns = [
    
    path('team-create/',TeamCreate.as_view(),name='team-create'),
    
    path('availability/<int:pk>/',Availablilty.as_view(),name='availability'),
    
    path('task-create/',TaskCreate.as_view(),name='task'),
    
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task'),
    
    path('report/<int:pk>/',Report.as_view(),name='report'),
    
]