from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, redirect_to_login

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from hr.models import Project
from employee.models import User


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
        context['leaders'] = User.objects.filter(is_staff=True)
        return context


class ProjectDetailView(DetailView):
    model = Project
    fields = '__all__'
    template_name='hr/project-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaders'] = User.objects.filter(is_staff=True)
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


  