from django.db import models
from django.urls import reverse
from .laptop_manufacture import LaptopManufacture


class Laptop(models.Model):
    name = models.CharField(max_length=200)
    ram = models.CharField(max_length=20)
    screen = models.CharField(max_length=500)
    model = models.CharField(max_length=20, unique=True)

    laptop_manufacture= models.ForeignKey(
        LaptopManufacture,
        null=True,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('laptop-detail', args=[str(self.id)])
