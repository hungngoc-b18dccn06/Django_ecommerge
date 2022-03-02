from django.db import models
from .mobilephone import Mobilephone

class Mobilephone_item(models.Model):
    mobilephone = models.OneToOneField(
        Mobilephone,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    price = models.FloatField()
    discount = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'uploads/images/mobilephone_items/')