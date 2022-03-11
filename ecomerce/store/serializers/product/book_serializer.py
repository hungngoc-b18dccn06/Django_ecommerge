
from rest_framework import  serializers
from ...models.product.book.book import Book
from .product_serializer import ProductSerializer

class BookSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1