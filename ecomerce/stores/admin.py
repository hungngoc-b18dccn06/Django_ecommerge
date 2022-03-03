from unicodedata import category
from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Publisher, Author, Book, BookItem 
from .models import Laptop ,LaptopItem, LaptopManufacture
from .models import Clothes, ClothesManufacture, ClothesItem
from .models import MobilePhone, MobilePhoneItem, MobilePhoneManufacture

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'gender', 'material']

class ClothesManufactureAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']

class ClothesItemAdmin(admin.ModelAdmin):

    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))
    
    def clothes_name(self, obj):
        return obj.clothes.name
    
    image_view.short_description = 'IMAGE'
    clothes_name.short_description = 'NAME'
    list_display = ['image_view', 'clothes_name', 'price', 'discount']

admin.site.register(Clothes, ClothesAdmin)
admin.site.register(ClothesItem, ClothesItemAdmin)
admin.site.register(ClothesManufacture, ClothesManufactureAdmin)

class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen', 'model', 'ram']

class MobilePhoneManufactureAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'phone']

class MobilePhoneItemAdmin(admin.ModelAdmin):

    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))
    
    def mobile_phone_name(self, obj):
        return obj.mobile_phone.name
    
    image_view.short_description = 'IMAGE'
    mobile_phone_name.short_description = 'NAME'
    list_display = ['image_view', 'mobile_phone_name', 'price', 'discount']


admin.site.register(MobilePhone, MobilePhoneAdmin)
admin.site.register(MobilePhoneItem, MobilePhoneItemAdmin)
admin.site.register(MobilePhoneManufacture, MobilePhoneManufactureAdmin)

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen', 'model']

class LaptopItemAdmin(admin.ModelAdmin):
    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))
    
    def laptop_name(self, obj):
        return obj.laptop.name
    
    image_view.short_description = 'IMAGE'
    laptop_name.short_description = 'NAME'
    list_display = ['image_view', 'laptop_name', 'price', 'discount']

class LaptopManufactureAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone','email']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'biography']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']

admin.site.register(Laptop, LaptopAdmin)
admin.site.register(LaptopItem, LaptopItemAdmin)
admin.site.register(LaptopManufacture, LaptopManufactureAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'age_range']

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'summary']
    search_fields = ['name', 'language']
    filter_horizontal = ['authors', 'categories']

class BookItemAdmin(admin.ModelAdmin):
    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))
    
    def book_name(self, obj):
        return obj.book.name
    
    image_view.short_description = 'IMAGE'
    book_name.short_description = 'NAME'
    list_display = ['image_view', 'book_name', 'price', 'discount']
    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookItem, BookItemAdmin)

