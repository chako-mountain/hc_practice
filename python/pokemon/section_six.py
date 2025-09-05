

# abstract class Pokemon {
#     abstract var name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()
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

    @property
    @abstractmethod
    def attack(self):
        






# abstract class Pokemon {
#     abstract var name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()

#     fun changeName(newName: String) {
#         // 不適切な名前はエラー
#         if(name == "うんこ") {
#             print("不適切な名前です")
#             return
#         }
#         this.name = newName
#     }
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

    @property
    @abstractmethod
    def attack(self):

    def change_name(self, new_name: str):
        if self.name == "うんこ":
            print("不適切な名前です")
            return  self.name = new_name
        
       





# abstract class Pokemon {
#     private var name: String = ""
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()

#     fun changeName(newName: String) {
#         // 不適切な名前はエラー
#         if(name == "うんこ") {
#             print("不適切な名前です")
#             return
#         }
#         this.name = newName
#     }
    
#     fun getName(): String {
#         return this.name
#     }
# }

from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self):
        self._name

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

    @property
    def name(self):
        return self.name
    
    def changeName(self,new_name):

        if self.name == "うんこ":
            print("不適切な名前です")
            return
        self.name = new_name

    def get_name(self):
        return self.name

    




# class Pikachu(
#     override val type1: String,
#     override val type2: String,
#     override val hp: Int
# ) : Pokemon() {

#     override fun attack() {
#         println("${super.getName()} の10万ボルト!")
#     }
# }

class Pikachu(Pokemon):
    def __init__(self, type1: str, type2: str, hp: int):
        super().__init__()
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    @property
    def type1(self) -> str:
        return self._type1

    @property
    def type2(self) -> str:
        return self._type2

    @property
    def hp(self) -> int:
        return self._hp

    def attack(self):
        print(f"{super().get_name()} の10万ボルト!")



# pokemon.changeName("テキセツ")
# pokemon.getName()     // テキセツ

# pokemon.changeName("うんこ")   // 「不適切な名前です」と表示される
# pokemon.getName()     // テキセツ のまま


pokemon.changeName("テキセツ")
pokemon.getName()    

pokemon.changeName("うんこ")  
pokemon.getName()    


# interface NameService {
#     fun changeName(newName: String)
#     fun getName(): String
# }

from abc import ABC, abstractmethod

class NameService(ABC):
    @abstractmethod
    def change_name(self,new_name):
        pass

    @abstractmethod
    def get_name(self):
        pass






# abstract class Pokemon: NameService {
#     private var name: String = ""
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()

#     override fun changeName(newName: String) {
#         // 不適切な名前はエラー
#         if(name == "うんこ") {
#             print("不適切な名前です")
#             return
#         }
#         this.name = newName
#     }
    
#     override fun getName(): String {
#         return this.name
#     }
# }



from abc import ABC, abstractmethod

class NameService(ABC):
    @abstractmethod
    def change_name(self, new_name):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Pokemon(NameService):
    def __init__(self):
        self.name = ""

    @property
    @abstractmethod
    def type1(self) -> str:
        pass

    @property
    @abstractmethod
    def type2(self) -> str:
        pass

    @property
    @abstractmethod
    def hp(self) -> int:
        pass

    @abstractmethod
    def attack(self):
        pass

    def change_name(self, new_name):
        if self.name == "うんこ":
            print("不適切な名前です")
            return self.name = new_name

    
    def get_name(self):
        return self.name