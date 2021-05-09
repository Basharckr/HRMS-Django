from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from hr.models import *
from .models import *
# Create your views here.



# project leader index view
class LeaderDashboard(TemplateView):
    template_name = 'projectlead/ldr_dashboard.html'


class ProjectView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name='projectlead/ldr_projects.html'

class ProjectDetail(DetailView):
    model = Project
    template_name='projectlead/project-view.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = ['task',]
    success_url = reverse_lazy('tasks')
    template_name = 'projectlead/tasks.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()
        return context

