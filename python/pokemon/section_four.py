
# アンチパターンはPythonで書いていません
# class Pokemon
#     val name: String,
#     val type1: String,
#     val type2: String,
#     val hp: Int
# ){
#     fun attack() {
#         println("$name のこうげき!")
#     }
    
#     // ピカチュウの攻撃
#     fun thunderboltAttack() { 
#         println("$name の10万ボルト!")
#     }
    
#     // ゼニガメの攻撃
#     fun watergunAttack() {
#         println("$name のみずでっぽう!") }
#     }
# }


# if(poke.name == "ピカチュウ") {
#     poke.thunderboltAttack()
# }
# else if(poke.name == "ゼニガメ") {
#     poke.watergunAttack()
# }
# ...


# class Pikachu: Pokemon()
#  継承の使い方

class Pikachu(Pokemon):


# Pythonでopenは不必要
# open class Pokemon(...)


# class Pikachu(
#     _name: String,
#     _type1: String,
#     _type2: String,
#     _hp: Int
# ): Pokemon(_name, _type1, _type2, _hp)

class Pikachu(Pokemon):
    def __init__(self,name,type1,type2,hp):
        super().__init__(name,type1,type2,hp)




# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)
    
#     println(pika.name)     // ピカチュウ
#     println(pika.attack()) // ピカチュウ のこうげき! 
# }


pika = Pikachu("ピカチュウ","でんき","",100)

print(pika.name)
print(pika.attack())



# class Pikachu(
#     _name: String,
#     _type1: String,
#     _type2: String,
#     _hp: Int
# ): Pokemon(_name, _type1, _type2, _hp) {

#     override fun attack() {
#         println("$name の10万ボルト!")
#     }
# }

class Pikachu(Pokemon):
    def __init__(self,name,type1,type2,hp):
        super().__init__(name,type1,type2,hp)

    def attack(self):
        print(f"{self.name}の10まんボルト!")



# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)
    
#     println(pika.attack()) // ピカチュウ の10万ボルト! 
# }

pika = Pikachu("ピカチュウ", "でんき", "", 100)
print(pika.attack())




# Pythonにてopenは必要ない
# open class Pokemon(...) {
#     open fun attack() {
#         ...
#     }
# }



# class Pikachu(
#     _name: String,
#     _type1: String,
#     _type2: String,
#     _hp: Int
# ): Pokemon(_name, _type1, _type2, _hp) {

#     override fun attack() {
#         super.attack()    // 親クラスのメソッド呼び出し
#         println("$name の10万ボルト!")
#     }
# }

class Pikachu(Pokemon):
    def __init__(self,name,type1,type2,hp):
        super().__init__(name,type1,type2,hp)


    def attack(self):
        super().attack()
        print(f"{self.name}の10まんボルト!")



# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)
    
#     // ピカチュウ のこうげき！
#     // ピカチュウ の10万ボルト! が順番に表示される
#     println(pika.attack()) 
# }

pika = Pikachu("ピカチュウ", "でんき", "", 100)
print(pika.attack())




