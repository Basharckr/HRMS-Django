from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('profile/', emp_profile, name='profile'),


    path('employee/dashboard/', EmployeeDashboard.as_view(), name='emp_dashboard'),

]
