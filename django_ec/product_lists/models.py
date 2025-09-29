from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # ← これがないと普通のテーブルとして作られてしまう

    
class UserList(BaseModel):
    session_value = models.CharField(max_length=250, null = False)

    def __str__(self):
        return self.session_value


class ProductList(BaseModel):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    star_rating = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=False, null=False)
    is_sale = models.BooleanField(default=False)
    img = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    

class CartList(BaseModel):
    user = models.ForeignKey(UserList, on_delete=models.PROTECT)
    product = models.ForeignKey(ProductList, on_delete=models.PROTECT)
    number = models.IntegerField(null = False, blank = False)

    def __str__(self):
        return str(self.user)
