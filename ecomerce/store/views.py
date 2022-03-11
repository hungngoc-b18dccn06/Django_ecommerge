from numpy import product
from .models.product.product import Product
from .models.product.book.book import Book
from .models.product.item import Item

from .serializers.product.product_serializer import ProductSerializer
from .serializers.product.book_serializer import BookSerializer
from .serializers.product.item_serializer import ItemSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render

from django.http import HttpResponse

import io

# Create your views here.
def index(request):
    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)
    products_jsonRender = JSONRenderer().render(products_serializer.data)
    stream = io.BytesIO(products_jsonRender)
    products_jsonParser = JSONParser().parse(stream)
    print(products_jsonParser)

    context = {
        'books': [p for p in products_jsonParser if p['category']['id'] == 1],
        'laptops': [p for p in products_jsonParser if p['category']['id'] == 2],
        'moblie_phones': [p for p in products_jsonParser if p['category']['id'] == 3],
        'clothes': [p for p in products_jsonParser if p['category']['id'] == 4],
    }

    return render(request, 'store/products.html', context)

def getItems(request):
    items = Item.objects.all()
    items_serializer = ItemSerializer(items, many=True)
    items_jsonRender = JSONRenderer().render(items_serializer.data)
    stream = io.BytesIO(items_jsonRender)
    items_jsonParser = JSONParser().parse(stream)

    context = {
        'books': [i for i in items_jsonParser if i['product']['category']['id'] == 1],
        'laptops': [i for i in items_jsonParser if i['product']['category']['id'] == 2],
        'moblie_phones': [i for i in items_jsonParser if i['product']['category']['id'] == 3],
        'clothes': [i for i in items_jsonParser if i['product']['category']['id'] == 4],
    }

    return render(request, 'store/items.html', context)