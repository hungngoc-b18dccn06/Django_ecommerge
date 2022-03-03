from django.db import models
from django.urls import reverse

from .mobile_phone_manufacture import MobilePhoneManufacture

class MobilePhone(models.Model):

    name = models.CharField(max_length=50)
    screen = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)

    mobile_phone_manufacture= models.ForeignKey(
        MobilePhoneManufacture,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mobile-phone-detail', args=[str(self.id)])