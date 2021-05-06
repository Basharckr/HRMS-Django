from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, redirect_to_login

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from . models import *

# Create your views here.







# HR index
class HrDashboard(TemplateView):   
    template_name = 'hr/hr_dashboard.html'

    

class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projects')
    template_name = 'hr/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projects')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')


  