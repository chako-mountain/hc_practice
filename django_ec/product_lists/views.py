from django.shortcuts import render
from product_lists.models import ProductList
from django.http import HttpResponseRedirect 


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

# def contents_add_function(request):
#     print("called")
    
#     if request.method == "POST":
    
#         name = request.POST["name"]

#     return render(request, "contents.html")


# 以下は無視してください
def contents_add_function(request):


    if request.method == "POST":

        product_list = ProductList()
        product_list.name = request.POST["name"]
        product_list.price = request.POST["price"]
        product_list.star_rating = request.POST["rating"]
        product_list.description = request.POST["description"]
        product_list.is_sale = request.POST.get("is_sale") == "on"
        product_list.img = request.POST["img"]



        print("this is name")
        print(product_list.name)

        product_list.save()



        print("called")  # 呼び出されたか確認
        print("Method:", request.method)  # POST かどうか
        print("POST data:", request.POST)  # 送信データの中身

    return render(request, "contents.html")


def delete_function(request):
    print("called")
    model = ProductList
    
    delete_id = request.POST["post_id"]
    model.objects.filter(id = delete_id).delete()
    print("deleted")
    return render(request, "test.html")


def edit_function(request):
    print("edit is called")
    model = ProductList

    edit_id = request.POST["edit_id"]
    print(edit_id)
    edit_list = model.objects.get(id = edit_id)

    img = edit_list.img
    print("edit_list")
    print(edit_list)
    print(img)
    return render(request, "edit.html" ,{ "edit_list" : edit_list })


def update_function(request):

    product_id = request.POST.get("product_id")
    update_list = ProductList.objects.get(id=product_id)

     

    update_list.name = request.POST["name"]
    update_list.price = request.POST["price"]
    update_list.star_rating = request.POST["rating"]
    update_list.description = request.POST["description"]
    update_list.is_sale = request.POST.get("is_sale") == "on"
    update_list.img = request.POST["img"]

    print("imgですよ")
    print(update_list.img)
    update_list.save()



    return render(request, "administrator.html" )

  

