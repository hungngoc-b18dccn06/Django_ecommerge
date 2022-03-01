from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Publisher, Author, Book, BookItem


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'biography']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'age_range']

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'summary']
    search_fields = ['name', 'language']

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