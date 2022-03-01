from django.db import models
from .laptop import Laptop

class LaptopItem(models.Model):
    laptop = models.OneToOneField(
        Laptop,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    price = models.FloatField()
    discount = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'uploads/images/book_items/')