from django.shortcuts import render
from .models import ProductList

# Create your views here.
def listsfunction(request):
    model = ProductList
    object_list = model.objects.all()
    return render(request, 'lists.html', {'object_list': object_list})

def detailsfunction(request):
    return render(request, 'product_details/details.html', {})

def adminfunction(request):
    model = ProductList
    object_list = model.objects.all()
    return render(request, 'administrator.html', {'object_list': object_list})
    