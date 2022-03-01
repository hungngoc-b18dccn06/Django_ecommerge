from django.db import models
from django.urls import reverse

from .author import Author
from .category import Category
from .publisher import Publisher


class Book(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('vi', 'Vietnamese'),
        ('kr', 'Korean'),
        ('cn', 'Chinese')
    ]
    name = models.CharField(max_length=200)
    language = models.CharField(
        max_length=3,
        choices=LANGUAGES,
    )
    number_of_pages = models.IntegerField()
    summary = models.TextField(max_length=500)
    isbn = models.CharField(max_length=20, unique=True)

    publisher = models.ForeignKey(
        Publisher, 
        null=True, 
        on_delete=models.CASCADE,
    )

    category = models.ManyToManyField(Category,)
    author = models.ManyToManyField(Author,)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
