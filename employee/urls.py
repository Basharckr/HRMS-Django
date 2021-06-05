from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('profile/', emp_profile, name='profile'),
    path('profile-update/', profile_update, name='profile-update'),
    path('employee/dashboard/', EmployeeDashboard.as_view(), name='emp_dashboard'),
    path('my-projects/', employee_project, name='employee-project'),
    path('project-detail/<int:pk>/', employee_project_veiw, name='employee-project-detail'),
    path('my-tasks/<int:pk>/', employee_task_board, name='employee-tasks'),
    path('emp-change-task-status/<int:pk><str:st>/', emp_change_task_status, name='emp-change-task-status'),




]
