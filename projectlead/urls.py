from django.urls import path
from .views import *

urlpatterns = [
 
    path('', LeaderDashboard.as_view(), name='ldr_dashboard'),
    path('tasks/', TaskCreate.as_view(), name='tasks'),
    path('project-tasks/<int:pk>/', task_view, name='project-tasks'),
    path('tasks-delete/<int:pk>/', task_delete, name='tasks-delete'),
    path('change-task-status/(?P<pk>\d+)/$', change_task_status, name='change-task-status'),
    path('<int:pk>/<int:id>/assign-task/<int:uk>/', assign_task, name='assign-task'),
    path('leader/projects/', leader_projects, name='leader-projects'),
    path('<int:pk>/project/', LeaderProjectDetail.as_view(), name='ldr-view-project'),
    path('<int:pk>/task-board/', ldr_task_board, name='ldr-task-board'),

    
    
]
