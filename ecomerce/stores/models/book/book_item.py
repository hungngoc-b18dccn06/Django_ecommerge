from django.db import models
from .book import Book

class BookItem(models.Model):
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    price = models.FloatField()
    discount = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'uploads/images/book_items/')