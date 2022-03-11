from .models.product.product import Product
from .models.product.book.book import Book
from .models.product.item import Item

from .serializers.product.product_serializer import ProductSerializer
from .serializers.product.book_serializer import BookSerializer
from .serializers.product.item_serializer import ItemSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render

import io

# Create your views here.
def index(request):
    items = Item.objects.all()
    items_serializer = ItemSerializer(items, many=True)
    items_jsonRender = JSONRenderer().render(items_serializer.data)
    stream = io.BytesIO(items_jsonRender)
    items_jsonParser = JSONParser().parse(stream)

    context = {
        'books': [p for p in items_jsonParser if p['product']['category']['id'] == 1],
        'laptops': [p for p in items_jsonParser if p['product']['category']['id'] == 2],
        'moblie_phones': [p for p in items_jsonParser if p['product']['category']['id'] == 3],
        'clothes': [p for p in items_jsonParser if p['product']['category']['id'] == 4],
    }

    return render(request, 'store/test.html', context)