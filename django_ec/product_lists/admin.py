from django.contrib import admin
# from .models import ProductList
from .models import ProductList, CartList 

# Register your models here.

admin.site.register(ProductList)
admin.site.register(CartList)