from django.contrib import admin
# from .models import ProductList
from .models import ProductList, CartList, UserList

# Register your models here.

admin.site.register(ProductList)
admin.site.register(CartList)
admin.site.register(UserList)