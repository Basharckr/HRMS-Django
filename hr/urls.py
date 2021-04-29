from django.urls import path
from .views import *

urlpatterns = [
 

    path('', HrDashboard.as_view(), name='hr_dashboard')

]
