from django.db import IntegrityError
from django.shortcuts import render, redirect
from product_lists.models import ProductList, UserList, CartList
from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from basicauth.decorators import basic_auth_required
from django.shortcuts import get_object_or_404
import uuid


def product_list_view(request):

    session_database = UserList()
    session_value_b = request.session.get('key', None)

    if session_value_b == None:
        print("新規ユーザー")
        session_value_b = str(uuid.uuid4())
        request.session['key'] = session_value_b
        print(session_value_b)
        session_database.session_value = session_value_b
        session_database.save()
    
    if UserList.objects.filter(session_value=session_value_b).exists():
        print(session_value_b)
        print("既存のユーザー")

    if session_value_b != None and not UserList.objects.filter(session_value=session_value_b).exists():
        session_database.session_value = session_value_b
        session_database.save()

    try:
        user_id = UserList.objects.get(session_value=session_value_b)
        goods_sum = CartList.objects.filter(user=user_id)
        item_sum = 0

        for item in goods_sum:
            item_sum += item.number

        print(goods_sum)

        print("this is goods_sum_objects")
    
    except CartList.DoesNotExist:
        print("not exist")

    object_list = ProductList.objects.all()
    return render(request, 'lists.html', {'object_list': object_list, "item_sum":item_sum})


def product_detail_view(request, id,):
    session_value_b = request.session.get('key', None)

    try:

        user_id = UserList.objects.get(session_value=session_value_b)
        goods_sum = CartList.objects.filter(user=user_id)
        item_sum = 0

        for item in goods_sum:
            item_sum += item.number
    
    except CartList.DoesNotExist:
        print("not exist")

    related_products = ProductList.objects.order_by("-created_at")[:4]
    product = get_object_or_404(ProductList, id=id)
    return render(request, 'details.html', {"related_products": related_products, "product": product, "item_sum":item_sum})
    

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

    if request.method == "POST":
        session_value_b = request.session.get('key', 'none')

        user_instance = UserList.objects.get(session_value=session_value_b)

        product_id = request.POST.get("id")  # formから送信されたproductのID
        product_instance = ProductList.objects.get(id=product_id)

        if request.POST.get("source") == "from_lists":
            try:
                aim_cart = CartList.objects.get(user=user_instance, product=product_instance)

                aim_cart.number += 1  # numberをインクリメント
                aim_cart.save()       # 既存レコードを更新

                print("from_lists and 2回目")

            except CartList.DoesNotExist:
                # まだ存在していない場合は新規作成
                carts = CartList(user=user_instance, product=product_instance, number=1)
                carts.save()
                print("from_lists and 初回追加")


        if request.POST.get("source") == "from_details":

            try:
                aim_cart = CartList.objects.get(user=user_instance, product=product_instance)

                aim_cart.number += int(request.POST.get("number"))

                print("複数回目の追加")

                aim_cart.save()       

            except CartList.DoesNotExist:
                # まだ存在していない場合は新規作成
                carts = CartList(user=user_instance, product=product_instance, number=request.POST.get("number"))
                carts.save()
                print("from_lists and 初回追加")

    return redirect("lists")



def cart_view(request):
    session_value_b = request.session.get('key', 'none')

    try:
        user_instance = UserList.objects.get(session_value=session_value_b)
        carts = CartList.objects.filter(user=user_instance)

        print(carts)  # クエリセット全体を表示

        total_price = 0
        total_goods = 0

        for cart in carts:
            price = cart.product.price*cart.number
            total_price += price
            total_goods += cart.number

        return render(request, "carts.html", {"carts": carts, "total_price": total_price, "total_number": total_goods})

    except UserList.DoesNotExist:
        print("ユーザーが見つかりませんでした")
        return render(request, "carts.html", {"carts": []})


def cart_delete_view(request):

    id = request.POST.get("delete")
    delete_col = CartList.objects.get(id=id)
    delete_col.delete()

    print(id)
    print("called")
    return redirect("cart")