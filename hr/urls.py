from django.urls import path
from .views import *

urlpatterns = [
 

    path('', HrDashboard.as_view(), name='hr_dashboard'),
    path('projects/', ProjectCreate.as_view(), name='projects'),
    path('<int:pk>/projects/', ProjectDetailView.as_view(), name='view-project'),
    path('<int:pk>/update-projects/', ProjectUpdate.as_view(), name='update-projects'),
    path('<int:pk>/projects/delete/', project_delete, name='delete-projects'),
    path('<int:pk>/<int:id>/assign/', assign_employee, name='assign-employee'),
    path('<int:pk>/task-board/', task_board, name='task-board'),
    path('addtask/<int:pk>/', add_new_task, name='add-new-task'),
    path('task-delete/<int:pk>/<int:id>/', task_delete, name='task-delete'),
    path('edit-task/<int:pk>/<int:id>/', edit_task, name='edit-task'),
    path('change-task-status/<int:pk><str:st>/', change_task_status, name='change-task-status'),








]
