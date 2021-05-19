from django.urls import path
from .views import *

urlpatterns = [
 

    path('', HrDashboard.as_view(), name='hr_dashboard'),
    path('projects/', ProjectCreate.as_view(), name='projects'),
    path('<int:pk>/projects/', ProjectDetailView.as_view(), name='view-project'),
    path('<int:pk>/update-projects/', ProjectUpdate.as_view(), name='update-projects'),
    path('<int:pk>/projects/delete/', project_delete, name='delete-projects'),

]
