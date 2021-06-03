from django.db import models
from django.contrib.auth import get_user_model
from hr.models import Project

User = get_user_model()
# Create your models here.

class Tasks(models.Model):
    task = models.TextField(max_length=100, blank=True, null=True)
    task_priority = models.CharField(max_length=100, default='low') 
    due_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, default='pending')


class Team(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class TaskAssigned(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    task_status = models.CharField(max_length=100, default='pending')

