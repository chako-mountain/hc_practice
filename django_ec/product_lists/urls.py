
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import include
from .views import product_list_view, product_detail_view, contents_add_function , delete_function, edit_function, update_function,admin_page,admin_product_list_view

urlpatterns = [
    path('lists' , product_list_view, name='lists' ),
    path('details' , product_detail_view, name='details' ),
    path('administrator/products', admin_product_list_view, name='administrator'),
    # path('detail/int< >' , showdetailfunction , name = 'showdetails')
    # path('detail/<int:id>/', showdetailfunction, name='detail'),
    path('detail/<int:id>/', product_detail_view, name='detail'),
    path('administrator/products/create', contents_add_function, name = "contents_add"),
    path('administrator/products/delete', delete_function , name = 'delete' ),
    path('administrator/products/<int:id>/edit', edit_function , name = 'edit' ),
    path('administrator/products/<int:id>/update', update_function , name = 'update' ),
    # path('signup', signup_function , name = "signup" ),
    # path('login', loginfunction , name = "login"),
    path("admin-basic/", admin_page, name="admin_page"),
]
