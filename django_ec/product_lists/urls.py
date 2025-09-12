
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import include
from .views import listsfunction, detailsfunction, adminfunction, showdetailfunction, contents_add_function , delete_function, edit_function, update_function

urlpatterns = [
    path('lists' , listsfunction, name='lists' ),
    path('details' , detailsfunction, name='details' ),
    path('administrator/', adminfunction, name='administrator'),
    # path('detail/int< >' , showdetailfunction , name = 'showdetails')
    # path('detail/<int:id>/', showdetailfunction, name='detail'),
    path('detail/<int:id>/', detailsfunction, name='detail'),
    path('administrator/submit/', contents_add_function, name = "contents_add"),
    path('administrator/submit2/', delete_function , name = 'delete' ),
    path('administrator/submit3/', edit_function , name = 'delete' ),
    path('administrator/submit3/submit4/', update_function , name = 'delete' )
]
