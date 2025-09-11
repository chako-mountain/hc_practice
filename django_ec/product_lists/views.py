from django.shortcuts import render
from product_lists.models import ProductList

# Create your views here.
def listsfunction(request):
    model = ProductList
    object_list = model.objects.all()
    return render(request, 'lists.html', {'object_list': object_list})

def detailsfunction(request, id):
    targetid = id
    model = ProductList
    object_list = model.objects.all()
    related_products = {
        "first" : object_list.order_by("-created_at").first(),
        "second" : object_list.order_by("-created_at")[1],
        "third" : object_list.order_by("-created_at")[2],
        "fourth" : object_list.order_by("-created_at")[3]
    }

    info = model.objects.get(id = targetid)
    return render(request, 'details.html', {"related_products": related_products, "info": info})

def adminfunction(request):
    model = ProductList
    object_list = model.objects.all()
    return render(request, 'administrator.html', {'object_list': object_list})

def showdetailfunction(request, id):
    targetid = id
    model = ProductList
    info = model.objects.get(id = targetid)
    return render(request, 'details.html', {'info':info})



    