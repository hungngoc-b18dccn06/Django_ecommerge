from django.db import models
from django.urls import reverse

from ..product import Product

class MobilePhone(models.Model):

    screen = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.product.name