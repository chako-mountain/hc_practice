
class Suica:

    
    now_money = 0

    # インスタンス生成時に500円をチャージ
    def __init__(self):
        
        self.now_money = 500
        # return now_money
    
    # how_manyに金額を指定してチャージ可能
    def Charge(self , how_many):
        if  how_many < 100:
            return self.now_money
        elif how_many >= 100:
            self.now_money  += how_many
        
        return self.now_money 
    
    # 貯金額をただ返すだけ
    def Deposit(self):
        return self.now_money


# 一種類一インスタンスにしたかったが、ジュース一本で一インスタンスという要求より設計した
class Juice:

    def __init__ (self , name , price):
        self.price = price
        self.name = name

    def __del__(self):
        pass


# canbuy 現在の持ち金で購入できるかを確認
# buying　購入時の処理を記述

class Buy:

    def canbuy (self , juicelist , index , price , mymoney):

        canbuy = False

        self.stock = []

        self.stock = juicelist
        self.mymoney = mymoney

        if len(self.stock) != 0 and price <= self.mymoney:
             canbuy = True
        
        return canbuy
    

    def buying(self , juicelist , index , price , mymoney):

        self.stock = juicelist
        self.mymoney = mymoney
        
        self.salesamount = 0

        if self.canbuy(juicelist , index , price , mymoney) == True:

            self.mymoney -= price
            del self.stock[index]
            self.salesamount = price
        
        return self.stock, self.mymoney, self.salesamount















