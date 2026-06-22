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
        self.eyes = "brown"

    def get_eyes(self):
        print("get_eyes getter method called")
        return self.eyes

    def set_eyes(self, value):
        print("set_eyes setter method called")
        self.eyes = value


king = King()
king2 = King2()
print(f"king.eyes: {king.eyes}")  # Önce getter a gidildi, oradan _eyes çekildi, eyes gibi gösterildi. 
#Aslında King içinde eyes diye bir attribute yok, _eyes var. Ama property sayesinde eyes gibi görünüyor.
print(f"king2.eyes: {king2.eyes}")  # Direkt eyes attribute çekildi
king.eyes = "blue"  # Önce " = "blue" sayesindesetter a gidildi, oradan _eyes değiştirildi.
#ama eyes i soranlara getter sayesinde yine _eyes gösterilecek
king2.eyes = "blue"  #  Direkt attribute değiştirildi
print(f"king.eyes: {king.eyes}")
print(f"king2.eyes: {king2.eyes}")


# !!!!!! Bu kod sonsuz döngü üretir !!!
# class King:
#     def __init__(self):
#         self.eyes = "brown"

#     @property
#     def eyes(self):
#         print("Getting eyes property")
#         return self.eyes

#     @eyes.setter
#     def eyes(self, value):
#         print("Setting eyes property")
#         self.eyes = value
