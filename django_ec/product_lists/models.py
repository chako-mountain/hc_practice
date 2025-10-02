# from django.db import models

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True 

    
# class UserList(BaseModel):
#     session_value = models.CharField(max_length=250, null = False)

#     def __str__(self):
#         return self.session_value


# class ProductList(BaseModel):
#     name = models.CharField(max_length=255, null=False)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
#     star_rating = models.IntegerField(null=True, blank=True)
#     description = models.TextField(blank=False, null=False)
#     is_sale = models.BooleanField(default=False)
#     img = models.URLField(max_length=500, null=True, blank=True)

#     def __str__(self):
#         return self.name
    
    

# # class CartList(BaseModel):
# #     user = models.ForeignKey(UserList, on_delete=models.PROTECT)
# #     product = models.ForeignKey(ProductList, on_delete=models.PROTECT)
# #     number = models.IntegerField(null = False, blank = False)

# #     def __str__(self):
# #         return str(self.user)

# class CartList(BaseModel):
#     user = models.ForeignKey(UserList, on_delete=models.PROTECT)
#     FirstName = models.CharField(max_length=255, null=False)
#     LastName = models.CharField(max_length=255, null=False)
#     Username = models.CharField(max_length=255, null=False)
#     Email= email = models.EmailField(max_length=254, unique=True)
#     Address = models.CharField(max_length=255, null=False)
#     Address = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user
    

# class CreditCard(BaseModel):
#     user = models.ForeignKey(CartList, on_delete=models.PROTECT)
#     NameOnCart = models.CharField(max_length=255, null=False)
#     CreditCardNumber = models.IntegerField(null=True, blank=True)
#     Exporation = models.CharField(max_length=255, null=False)
#     CVV = models.CharField(max_length=255, null=False)






# # class CartProduct(models.Model):
# #     user = models.ForeignKey(CartList, on_delete=models.PROTECT)
# #     product = models.ForeignKey(ProductList, on_delete=models.PROTECT)

# #     def __str__(self):
# #         return self.user



# from uuid import UUID
import uuid
from django.db import models
    
class CartList(models.Model):
    # session_value = models.CharField(max_length=250, null = False)
    session_key = models.UUIDField(default=uuid.uuid4(),editable=False,unique=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.session_key)


class ProductList(models.Model):
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
    

class CartProduct(models.Model):
    user = models.ForeignKey(CartList, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductList, on_delete=models.PROTECT)
    number = models.IntegerField(null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
