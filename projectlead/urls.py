from django.urls import path
from .views import *
urlpatterns = [
 
    path('', LeaderDashboard.as_view(), name='ldr_dashboard'),
    path('list-project/', ProjectView.as_view(), name='list_projects'),
    path('project-view/(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project-view'),
    path('tasks/', TaskCreate.as_view(), name='tasks'),





    
]
