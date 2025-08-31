from vending_class import Suica, Juice, Buy

suica = Suica()

p = Juice("pepushi",150)
pepushis = [p,p,p,p,p]

m = Juice("monster",230)
monsters = [m,m,m,m,m]

i = Juice("irohasu",120)
irohasus = [i,i,i,i,i]

total_sales = 0

zankin = suica.Deposit()

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
        print(str(f"現在の残高は、{suica.Deposit()}円です"))

    elif command == "charge":
        charge_amount = int(input("100円以上のチャージ金額を指定してください"))
        if charge_amount >= 100:
            suica.Charge(charge_amount)
            zankin = suica.Deposit()
            print(f"{charge_amount}円チャージされ、残金{zankin}円です")
            
        else:
            print("正しいフォーマットで入力してください")

    elif command == "zaiko":
        goods = input("在庫を確認したい商品を指定してください。三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")

        if goods == "pepushi":
            print(f"在庫は{len(pepushis)}個です")
        elif goods == "monster":
            print(f"在庫は{len(monsters)}個です")
        elif goods == "irohasu":
            print(f"在庫は{len(irohasus)}個です")

    elif command == "zaiko_charge":

        goods = input("どの商品の在庫を補填するか選択してください。以下三種類ございます"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")
        
        if goods == "pepushi":
            pepushis = [p,p,p,p,p]
            print("補填が完了しました")
        elif goods == "monster":
            monsters = [m,m,m,m,m]
            print("補填が完了しました")
        elif goods == "irohasu":
            irohasus = [i,i,i,i,i]
            print("補填が完了しました")

    
    elif command == "buy":

        goods = input("どの商品の在庫を購入するか選択してください。以下三種類ございます\n"
                      "pepushi\n"
                      "monster\n"
                      "irohasu\n")

        if goods == "pepushi":
            buy_pepushi = Buy()

            if buy_pepushi.canbuy(pepushis,len(pepushis),p.price,suica.now_money):
               stock,mymoney,uriage = buy_pepushi.buying(pepushis,len(pepushis)-1,p.price,suica.now_money)

            #    zankin = mymoney

               suica.now_money = mymoney
               total_sales += uriage

               print(f"ペプシの在庫は{len(pepushis)}個、残金は{mymoney}、売上{total_sales}円")
            else:
                print("該当商品の在庫または残金が足りないので、購入できません")

        elif goods == "monster":

            buy_monster = Buy()

            if buy_monster.canbuy(monsters,len(monsters),m.price,suica.now_money):
                stock,mymoney,uriage = buy_monster.buying(monsters,len(monsters)-1,m.price,suica.now_money)

                suica.now_money = mymoney
                total_sales += uriage

                print(f"モンスターの在庫は{len(monsters)}個、残金は{mymoney}、売上{total_sales}円")
            else:
                print("該当商品の在庫または残金が足りないので、購入できません")

        
        elif goods == "irohasu":

            buy_irohasu = Buy()

            if buy_irohasu.canbuy(irohasus,len(irohasus),m.price,suica.now_money):
                stock,mymoney,uriage = buy_irohasu.buying(irohasus,len(irohasus)-1,m.price,suica.now_money)

                suica.now_money = mymoney
                total_sales += uriage

                print(f"イロハスの在庫は{len(irohasus)}個、残金は{mymoney}、売上{total_sales}円")
            else:
                print("該当商品の在庫または残金が足りないので、購入できません")
        
    elif command == "sales_amount":
        print(f"現在の自動販売機の売上額は{total_sales}円です")
    
    # elif command == "zaiko":
    #     goods = input("どの商品の在庫を確認しますか")

    #     if goods == "pepushi":
    #         print(len(pepushis))

    elif command in ["q", "Q", "exit", "quit"]:
        break

    
    
    









