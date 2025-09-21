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
    # product = ProductList.objects.get(id=id)
    product = get_object_or_404(ProductList, id=id)
    return render(request, 'details.html', {"related_products": related_products, "product": product})
    

@basic_auth_required
def admin_product_list_view(request):
    object_list = ProductList.objects.all()
    return render(request, 'administrator.html', {'object_list': object_list})


# @basic_auth_required
# def contents_add_function(request):

#     if request.method == "POST":
#         product_list = ProductList()
#         try:  
#             product_list.name = request.POST["name"]
#             product_list.price = request.POST["price"]
#             product_list.star_rating = request.POST["rating"]
#             product_list.description = request.POST["description"]
#             product_list.is_sale = request.POST.get("is_sale") == "on"
#             product_list.img = request.POST["img"]
#             product_list.save()
#             return redirect("administrator")     
#         except (ValidationError, ValueError):
#             print("this is validation error")
#             error_message = "PriceまたはStar Ratingは整数で記入してね"
#             return render(request, "administrator.html" ,{ "product_list" : product_list, "error_message":error_message })
        
#     return redirect('administrator')

@basic_auth_required
def contents_add_function(request):

    if request.method == "POST":
        product_list = ProductList()

        # renderで返却するために、product_listに一旦値を格納しています。
        product_list.name = request.POST.get("name", "").strip()
        product_list.price = request.POST["price"]
        product_list.star_rating = request.POST["rating"]
        product_list.description = request.POST.get("description", "").strip()
        product_list.is_sale = request.POST.get("is_sale") == "on"
        product_list.img = request.POST["img"]
        
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
def delete_function(request):
    # print("called")
    delete_id = request.POST["post_id"]
    ProductList.objects.filter(id = delete_id).delete()
    print("deleted")
    # return render(request, "test.html")
    return redirect('administrator')


@basic_auth_required
def edit_function(request, id):
    # model = ProductList
    # edit_id = request.POST["edit_id"]
    edit_id = id
    edit_list = ProductList.objects.get(id=edit_id)
    img = edit_list.img
    return render(request, "edit.html" ,{ "edit_list" : edit_list })


@basic_auth_required
def update_function(request ,id):

    # product_id = request.POST.get("product_id")
    product_id = id


    update_list = ProductList.objects.get(id=product_id)
    update_list.name = request.POST.get("name", "").strip()
    update_list.price = request.POST["price"]
    update_list.star_rating = request.POST["rating"]
    update_list.description = request.POST.get("description", "").strip()
    update_list.is_sale = request.POST.get("is_sale") == "on"
    update_list.img = request.POST["img"]

    try: 

        price = int(update_list.price) if update_list.price else None
        star_rating = int(update_list.star_rating) if update_list.star_rating else None
        
        # かた変換したものを上書き
        update_list.price = price
        update_list.star_rating = star_rating
        
        update_list.save()

        return redirect("administrator") 
    
    except (ValidationError, ValueError):
        print("this is validation error")
        error_message = "PriceまたはStar Ratingは整数で記入してね"
        return render(request, "edit.html" ,{ "edit_list" : update_list, "error_message":error_message })

    # return redirect('administrator')
    # return render(request, "administrator.html" )


@basic_auth_required
def admin_page(request):
    # return render(request, "administrator.html")
    return redirect("administrator")
