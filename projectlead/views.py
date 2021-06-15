from django.shortcuts import redirect, render
from django.db.models import Max
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from hr.models import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.



# project leader index view
class LeaderDashboard(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(LeaderDashboard, self).get_context_data(**kwargs)
        context['project_count'] = Team.objects.filter(employee=self.request.user).count()
        context['task_count'] = Tasks.objects.count()
        context['employee_count'] = User.objects.count()
        return context 
    template_name = 'projectlead/ldr_dashboard.html'


class ProjectDetail(DetailView):
    model = Project
    template_name='projectlead/project-view.html'


class TaskCreate(CreateView): 
    model = Tasks
    fields = ['task', 'project',]
    success_url = reverse_lazy('tasks')
    template_name = 'projectlead/tasks.html'

    def get(self, request):
        tasks = Tasks.objects.filter(project=Project.objects.aggregate(Max('id')).get('id__max'))
        projects = Project.objects.all().order_by('-id')
        employee = User.objects.filter(is_superuser=False).exclude(id=request.user.id)
        context = {
            'tasks': tasks, 'projects': projects, 'employee': employee
        }
        return render(request, 'projectlead/tasks.html', context)


def task_view(request, pk):
    tasks = Tasks.objects.filter(project=pk)
    projects = Project.objects.all().order_by('-id')
    employee = User.objects.filter(is_superuser=False).exclude(id=request.user.id)
    context = {
        'tasks': tasks, 'projects': projects, 'employee': employee
    }
    return render(request, 'projectlead/tasks.html', context)


def task_delete(request, pk):
   task = Tasks.objects.get(id=pk)
   task.delete()
   return JsonResponse('true', safe=False)


def change_task_status(request, pk):
    task = Tasks.objects.get(id=pk)
    if task.task_complete == False:
        task.task_complete = True
        task.save()
    else:
        task.task_complete = False
        task.save()
    return redirect('tasks')


def assign_task(request, pk, id, uk):
    employee = User.objects.get(id=pk)
    task_id = Tasks.objects.get(id=id)
    project_id = Project.objects.get(id=uk)

    if  TaskAssigned.objects.filter(employee=employee, task=task_id, project=project_id):
        obj = TaskAssigned.objects.get(employee=employee, task=task_id, project=project_id)
        obj.delete()
        return JsonResponse('not selected', safe=False)
    else:
        TaskAssigned.objects.create(employee=employee, task=task_id, project=project_id)
        return JsonResponse('selected', safe=False)