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



class Juice:

    def __init__ (self, name, price):
        self.price = price
        self.name = name

    #  オブジェクト比較のため、eq と hashを追加

    def __eq__(self, other):
        # if isinstance(other, Juice):
          return isinstance(other, Juice) and self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))
    
   
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
    
    
    # 購入できるジュースを名前で指名
    def get_canbuy_juice_name(self):
        return [juice.name for juice in self.stock.keys()]
    

    # 有効な名前のジュースかを判定
    def get_juice_by_name(self, name: str):
        for juice in self.stock.keys():
            if juice.name == name:
                return juice
        raise ValueError("指定された商品は存在しません")
    
    
    # 購入処理
    def buy(self, juice_name: str, suica: Suica):

        try:
            juice = self.get_juice_by_name(juice_name)
        except ValueError:
            raise ValueError("指定された商品は存在しません")
        
        if self.stock[juice] <= 0:
            raise ValueError("指定された商品は在庫切れです")
        if not suica.pay(juice.price):
            raise ValueError("残高が不足しています")
        
        self.stock[juice] -= 1
        self.sales_total += juice.price
        return juice