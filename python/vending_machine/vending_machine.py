from vending_class import Suica, Juice ,VendingMachine

suica = Suica()

vending = VendingMachine()

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
        for name, count in vending.get_all_stock():
            print(f"{name}の在庫は{count}個です")


    elif command == "zaiko_charge":
        vending.add_stock(Juice("pepushi", 150), 5)
        vending.add_stock(Juice("monster", 230), 5)
        vending.add_stock(Juice("irohasu", 120), 5)


    elif command == "buy":
        goods = input("どの商品の在庫を購入するか選択してください。以下三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")
        try:
            if goods == "pepushi":
                vending.buy(Juice("pepushi", 150), suica)
                total_sales += 150
                print(f"ペプシの在庫は{vending.get_stock_count(Juice('pepushi', 150))}個、残金は{suica.deposit()}円、売上{total_sales}円")
            elif goods == "monster":
                vending.buy(Juice("monster", 230), suica)
                total_sales += 230
                print(f"モンスターの在庫は{vending.get_stock_count(Juice('monster', 230))}個、残金は{suica.deposit()}円、売上{total_sales}円")
            elif goods == "irohasu":
                vending.buy(Juice("irohasu", 120), suica)
                total_sales += 120
                print(f"イロハスの在庫は{vending.get_stock_count(Juice('irohasu', 120))}個、残金は{suica.deposit()}円、売上{total_sales}円")
            else:
                print("指定された商品は存在しません")
        except ValueError as e:
            print(e)


    elif command == "sales_amount":
        print(f"現在の自動販売機の売上額は{total_sales}円です")

    
    elif command in ["q", "Q", "exit", "quit"]:
        break