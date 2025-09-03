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
    
    def pay(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


# 一種類一インスタンスにしたかったが、ジュース一本で一インスタンスという要求より設計した
class Juice:

    def __init__ (self, name, price):
        self.price = price
        self.name = name

    def __del__(self):
        pass

    #  オブジェクト比較のため、eq と hashを追加

    def __eq__(self, other):
        if isinstance(other, Juice):
          return isinstance(other, Juice) and self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))
   
# canbuy 現在の持ち金で購入できるかを確認
# buying　購入時の処理を記述

class VendingMachine:

    stock: Dict[Juice, int]
    sales_total: int

    def __init__(self):
        self.stock = {}
        self.sales_total = 0

        self.add_stock(Juice("pepushi", 150), 5)
        self.add_stock(Juice("monster", 230), 5)
        self.add_stock(Juice("irohasu", 120), 5)

    def can_buy(self, juice: Juice, suica: Suica):
        return self.stock.get(juice, 0) > 0 and suica.deposit() >= juice.price
    
    # 標準出力は使えないことを考え、エラーで対処
    def buy(self, juice: Juice, suica: Suica):
        if juice not in self.stock:
            raise ValueError("指定された商品は存在しません")
        if self.stock[juice] <= 0:
            raise ValueError("指定された商品は在庫切れです")
        if not suica.pay(juice.price):
            raise ValueError("残高が不足しています")
        
        self.stock[juice] -= 1
        self.sales_total += juice.price

    def get_stock_count(self, juice: Juice):
        return self.stock.get(juice, 0)
    
    def add_stock(self, juice: Juice, count: int):
        if juice in self.stock:
            self.stock[juice] += count
        else:
            self.stock[juice] = count

    def get_all_stock(self):
        result = []
        for juice, count in self.stock.items():
            result.append((juice.name, count))
        return result

