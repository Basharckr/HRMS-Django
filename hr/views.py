from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, redirect_to_login

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from hr.models import Project
from employee.models import User
from projectlead.models import Team
from django.db.models import Q
from django.http import HttpResponse


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
        context['team'] = Team.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    fields = '__all__'
    template_name='hr/project-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = User.objects.filter(is_superuser=False)
        context['leader'] = User.objects.filter(is_superuser=False)
        context['assigned'] = Team.objects.filter(project=self.kwargs.get('pk'))
        print(context['assigned'])

        employee_list = []
        leader_list = []

        for employee in employees:
            if employee.is_staff==True:
                leader_list.append(employee)
            else:
                employee_list.append(employee)
                
        context['employees'] = employee_list
        context['leaders'] = leader_list
        return context


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'hr/project-view.html'
    success_url = reverse_lazy('projects')



def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('projects')

def assign_employee(request, pk, id):
    employee = User.objects.get(id=pk)
    project = Project.objects.get(id=id)

    if  Team.objects.filter(employee=employee, project=project):
        obj = Team.objects.get(employee=employee, project=project)
        obj.delete()
        print('not')
        return JsonResponse('not selected', safe=False)
    else:
        Team.objects.create(employee=employee, project=project)
        print('yessssss')

        return JsonResponse('selected', safe=False)
       

    


  