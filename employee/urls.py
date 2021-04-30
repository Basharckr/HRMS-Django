from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='signup'),

    path('employee/dashboard/', EmployeeDashboard.as_view(), name='emp_dashboard'),

]
