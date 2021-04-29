from django.urls import path
from .views import *
urlpatterns = [
 
    path('', LeaderDashboard.as_view(), name='ldr_dashboard')
]
