from typing import Dict

class Suica:

    
    balance = 0

    # インスタンス生成時に500円をチャージ
    def __init__(self):
        
        self.balance = 500
        # return balance
    
    # amountに金額を指定してチャージ可能
    def charge(self, amount):
        if  amount < 100:
            raise ValueError("100円以上の金額をチャージしてください")
        elif amount >= 100:
            self.balance  += amount
        
        return self.balance 
    
    # 貯金額をただ返すだけ
    def deposit(self):
        return self.balance


# 一種類一インスタンスにしたかったが、ジュース一本で一インスタンスという要求より設計した
class Juice:

    def __init__ (self, name, price):
        self.price = price
        self.name = name

    def __del__(self):
        pass


# canbuy 現在の持ち金で購入できるかを確認
# buying　購入時の処理を記述

class VendingMachine:

    stock: Dict[Juice, int]
    sales_total: int

    def __init__(self):
        self.stock = {}
        self.sales_total = 0

    def can_buy(self, juice: Juice, mymoney: int) :
        if juice in self.stock and self.stock[juice] > 0 and juice.price <= mymoney:
            return True
        return False
    
    def buy(self, juice: Juice, mymoney: int):
        if self.can_buy(juice, mymoney):
            self.stock[juice] -= 1
            self.sales_total += juice.price
            mymoney -= juice.price
        return mymoney
    
    def get_stock_count(self, name):
        return self.stock[name]
    
    def add_stock(self, juice: Juice, count: int):
        if juice in self.stock:
            self.stock[juice] += count
        else:
            self.stock[juice] = count

