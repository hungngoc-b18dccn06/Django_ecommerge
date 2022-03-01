from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    biography = models.CharField(max_length=200)

    def __str__(self):
        return self.name