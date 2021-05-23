from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500, blank=True, null=True)
    

    
