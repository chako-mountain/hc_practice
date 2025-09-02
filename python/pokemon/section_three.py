# コメントアウトしている部分がコトリンのコード、コメントアウトしていない部分がPythonのコードです。

# class Pokemon {
#     val name = “リザードン”
#     val type1 = “ほのお”
#     val type2 = “ひこう”
#     val hp = 100
    
#     fun attack() {
#         println("$name のこうげき！")
#     }
# }


class Pokemon:
    name = "リザードン"
    type1 = "ほのお"
    type2 = "ひこう"
    hp = 100
    
    @staticmethod
    def attack():
        print(f"{Pokemon.name}のこうげき!")

def main():

    poke = Pokemon()

    print(poke.mp)




# val name = "リザードン"

name = "リザードン"



# class Pokemon {
#     val name: String
    
#     constructor(_name: String) {
#         name = _name
#     }
# }


class Pokemon:

    def __init__(self,name):

        self.name = name


class Pokemon:

    
# val poke = Pokemon("ピカチュウ")
# print(poke.name)    // ピカチュウ

    poke = Pokemon("ピカチュウ")
    print(poke.name)


# class Pokemon constructor(_name: String) {
#     val name: String = _name
# }

class Pokemon:

    def __init__(self,name):

        self.name = name




# class Pokemon(
#     val name: String
#     val type1: String
#     val type2: String
#     val hp: Int
# ) {
#     fun attack() {
#         println("$name のこうげき！")
#     }
# }

class Pokemon:

    def __init__(self,name,type1,type2,hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attafk(self):
        print(f"{self.name}のこうげき!")




# class Pokemon constructor(_name: String, _type: String) {
#     val exText = "$_name は $_type タイプのポケモン。"
# }

class Pokemon:

    def __init__(self,name,type):
        self.ex_text = f"{name}は{type}タイプのポケモン"



# ↓メソッド開始
# fun localFunction() {
#     val poke = Pokemon()    // インスタンス生成
#     ...
# }

    def localFunction():
        poke = Pokemon()