from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
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
        context['tasks'] = Tasks.objects.all().order_by('-id')
        context['employee'] = User.objects.filter(is_staff=False, is_superuser=False)
     
        return context


def task_delete(request, pk):
   task = Tasks.objects.get(id=pk)
   task.delete()
   return redirect('tasks')

def change_task_status(request, pk):
    task = Tasks.objects.get(id=pk)
    if task.task_complete == False:
        task.task_complete = True
        task.save()
    else:
        task.task_complete = False
        task.save()
    return redirect('tasks')
