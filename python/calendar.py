
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
def get_length_of_manth(year,month):

    if month == 12:
        begin_date = datetime.date(year,month,1)
        end_date = datetime.date(year+1,1,1)
    else:

        begin_date = datetime.date(year,month,1)
        end_date = datetime.date(year,month+1,1)

    return (end_date - begin_date).days


# 年と月を代入して、その月の始まりの番号を取得
def get_first_day_of_month (year,month):
    return  datetime.date(year,month,1).weekday()


# 開始番号(=曜日)と、月の長さを書いてカレンダーを作成
def print_calendar (beginning_day, length, year ,month):

    print(f"      {month}月 {year}")
    print("月 火 水 木 金 土 日")

    # 改行の指標となるweek_dayを設定
    week_day = beginning_day

    # 開始地点まで空欄を作成
    print("   " * beginning_day, end="")

    # 数字を付きの長さの分だけ数字を出力
    for j in range(1,length + 1):

        # 日曜日（左端）を検出 
        if week_day == 6:

            print(str(j).rjust(2))  
            week_day = 0

        else:

            print(str(j).rjust(2) + " ",end = "")
            week_day += 1


# 三つの関数をまとめて、カレンダーを作る関数
def makecalendar(year, month):
    # 月の日数を取得
    length = get_length_of_manth(year,month)
    # 何曜日から始まるか取得
    beginning_day_day = get_first_day_of_month(year,month)     
    # 地図描画   
    print_calendar(beginning_day_day,length,year,month)

# オプションによってバリデーションをかける
value = sys.argv

# デフォルト処理を実行
today = datetime.date.today()
today_year = today.year
today_month = today.month
print("デフォルト処理を実行します")
makecalendar(today_year ,today_month)

if len(value) >= 2:
    if value[1] == "-m":
        if int(value[2]) == None or int(value[2]) == "" or int(value[2]) < 1 or int(value[2]) > 12:
            print("\noption error")
            print(f"{value[2]} is neither a month number (1 .. 12) nor a name")
        elif 1 <= int(value[2]) <= 12:
            print("\n正しいオプションが指定されました\n")
            month = value[2]
            makecalendar(int(2025) ,int(month))
