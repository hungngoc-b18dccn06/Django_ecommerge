from django.db import models
from django.urls import reverse

from ..product import Product

class Clothes(models.Model):

    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    material = models.CharField(max_length=50)

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.product.name


