from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



# project leader index view
class LeaderDashboard(TemplateView):
    template_name = 'projectlead/ldr_dashboard.html'
