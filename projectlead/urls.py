from django.urls import path
from .views import *

urlpatterns = [
 
    path('', LeaderDashboard.as_view(), name='ldr_dashboard'),
    path('change-task-status/(?P<pk>\d+)/$', change_task_status, name='change-task-status'),
    path('<int:pk>/<int:id>/assign-task/<int:uk>/', assign_task, name='assign-task'),
    path('projects/', leader_projects, name='leader-projects'),
    path('<int:pk>/project/', LeaderProjectDetail.as_view(), name='ldr-view-project'),
    path('<int:pk>/task-board/', ldr_task_board, name='ldr-task-board'),
    path('addtask/<int:pk>/', add_new_task, name='ldr-add-new-task'),
    path('task-delete/<int:pk>/<int:id>/', task_delete, name='ldr-task-delete'),
    path('edit-task/<int:pk>/<int:id>/', edit_task, name='ldr-edit-task'),

    
    
]
