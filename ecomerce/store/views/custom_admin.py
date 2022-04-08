from store.models.product.product import Product
from store.models.product.category import Category
from store.models.product.item import Item

from store.serializers.product.product_serializer import ProductSerializer
from store.serializers.product.item_serializer import ItemSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from store.forms.product_form import ProductForm
from store.forms.book_form import BookForm
from store.forms.laptop_form import LaptopForm
from store.forms.mobile_phone_form import MobilePhoneForm
from store.forms.item_form import ItemForm
import io

# Create your views here.
def admin(request):
    products = Product.objects.filter(category=1)
    products_serializer = ProductSerializer(products, many=True)
    products_jsonRender = JSONRenderer().render(products_serializer.data)
    stream = io.BytesIO(products_jsonRender)
    products_jsonParser = JSONParser().parse(stream)

    context = {
        'books': products_jsonParser,
    }

    return render(request, 'store/book_products.html', context)

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
        # 'clothes': [i for i in items_jsonParser if i['product']['category']['id'] == 4],
    }

    return render(request, 'store/items.html', context)

def addBook(request):
    if (request.method=="POST"):
        product_form = ProductForm(request.POST)
        book_form = BookForm(request.POST)
        if product_form.is_valid() and book_form.is_valid():

            product = product_form.save(commit = False)
            category = Category.objects.get(pk=1)
            product.category = category
            product.save()

            book = book_form.save(commit = False)
            book.product = product 
            book.save()

            return redirect('/')
    else:
        product_form = ProductForm()
        book_form = BookForm()
        return render(request, 'store/add_book.html',
            {
                'product_form': product_form,
                'book_form': book_form
            }
        )
    
def addLaptop(request):
    if (request.method=="POST"):
        product_form = ProductForm(request.POST)
        laptop_form = LaptopForm(request.POST)
        if product_form.is_valid() and laptop_form.is_valid():

            product = product_form.save(commit = False)
            category = Category.objects.get(pk=2)
            product.category = category
            product.save()

            laptop = laptop_form.save(commit = False)
            laptop.product = product 
            laptop.save()

            return redirect('/')
    else:
        product_form = ProductForm()
        laptop_form = LaptopForm()
        return render(request, 'store/add_laptop.html',
            {
                'product_form': product_form,
                'laptop_form': laptop_form,
            }
        )
    
    
def addMobilePhone(request):
    if (request.method=="POST"):
        product_form = ProductForm(request.POST)
        mobile_phone_form = MobilePhoneForm(request.POST)
        if product_form.is_valid() and mobile_phone_form.is_valid():

            product = product_form.save(commit = False)
            category = Category.objects.get(pk=3)
            product.category = category
            product.save()

            mobile_phone = mobile_phone_form.save(commit = False)
            mobile_phone.product = product 
            mobile_phone.save()

            return redirect('/')
    else:
        product_form = ProductForm()
        mobile_phone_form = MobilePhoneForm()
        return render(request, 'store/add_mobile_phone.html',
            {
                'product_form': product_form,
                'mobile_phone_form': mobile_phone_form,
            }
        )
    
def addItem(request, product_id):
    if (request.method=="POST"):
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            print("hi")
            print(product_id)
    else:
        item_form = ItemForm()
        return render(request, 'store/add_item.html',
            {
                'product_id': product_id,
                'item_form': item_form,
            }
        )
    
