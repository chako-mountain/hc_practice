#  目的　6人を、3:3もしくは2:4にランダムに分ける
# 3:3か4:2どっちにするかをまず選ぶ
# 前者の場合、ランダムに三人を選び、それ以外の人間でそれぞれグループを作る
# 後者の場合、ランダムに二人を選び、それ以外の人間でグループを作る

import random

persons = ["A","B","C","D","E","F"]
zero_or_one = [0,1]

# 分割関数を一つにまとめた。

def devide(person_list, how_to_devide):


    def divide_3_3(person_list):
        new_list_1 = random.sample(person_list, 3)
        new_list_2 = list(set(person_list) - set(new_list_1))
        print(f"グループを3:3に分けました {new_list_1},{new_list_2}")


    def divide_4_2(person_list):
        new_list_1 = random.sample(person_list, 2)
        new_list_2 = list(set(person_list) - set(new_list_1))
        print(f"グループを2:4に分けました {new_list_1},{new_list_2}")


    # 引数に基づいて分ける
    if how_to_devide == "3:3":
        divide_3_3(person_list)
    elif how_to_devide == "2:4":
        divide_4_2(person_list)


randomnum = random.choice(zero_or_one)

if randomnum == 0:
    devide(persons, "2:4")
else:
    devide(persons, "3:3")

# devide(persons, "3:3")