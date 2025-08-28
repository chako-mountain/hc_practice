#  目的　6人を、3:3もしくは2:4にランダムに分ける
# 3:3か4:2どっちにするかをまず選ぶ
# 前者の場合、ランダムに三人を選び、それ以外の人間でそれぞれグループを作る
# 後者の場合、ランダムに二人を選び、それ以外の人間でグループを作る

import random

persons = ["A","B","C","D","E","F"]
zero_or_one = [0,1]

def divide_3_3 (list1,list2,list3,list4,list5,list6):
    l = [list1,list2,list3,list4,list5,list6]
    new_list_1 = random.sample(l,3)
    new_list_2 = list(set(l) - set(new_list_1))
    
    print(f"グループを3:3に分けました {new_list_1},{new_list_2}")


def divide_4_2 (list1,list2,list3,list4,list5,list6):
    l = [list1,list2,list3,list4,list5,list6]
    new_list_1 = random.sample(l,2)
    new_list_2 = list(set(l) - set(new_list_1))
    
    print(f"グループを2:4に分けました {new_list_1},{new_list_2}")

randomnum = random.choice(zero_or_one)
# print(randomnum)

if randomnum == 0:
    divide_4_2(*persons)
else:
    divide_3_3(*persons) 

# divide_4_2(*persons)