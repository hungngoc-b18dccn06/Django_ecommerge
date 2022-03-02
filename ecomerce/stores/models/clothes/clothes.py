from django.db import models
from django.urls import reverse

from .clothes_manufacture import Clothes_manufacture

class Clothes(models.Model):

      name = models.CharField(max_length=50)
      color = models.CharField(max_length=20)
      age = models.CharField(max_length=20)
      gender = models.CharField(max_length=20)
      material = models.CharField(max_length=50)

      clothes_manufacture= models.ManyToManyField(Clothes_manufacture,)

def __str__(self):
    return self.name

def get_absolute_url(self):
        return reverse('clothes-detail', args=[str(self.id)])

