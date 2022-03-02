from django.db import models
from .clothes import Clothes

class ClothesItem(models.Model):
    clothes = models.OneToOneField(
        Clothes,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    price = models.FloatField()
    discount = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'uploads/images/clothes_items/')