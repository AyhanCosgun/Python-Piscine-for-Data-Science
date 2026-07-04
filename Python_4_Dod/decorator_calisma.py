from typing import Any


def decorator_factory(limit: int):  # Bu bir dekoratör fabrikasıdır ve limit 
     #parametresi alıp bu ayarla bir dekoratör döndürür.
    count = 0

    def decorator(function):  # Bu decorator, @decorator_factory(limit) satırının
    #hemen altındaki dekore edilecek olan orjinal fonksiyonu 
    # Python'un decorator mekanizması sayesinde argüman olarak alır
    #ve onu saracak olan bir wrapper fonksiyonu döndürür.
    
        def wrapper(*args: Any, **kwds: Any):  # Bu wrapper artık orijinal fonksiyonun yerine çağrılan fonksiyondur.
        #görevi # *args ve **kwds, çağrı sırasında, sanki orjinal fonksiyona veriliyormuş gibi verilen tüm argümanları yakalar.
        # buna göre orjinal fonksiyonun davranışını değiştirir, dönüştürür.
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None
        return wrapper
    return decorator




# def iptal_et(function):
#     def wrapper(*args, **kwargs):
#         print("Bu fonksiyon iptal edildi.")
#         return None
#     return wrapper


# @iptal_et
# def selam():
#     print("Merhaba")
    
# selam()  # Output: Bu fonksiyon iptal edildi.


def ayar_katmanı_factory(msg: str):
    def iptal_et(function):
        def wrapper(*args, **kwargs):
            print(msg)
            return None
        return wrapper
    return iptal_et


@ayar_katmanı_factory("Bu fonksiyon msg ile iptal edildi.")
def selam():
    print("Merhaba")


selam()


def aynen_birak(function):  #sadece decorator, wrapper yok
    # wrapper : Bir fonksiyon/class alır ve yerine kullanılacak bir şey döndürür.
    #Decorator sadece fonksiyon tanımlanırken bir şey yapacaksa ve çağrılarda araya girmeyecekse wrapper gerekmez.
    #Çağrı anında araya gireceksen wrapper gerekir.
    #Tanım anında bir şey yapıp fonksiyonu aynen bırakacaksan wrapper gerekmez.
    return function


@aynen_birak
def merhaba(msg):
    print(msg)


merhaba("Merhaba")  # Output: Merhaba