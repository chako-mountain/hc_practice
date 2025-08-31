#  目的　6人を、3:3もしくは2:4にランダムに分ける
# 3:3か4:2どっちにするかをまず選ぶ
# 前者の場合、ランダムに三人を選び、それ以外の人間でそれぞれグループを作る
# 後者の場合、ランダムに二人を選び、それ以外の人間でグループを作る

import random
persons = ["A","B","C","D","E","F"]
zero_or_one = [0,1]

# 分割関数を一つにまとめた。
def divide_groups(person_list, how_to_devide):
    group1 = random.sample(person_list, how_to_devide)
    group2 = list(set(person_list) - set(group1))
    print(f"グループを{how_to_devide} : {len(person_list)-how_to_devide}に分けました {group1},{group2}")

randomnum = random.choice(zero_or_one)
if randomnum == 0:
    divide_groups(persons, 3)
else:
    divide_groups(persons, 2)