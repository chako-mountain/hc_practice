from vending_class import Suica, Juice ,VendingMachine

suica = Suica()

vending = VendingMachine()


# p = Juice("pepushi",150)
# pepushis = [p,p,p,p,p]

# m = Juice("monster",230)
# monsters = [m,m,m,m,m]

# i = Juice("irohasu",120)
# irohasus = [i,i,i,i,i]

pepushi = Juice("pepushi", 150)
vending.add_stock(pepushi, 5)

monster = Juice("monster", 230)
vending.add_stock(monster, 1)

irohasu = Juice("irohasu", 120)
vending.add_stock(irohasu, 5)

total_sales = 0

zankin = suica.deposit()

while(1):

    # deposit 残金確認
    # charge 金額チャージ
    command = input("実行したい処理を書いてください : \n"
                    "deposit : 現在の持ち金を確認します\n"
                    "charge : 現金をスイカにチャージします\n"
                    "zaiko : 商品在庫を確認します\n"
                    "zaiko_chaege : 在庫が足りない場合、在庫を補填します\n"
                    "buy : 商品を購入します\n"
                    "sales_amount : 自動販売機の合計売り上げを表示します\n"
                    "q : 処理から抜けます\n")

    if command == "deposit":
        print(str(f"現在の残高は、{suica.deposit()}円です"))

    elif command == "charge":    
        try:
            suica_charge = int(input("100円以上のチャージ金額を指定してください"))
            suica.charge(suica_charge)
            zankin = suica.deposit()
            print(f"{suica_charge}円チャージされ、残金{zankin}円です")
        except ValueError as e:
            print(e)

    
    elif command == "zaiko":
        goods = input("在庫を確認したい商品を指定してください。三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")

        if goods == "pepushi":
            print(f"在庫は{vending.get_stock_count(pepushi)}個です")
        elif goods == "monster":
            print(f"在庫は{vending.get_stock_count(monster)}個です")
        elif goods == "irohasu":
            print(f"在庫は{vending.get_stock_count(irohasu)}個です")


    elif command == "zaiko_charge":
        
        goods = input("どの商品の在庫を補填するか選択してください。以下三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")
        
        if goods == "pepushi":
            vending.add_stock(pepushi, 5)
            print("補填が完了しました")
        elif goods == "monster":
            vending.add_stock(monster, 5)
            print("補填が完了しました")
        elif goods == "irohasu":
            vending.add_stock(irohasu, 5)
            print("補填が完了しました")


    elif command == "zaiko":
        goods = input("在庫を確認したい商品を指定してください。三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")

        if goods == "pepushi":
            print(f"在庫は{vending.get_stock_count(pepushi)}個です")
        elif goods == "monster":
            print(f"在庫は{vending.get_stock_count(monster)}個です")
        elif goods == "irohasu":
            print(f"在庫は{vending.get_stock_count(irohasu)}個です")

    
    elif command == "buy":

        goods = input("どの商品の在庫を購入するか選択してください。以下三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")

        if goods == "pepushi":
            mymoney = vending.buy(pepushi, suica.deposit())
            if mymoney != suica.deposit():
                uriage = 150
                suica.balance = mymoney
                total_sales += uriage
                print(f"ペプシの在庫は{vending.get_stock_count(pepushi)}個、残金は{mymoney}、売上{total_sales}円")
            elif vending.get_stock_count(pepushi) == 0:
                print("該当商品の在庫がありません")
            else:
                print("残金が足りないので購入できません")

        if goods == "monster":
            mymoney = vending.buy(monster, suica.deposit())
            if mymoney != suica.deposit():
                uriage = 230
                suica.balance = mymoney
                total_sales += uriage
                print(f"モンスターの在庫は{vending.get_stock_count(monster)}個、残金は{mymoney}、売上{total_sales}円")
            elif vending.get_stock_count(monster) == 0:
                print("該当商品の在庫がありません")
            else:
                print("残金が足りないので購入できません")

        if goods == "irohasu":
            mymoney = vending.buy(irohasu, suica.deposit())
            if mymoney != suica.deposit() :
                uriage = 200
                suica.balance = mymoney
                total_sales += uriage
                print(f"イロハスの在庫は{vending.get_stock_count(irohasu)}個、残金は{mymoney}、売上{total_sales}円")
            elif vending.get_stock_count(irohasu) == 0:
                print("該当商品の在庫がありません")
            else:
                print("残金が足りないので購入できません")


    elif command == "sales_amount":
        print(f"現在の自動販売機の売上額は{total_sales}円です")
        
    
    elif command in ["q", "Q", "exit", "quit"]:
        break

    
    
    









