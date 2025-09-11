
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import include
from .views import listsfunction, detailsfunction, adminfunction, showdetailfunction

urlpatterns = [
    path('lists' , listsfunction, name='lists' ),
    path('details' , detailsfunction, name='details' ),
    path('administrator/', adminfunction, name='administrator'),
    # path('detail/int< >' , showdetailfunction , name = 'showdetails')
    # path('detail/<int:id>/', showdetailfunction, name='detail'),
    path('detail/<int:id>/', detailsfunction, name='detail'),
]
