from django.db import models

# Create your models here.


# class CartList(models.Model):
#     # user_id = models.IntegerField()
#     session_value = models.CharField(max_length=250, null = False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"CartList for user {self.user_id}"
    

class UserList(models.Model):
    session_value = models.CharField(max_length=250, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_value


class ProductList(models.Model):
    # id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(CartList,  on_delete=models.PROTECT)
    # user = models.ForeignKey(UserList, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    star_rating = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=False, null=False)
    is_sale = models.BooleanField(default=False)
    img = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class CartList(models.Model):
    user = models.ForeignKey(UserList, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductList, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
