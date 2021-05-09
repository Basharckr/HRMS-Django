from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from hr.models import *

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