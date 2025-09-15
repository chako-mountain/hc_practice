
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import include
from .views import product_list_view, product_detail_view, product_admin_view, showdetailfunction, contents_add_function , delete_function, edit_function, update_function,signup_function,admin_page,carts_function

urlpatterns = [
    path('lists' , product_list_view, name='lists' ),
    path('details' , product_detail_view, name='details' ),
    path('administrator/', product_admin_view, name='administrator'),
    # path('detail/int< >' , showdetailfunction , name = 'showdetails')
    # path('detail/<int:id>/', showdetailfunction, name='detail'),
    path('detail/<int:id>/', product_detail_view, name='detail'),
    path('administrator/submit/', contents_add_function, name = "contents_add"),
    path('administrator/submit_delete/', delete_function , name = 'delete' ),
    path('administrator/submit_edit/', edit_function , name = 'delete' ),
    path('administrator/submit_edit/submit_update/', update_function , name = 'delete' ),
    path('signup', signup_function , name = "signup" ),
    # path('login', loginfunction , name = "login"),
    path("admin-basic/", admin_page, name="admin_page"),
    path('submit_to_cart', carts_function , name = "carts")

]
