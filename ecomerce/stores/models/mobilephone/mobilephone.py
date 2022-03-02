from django.db import models
from django.urls import reverse

from .mobilephone_manufacture import Mobilephone_manufacture

class Mobilephone(models.Model):

      name = models.CharField(max_length=50)
      screen = models.CharField(max_length=20)
      model = models.CharField(max_length=20)
      ram = models.CharField(max_length=20)

      mobilephone_manufacture= models.ManyToManyField(Mobilephone_manufacture,)

def __str__(self):
    return self.name

def get_absolute_url(self):
        return reverse('mobilephone-detail', args=[str(self.id)])