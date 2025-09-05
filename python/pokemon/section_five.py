

# abstract class Pokemon {
#     abstract val name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()
# }

# Pythonで抽象クラスを定義

from abc import ABC, abstractmethod

class Pokemon(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def type1(self):
        pass

    @property
    @abstractmethod
    def type2(self):
        pass

    @property
    @abstractmethod
    def hp(self):
        pass

    @property
    @abstractmethod
    def attack(self):
        pass


# class Pikachu(
#     override val name: String,
#     override val type1: String,
#     override val type2: String,
#     override val hp: Int
# ) : Pokemon() {

#     override fun attack() {
#         println("$name の10万ボルト!")
#     }
# }

class Pikachu(Pokemon):
    def __init__(self,name,type1,type2,hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @property
    @abstractmethod
    def name(self):
        return self._name
    
    @property
    @abstractmethod
    def type1(self):
        return self._type1
    
    @property
    @abstractmethod
    def type2(self):
        return self._type2
    
    @property
    @abstractmethod
    def hp(self):
        return self._hp

    @property
    @abstractmethod
    def attack(self):
        print(f"{self.name} の10万ボルト!")


# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)

#     println(pika.attack()) // ピカチュウ の10万ボルト!
# }

pika = Pikachu("ピカチュウ","でんき","",100)
print(pika.attack())


# abstract class Pokemon
#     abstract val name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int

#     open fun attack() {
#         println("$name のこうげき！")
#     }
# }

# class Pikachu(
#     override val name: String,
#     override val type1: String,
#     override val type2: String,
#     override val hp: Int
# ) : Pokemon() {

#     override fun attack() {
#         super.attack()
#         println("$name の10万ボルト!")
#     }
# }

# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)

#     // ピカチュウ のこうげき！
#     // ピカチュウ の10万ボルト! が順番に表示される
#     println(pika.attack())
# }

from abc import ABC, abstractmethod

class Pokemon(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def type1(self):
        pass

    @property
    @abstractmethod
    def type2(self):
        pass

    @property
    @abstractmethod
    def hp(self):
        pass

    def attack(self):
        print(f"{self.name} のこうげき！")

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    def name(self):
        return self._name

    def type1(self):
        return self._type1

    def type2(self):
        return self._type2

    def hp(self):
        return self._hp

    def attack(self):
        super().attack()
        print(f"{self.name} の10万ボルト!")

pika = Pikachu("ピカチュウ", "でんき", "", 100)
pika.attack()






# class Pikachu(
#     val namae: String,     // 名前。 本来は `name` を使いたい
#     val taipu1: String,    // タイプ1。 本来は `type1` を使いたい 
#     val taipu2: String,    // タイプ2。 本来は `type2` を使いたい
#     val hitpoint: Int      // HP。 本来は `hp` を使いたい
# ): Pokemon(namae, taipu1, taipu2, hitpoint) {
#     // kougeki() じゃなくて attack() を使いたい
#     fun kougeki() { ... }
# }


# interface Pokemon {
#     val name: String
#     val type1: String
#     val type2: String
#     val hp: Int

#     fun attack()
# }

# abstract class Test {
#     val value = 100    // 値を入れられる
    
#     fun greet() { print("Hello!") }
# }

# インターフェース
# interface Test {
#     val value: Int    // 値を入れられない
    
#     fun greet() { print("Hello!") }  // メソッドは実装可能
# }

# 1つの子クラスに複数継承させる(多重継承)
# 抽象クラス
# abstract class ParentA
# abstract class ParentB

# class Child: ParentA()         // 多重継承NG

# インターフェース
# interface ParentA
# interface ParentB

# class Child: ParentA, ParentB // 多重継承OK

