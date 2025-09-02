
# # 既定打数と実際の打数のリストを入力してもらう
# kitei = list[input("既定打数を入力してください")]
# dasuu = list[input("実際の打数を入力してください")]
# print(kitei)
# print(dasuu)
# 初期化

row1 = []
row2 = []

score = []

# ファイルを読み取りモードで開く
with open('case1.txt', 'r') as f:
    lines = f.readlines()  # 全行をリストで取得


    row1 = lines[0].strip().split(',') 
    row2 = lines[1].strip().split(',') 

    
print("row1:", row1)
print("row2:", row2)


def hantei (kitei_row, dasuu_row):

    result = None  

    kitei = int(kitei_row)
    dasuu = int(dasuu_row)

    if kitei == dasuu:
        result  = "パー"
    
    elif kitei < dasuu:
        if dasuu == kitei + 1:
            result = "ボギー"
        elif dasuu == kitei + 2:
            result = "2ボギー"
        elif dasuu == kitei + 3:
            result = "3ボギー"
        elif dasuu == kitei + 4:
            result = "4ボギー"

    elif kitei > dasuu:
        if dasuu == kitei - 1:
            result =  "バーディ"
        elif dasuu == kitei - 2 and dasuu ==1:
            result = "ホールインワン"
        elif dasuu == kitei - 2 :
            result = "イーグル"
        elif kitei == 5 and dasuu == kitei - 3:
            result = "アルバトロス"
        elif kitei == 5 and dasuu == 1:
            result = "コンドル"
        elif dasuu == 1:
            result = "ホールインワン"

    return result
        

# print(len(row1))

for i in range(0,len(row1)):
    kekka = hantei(row1[i],row2[i])
    score.append(kekka)

    print(str(row1[i]),str(row2[i]),kekka)

# print(str(score))