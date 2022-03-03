from django.db import models
from .mobile_phone import MobilePhone

class MobilePhoneItem(models.Model):
    mobile_phone = models.OneToOneField(
        MobilePhone,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    price = models.FloatField()
    discount = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'uploads/images/mobile_phone_items/')