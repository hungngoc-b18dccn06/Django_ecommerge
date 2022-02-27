from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('stores/', include('stores.urls')),
    path('admin/', admin.site.urls),
]
