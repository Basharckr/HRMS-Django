from django.db import models
from django.contrib.auth import get_user_model
from hr.models import Project

User = get_user_model()
# Create your models here.

class Tasks(models.Model):
    task = models.TextField(max_length=100, blank=True, null=True)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    task_complete = models.BooleanField(default=False)


class Team(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

