from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, redirect_to_login, LogoutView

from django.urls import reverse_lazy

from .forms import SignUpFrom
from hr.models import *
from projectlead.models import *
# Create your views here.


#user signUp
class SignUpView(CreateView):
    form_class = SignUpFrom
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'


# user login
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


#user logout
class CustomLogoutView(LogoutView):
    next_page = 'login'

class EmployeeDashboard(TemplateView):
    template_name = 'employee/emp_dashboard.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     tasks = TaskAssigned.objects.filter(employee=self.request.user).count()
    #     for task in tasks:
    #         if task.task.task_complete()
    #     return context


def emp_profile(request):
 

    team = Team.objects.all()

 

    if request.user.is_superuser:
        project = Project.objects.all()

    else:       
        project = Team.objects.filter(employee=request.user)
    context = {
        'project': project, 'team': team
    }
    return render(request, 'account/profile.html', context)