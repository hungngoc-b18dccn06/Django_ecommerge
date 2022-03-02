from django.db import models
from django.urls import reverse
from .manufacture import Manufacture


class Laptop(models.Model):
    name = models.CharField(max_length=200)
    ram = models.IntegerField()
    screen = models.TextField(max_length=500)
    model = models.TextField(max_length=20, unique=True)

    manufacture = models.ManyToManyField(Manufacture,)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('laptop-detail', args=[str(self.id)])
