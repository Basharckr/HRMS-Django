from django.urls import path
from .views import *

urlpatterns = [
 

    path('', HrDashboard.as_view(), name='hr_dashboard'),
    path('projects/', ProjectCreate.as_view(), name='projects'),
    path('<int:pk>/projects/', ProjectUpdate.as_view(), name='update-projects'),
    path('<int:pk>/projects/delete/', ProjectDelete.as_view(), name='delete-projects')





]
