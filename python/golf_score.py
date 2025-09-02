
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


def hantei (par_row, score_row):

    SCORE_MAPPING = {
    -4 : "コンドル",
    -3 : "アルバトロス",
    -2 : "イーグル",
    -1 : "バーディ",
    0 : "パー",
    1 : "ボギー",
    2 : "2ボギー",
    3 : "3ボギー",
    4 : "4ボギー"
    }

    result = None  
    par = int(par_row)
    score = int(score_row)
    difference = score - par

    if par <= score:
        if score == 1:
            result = "ホールインワン"
        else:
            result = SCORE_MAPPING[difference]
    elif par > score:
        if difference == -4 and par == 5:
            result = "コンドル"
        elif score == 1:
            result = "ホールインワン"
        else:
            result = SCORE_MAPPING[difference]

    return result


for i in range(0,len(row1)):
    kekka = hantei(row1[i], row2[i])
    print(f"ホール {i+1}: par={row1[i]}, score={row2[i]} → {kekka}")