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
        juice_names = vending.get_canbuy_juice_name()
        print("購入可能な商品は以下の通りです")
        print(", ".join(juice_names))

        wants = input("どの商品を購入しますか？商品名を入力してください: ")

        if wants not in juice_names:
            print("指定された商品は存在しません")
            continue

        try:
            juice = vending.buy(wants, suica)
            total_sales += juice.price
            print(f"{juice.name}を購入しました。{juice.name}の在庫は{vending.get_stock_count(juice)}個、残金は{suica.deposit()}円です。")
        except ValueError as e:
            print(e)


    elif command == "sales_amount":
        print(f"現在の自動販売機の売上額は{total_sales}円です")

    
    elif command in ["q", "Q", "exit", "quit"]:
        break