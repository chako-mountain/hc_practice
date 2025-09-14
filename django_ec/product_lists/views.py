from django.db import IntegrityError
from django.shortcuts import render, redirect
from product_lists.models import ProductList
from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from basicauth.decorators import basic_auth_required
# from django.utils.decorators import method_decorator


# Create your views here.
def product_list_view(request):
    model = ProductList
    object_list = model.objects.all()
    return render(request, 'lists.html', {'object_list': object_list})


def product_detail_view(request, id):
    # targetid = id
    model = ProductList
    object_list = model.objects.all()
    related_products = object_list.order_by("-created_at")[:4]
    print("リスト表示したい")
    print(related_products)
    product = model.objects.get(id = id)
    return render(request, 'details.html', {"related_products": related_products, "product": product})
    
    
def product_admin_view(request):
    model = ProductList
    object_list = model.objects.all()
    return render(request, 'administrator.html', {'object_list': object_list})


def showdetailfunction(request, id):
    targetid = id
    model = ProductList
    info = model.objects.get(id=targetid)
    return render(request, 'details.html', {'info':info})


# 以下は無視してください。実装の途中です。
@basic_auth_required
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

    # return render(request, "contents.html")
    return redirect("../")


def delete_function(request):
    print("called")
    model = ProductList
    delete_id = request.POST["post_id"]
    model.objects.filter(id = delete_id).delete()
    print("deleted")
    # return render(request, "test.html")
    return redirect("../")


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

    return redirect("../../")
    # return render(request, "administrator.html" )

  
def signup_function(request):

    if request.method == "POST":
        user_name = request.POST["user_name"]
        passward = request.POST["passward"]
        try:
            user = User.objects.create_user(user_name , '' , passward)
        except IntegrityError:
            return render(request, "signup.html", {"error":"このユーザーは登録済みです"})


    return render(request, "signup.html" )


# def loginfunction(request):
#     if request.method == "POST":
#         username = request.POST["user_name"]
#         password = request.POST["passward"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return(render(request, "login.html", {"content":"logged in"}))
#         else:
#             return render(request, "login.html", {"content": "not logged in"})
        
#     return render(request, "login.html", {"content": "not logged in"})


# @basic_auth_required
# def loginfunction(request):

#     users = getattr(settings, 'BASICAUTH_USERS', {})
#     if request.method == "POST":
#         username = request.POST["user_name"]
#         password = request.POST["passward"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return(render(request, "login.html", {"content":"logged in"}))
#         else:
#             return render(request, "login.html", {"content": "not logged in"})
        
#     return render(request, "login.html", {"content": "not logged in"})


@basic_auth_required
def admin_page(request):
    # return render(request, "administrator.html")
    return redirect("administrator")