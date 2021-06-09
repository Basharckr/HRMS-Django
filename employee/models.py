from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    number = models.CharField(max_length=15, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True, default='developer')
    image = models.ImageField(blank=True, null=True, upload_to='images', default='images/images.profile.png')

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
  
