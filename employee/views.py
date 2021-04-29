from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, redirect_to_login

from django.urls import reverse_lazy

# Create your views here.


# login

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_superuser == True:
            return reverse_lazy('hr_dashboard')
        elif self.request.user.is_staff == True:
            return reverse_lazy('ldr_dashboard')
        elif self.request.user.is_active == True:
            return reverse_lazy('emp_dashboard')


class EmployeeDashboard(TemplateView):
    template_name = 'employee/emp_dashboard.html'