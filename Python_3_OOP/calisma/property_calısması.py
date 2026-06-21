class King:
    def __init__(self):
        self._eyes = "brown"

    @property  #"bir fonksiyonu değişken gibi kullanma arayüzü" sağlar
    def eyes(self):
        print("Getting eyes property")
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        print("Setting eyes property")
        self._eyes = value

   
class King2:
    def __init__(self):
        self._eyes = "brown"

    def get_eyes(self):
        print("get_eyes getter method called")
        return self._eyes

    def set_eyes(self, value):
        print("set_eyes setter method called")
        self._eyes = value


king = King()
king2 = King2()
print(f"king.eyes: {king.eyes}") # Önce getter a gidildi, oradan eyes çekildi
print(f"king2.eyes: {king2._eyes}") # Direkt attribute çekildi
king.eyes = "blue"  # Önce setter a gidildi, oradan eyes değiştirildi
king2._eyes = "blue" # Direkt attribute değiştirildi
print(f"king.eyes: {king.eyes}")
print(f"king2.eyes: {king2._eyes}")
