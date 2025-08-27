
# 2022年、2月の初めの曜日を取得
# 2022年、2月が何日あるか取得
# 2022年、2月の初めの曜日だけ、スペースで間を空ける
# for文で、とりあえず2月分のループを回す
# 初めの曜日のを格納する変数に1足していき、6になったらリセット
# リセットとともに改行するようにする

import datetime
import sys

hennsuu = 0

# 指定した月の長さを取得
# カレンダーモジュールが使用できないので、ゴリ押しで取得
def get_length_of_manth(year,month):

    for i in range (28,33):

        try:
            a = datetime.date(year,month,i).weekday()
            if 0<= a <= 6:
                # print("OK")
                pass
        except:
            print("NG")
            day = i-1
            # print(str(hennsuu))
            break
    
    return day


# 年と月を代入して、その月の始まりの番号を取得
def get_first_number_of_month (year,month):
    return  datetime.date(year,month,1).weekday()


# 開始番号(=曜日)と、月の長さを書いてカレンダーを作成
def calendar (beginning, length, year ,month):

    print("      " + str(month) +"月" + str(year))

    print("月" + " " + "火" + " " + "水" + " " + "木"
          + " " + "金" + " " + "土"  + " " + "日")

    # 改行の指標となるweek_numberを設定
    week_number = beginning

    # 開始地点まで空欄を作成
    for i in range(0,beginning):
        print("   " , end = "")

    # 数字を付きの長さの分だけ数字を出力
    for j in range(1,length + 1):

        # 日曜日（左端）を検出 
        if week_number == 6:

            # 一桁なら、数字出力の前に半角スペース
            if j < 10:
                print(" ", end = "")

            # 日を記入し、week_numberリセット
            print(str(j))
            week_number = 0

        else:

            # 一桁なら、半角スペース
            if j < 10:
                print(" ", end= "")
            
            # スペースを開けて数字を書く。week_numも更新
            print(str(j) + " " , end = "")
            week_number += 1


# 三つの関数をまとめて、カレンダーを作る関数
def makecalendar(year, month):
    # 月の日数を取得
    length = get_length_of_manth(year,month)
    # 何曜日から始まるか取得
    beginning = get_first_number_of_month(year,month)     
    # 地図描画   
    calendar(beginning,length,year,month)




# オプションによってバリデーションをかける
value = sys.argv

if len(value) == 1:
    print("デフォルト処理を実行します")
    makecalendar(2022 ,2)

elif len(value) == 3 and value[1] == "-m":
    if 1 <= int(value[2]) <= 12:
        print("正しいオプションです")
        month = value[2]
        makecalendar(int(2025) ,int(month))
    else:
        print("-m のオプションとして、1から12の整数をタイプしてください")

elif len(value) and value[1] == "-m":
    print("コマンドを正しく打ってください。-m の次には1から12の整数を打ち込んでください")

else:
    print("不正なコマンドです。")
