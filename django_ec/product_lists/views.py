from django.db import IntegrityError
from django.shortcuts import render, redirect
from product_lists.models import ProductList
from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from basicauth.decorators import basic_auth_required
from django.shortcuts import get_object_or_404
# from django.utils.decorators import method_decorator


def product_list_view(request):
    
    object_list = ProductList.objects.all()
    return render(request, 'lists.html', {'object_list': object_list})


def product_detail_view(request, id):

    related_products = ProductList.objects.order_by("-created_at")[:4]
    product = get_object_or_404(ProductList, id=id)
    return render(request, 'details.html', {"related_products": related_products, "product": product})
    

@basic_auth_required
def admin_product_list_view(request):
    object_list = ProductList.objects.all()
    return render(request, 'administrator.html', {'object_list': object_list})


@basic_auth_required
def product_create_view(request):

    if request.method == "POST":
        product_list = ProductList()
        # renderで返却するために、product_listに一旦値を格納しています。
        product_list.name = request.POST.get("name", "").strip()
        product_list.description = request.POST.get("description", "").strip()
        product_list.is_sale = request.POST.get("is_sale") == "on"
        product_list.img = request.POST["img"]
        product_list.price = request.POST["price"]
        product_list.star_rating = request.POST["rating"]
        
        try:
            price = int(product_list.price) if product_list.price else None
            star_rating = int(product_list.star_rating) if product_list.star_rating else None 
            # かた変換したものを上書き
            product_list.price = price
            product_list.star_rating = star_rating
            product_list.save()
            return redirect("administrator")    
         
        except (ValidationError, ValueError):
            print("this is validation error")
            error_message = "PriceまたはStar Ratingは整数で記入してね"
            return render(request, "administrator.html" ,{ "product_list" : product_list, "error_message":error_message })
        
    return redirect('administrator')


@basic_auth_required
def product_delete_view(request):
    delete_id = request.POST["post_id"]
    ProductList.objects.filter(id = delete_id).delete()
    print("deleted")
    return redirect('administrator')


@basic_auth_required
def product_edit_view(request, id):
    edit_list = ProductList.objects.get(id=id)
    return render(request, "edit.html" ,{ "edit_list" : edit_list })


@basic_auth_required
def product_update_view(request ,id):
    update_list = ProductList.objects.get(id=id)
    update_list.name = request.POST.get("name", "").strip()
    update_list.description = request.POST.get("description", "").strip()
    update_list.is_sale = request.POST.get("is_sale") == "on"
    update_list.img = request.POST["img"]

    # POSTデータを直接取得
    price_str = request.POST.get("price", "").strip()
    rating_str = request.POST.get("rating", "").strip()

    try: 
        price = int(price_str) if price_str else None
        star_rating = int(rating_str) if rating_str else None
        # 変換した値を代入
        update_list.price = price
        update_list.star_rating = star_rating
        update_list.save()
        return redirect("administrator") 
    except (ValidationError, ValueError):
        print("this is validation error")
        error_message = "PriceまたはStar Ratingは整数で記入してね"
        # 入力値を一時的に更新しておく
        update_list.price = price_str
        update_list.star_rating = rating_str
        return render(request, "edit.html", { "edit_list": update_list, "error_message": error_message })


@basic_auth_required
def admin_page(request):
    return redirect("administrator")


def add_products_view(request):
    print("called")
    print(request.POST["id"])
    return redirect("lists")

