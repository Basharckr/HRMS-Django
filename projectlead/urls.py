from django.urls import path
from .views import *
urlpatterns = [
 
    path('', LeaderDashboard.as_view(), name='ldr_dashboard'),
    path('list-project/', ProjectView.as_view(), name='list_projects'),
    path('project-view/(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project-view'),
    path('tasks/', TaskCreate.as_view(), name='tasks'),
    path('tasks-delete/(?P<pk>\d+)/$', task_delete, name='tasks-delete'),
    path('change-task-status/(?P<pk>\d+)/$', change_task_status, name='change-task-status'),

    






    
]
