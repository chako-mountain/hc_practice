
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import include
from .views import listsfunction, detailsfunction, adminfunction

urlpatterns = [
    path('lists' , listsfunction, name='lists' ),
    path('details' , detailsfunction, name='details' ),

    path('administrator/', adminfunction, name='administrator'),
]
