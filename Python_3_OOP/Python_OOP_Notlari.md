# Python'da OOP Notlari

Bu notlar C++'ta OOP kavramlarini bilen ama Python'daki karsiliklarini yeni
ogrenen biri icin yazildi. Amaç sadece syntax gostermek degil; Python'in OOP
felsefesini, C++ ile nerede benzedigini, nerede ayrildigini ve 42 subjectindeki
egzersizlerde hangi ozelliklerin kullanildigini netlestirmek.

## 1. Python'da Her Sey Nesnedir

Python'da integer, string, list, function, class, module gibi neredeyse her sey
nesnedir.

```python
print(type(42))          # <class 'int'>
print(type("Ned"))       # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
print(type(len))         # <class 'builtin_function_or_method'>
```

C++'ta primitive tipler ve object tipler ayrimi daha belirgindir. Python'da ise:

```python
x = 42
print(x.__class__)       # <class 'int'>
print(x.bit_length())    # 6
```

Yani `int` bile metodlari olan bir nesnedir.

## 2. Class Tanimi

C++:

```cpp
class Stark {
public:
    std::string first_name;

    Stark(std::string name) : first_name(name) {}
};
```

Python:

```python
class Stark:
    """Representing a Stark character."""

    def __init__(self, first_name):
        """Initialize a Stark character."""
        self.first_name = first_name
```

Temel farklar:

- Python'da class govdesi indentation ile belirlenir.
- Constructor adi `__init__` metodudur.
- Instance uzerindeki verilere `self` ile erisilir.
- `self` C++'taki `this` pointer'ina benzer ama metot parametresinde acikca
  yazilir.
- Python'da attribute'lar genellikle constructor icinde dinamik olarak olusturulur.

Kullanim:

```python
ned = Stark("Ned")
print(ned.first_name)    # Ned
```

## 3. `self` Nedir?

Python'da instance metodunun ilk parametresi geleneksel olarak `self` adini alir.
Bu zorunlu bir keyword degildir ama standart budur.

```python
class Character:
    def say_name(self):
        print(self.first_name)
```

Aslinda su cagri:

```python
ned.say_name()
```

Python tarafindan buna benzer sekilde calisir:

```python
Character.say_name(ned)
```

Bu yuzden instance metodlarinda ilk parametre olarak `self` gerekir.

## 4. Instance Attribute ve Class Attribute

Python'da iki yaygin attribute turu vardir.

### Instance Attribute

Her nesneye ozel degerdir.

```python
class Character:
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True

ned = Character("Ned")
arya = Character("Arya")

ned.is_alive = False

print(ned.is_alive)      # False
print(arya.is_alive)     # True
```

### Class Attribute

Sinifin kendisine aittir, tum instance'lar tarafindan paylasilir.

```python
class Baratheon:
    family_name = "Baratheon"

robert = Baratheon()
stannis = Baratheon()

print(robert.family_name)    # Baratheon
print(stannis.family_name)   # Baratheon
```

Dikkat: mutable class attribute kullanirken cok dikkatli olun.

```python
class BadExample:
    items = []

a = BadExample()
b = BadExample()

a.items.append("surprise")
print(b.items)          # ['surprise']
```

Bu iki nesnenin ayni listeyi paylastigi anlamina gelir. Genelde boyle durumlarda
listeyi `__init__` icinde olusturmak daha dogrudur.

```python
class GoodExample:
    def __init__(self):
        self.items = []
```

## 5. Constructor: `__init__`

Python'da constructor gibi dusundugumuz metod `__init__` metodudur.

```python
class Character:
    """Base character class."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a character."""
        self.first_name = first_name
        self.is_alive = is_alive
```

C++'taki constructor ile benzer amaca hizmet eder ama teknik olarak nesneyi
yaratan metod degildir. Nesne once `__new__` ile olusturulur, sonra `__init__`
ile initialize edilir.

Cogunlukla `__new__` yazmazsiniz. `__init__` yeterlidir.

## 6. Destructor Var mi?

C++'ta destructor cok onemlidir:

```cpp
~Character();
```

Python'da `__del__` adinda bir metod vardir ama C++ destructor mantigiyla
dusunmek genellikle yanlistir.

```python
class Character:
    def __del__(self):
        print("object destroyed")
```

Neden dikkatli olmak gerekir?

- Python garbage collector kullanir.
- Nesnenin ne zaman yok edilecegi C++ kadar deterministik degildir.
- Dosya, socket, lock gibi kaynaklar icin `__del__` yerine context manager
  kullanilir.

Dogru kaynak yonetimi:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Bu C++'taki RAII kadar dilin merkezinde degildir ama `with` + context manager
Python'daki guvenli yoldur.

## 7. Public, Protected, Private

C++:

```cpp
class Character {
public:
    std::string first_name;

protected:
    int health;

private:
    std::string secret;
};
```

Python'da C++ gibi zorlayici access modifier yoktur. Bunun yerine naming
convention vardir.

### Public

Normal attribute veya method.

```python
self.first_name = "Ned"
```

Disaridan erisilebilir:

```python
print(ned.first_name)
```

### Protected Convention: `_name`

Tek underscore "bu internal/protected gibi dusunulsun" anlamina gelir.
Zorlayici degildir.

```python
class Character:
    def __init__(self):
        self._health = 100
```

Disaridan hala erisilebilir:

```python
print(obj._health)
```

Ama Python kulturunde bu "dokunma, implementation detail" demektir.

### Private Name Mangling: `__name`

Cift underscore name mangling yapar.

```python
class Character:
    def __init__(self):
        self.__secret = "winter"
```

Dogrudan erisim:

```python
obj.__secret           # AttributeError
```

Ama tamamen gizli degildir:

```python
obj._Character__secret
```

Yani Python'da private, C++'taki kadar sert bir guvenlik duvari degildir.
Python felsefesi daha cok "consenting adults" diye anilir: kod yazan kisinin
convention'lara uymasi beklenir.

## 8. Method Turleri

Python'da class icinde uc yaygin method turu vardir.

### Instance Method

Ilk parametresi `self` olur ve nesne state'ine erisir.

```python
class Character:
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True

    def die(self):
        self.is_alive = False
```

Kullanim:

```python
ned = Character("Ned")
ned.die()
```

### Class Method

Ilk parametresi `cls` olur ve sinifin kendisine erisir. `@classmethod` decorator'u
ile tanimlanir.

```python
class Lannister:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
```

Kullanim:

```python
cersei = Lannister.create_lannister("Cersei")
```

C++'taki static factory method'a benzer ama farki sudur: `cls` hangi class
uzerinden cagrildiysa onu temsil eder. Inheritance ile daha esnektir.

### Static Method

Instance veya class state'ine ihtiyac duymaz. `@staticmethod` ile tanimlanir.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

Kullanim:

```python
print(Calculator.add(3, 4))
```

C++'taki `static` member function'a en yakin karsilik budur.

## 9. Inheritance

Python'da inheritance syntax'i:

```python
class Character:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False


class Stark(Character):
    pass
```

Kullanim:

```python
ned = Stark("Ned")
print(ned.first_name)   # Ned
ned.die()
print(ned.is_alive)     # False
```

C++:

```cpp
class Stark : public Character {};
```

Python'da inheritance varsayilan olarak public inheritance gibi dusunulebilir.
Ancak C++'taki public/protected/private inheritance ayrimi yoktur.

## 10. `super()`

Base class constructor veya method cagirmak icin kullanilir.

```python
class Character:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
```

C++'taki base constructor cagrisina benzer:

```cpp
Baratheon(std::string name) : Character(name) {}
```

Python'da `super()` ozellikle multiple inheritance ile birlikte onemlidir.

## 11. Multiple Inheritance

Python multiple inheritance destekler.

```python
class Baratheon:
    def family(self):
        return "Baratheon"


class Lannister:
    def motto(self):
        return "Hear Me Roar"


class King(Baratheon, Lannister):
    pass
```

Kullanim:

```python
joffrey = King()
print(joffrey.family())
print(joffrey.motto())
```

C++ multiple inheritance destekler. Python da destekler ama method resolution
order kurali farklidir.

## 12. MRO: Method Resolution Order

Bir method veya attribute arandiginda Python belirli bir sirayla class'lara bakar.
Bu siraya MRO denir.

```python
class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B"


class C(A):
    def who(self):
        return "C"


class D(B, C):
    pass


print(D.mro())
print(D().who())        # B
```

Python 2.3'ten beri C3 linearization kullanir. 42 subjectindeki `DiamondTrap.py`
egzersizinde bahsedilen "diamond inheritance" problemi bununla ilgilidir.

MRO ornegi:

```python
[
    <class '__main__.D'>,
    <class '__main__.B'>,
    <class '__main__.C'>,
    <class '__main__.A'>,
    <class 'object'>
]
```

`class King(Baratheon, Lannister)` yazarsan Python once `King`, sonra
`Baratheon`, sonra `Lannister`, sonra onlarin base class'larina bakar.

## 13. Abstract Class

C++:

```cpp
class Character {
public:
    virtual void die() = 0;
};
```

Python'da abstract class icin `abc` modulu kullanilir.

```python
from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a character."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change alive state to False."""
        self.is_alive = False
```

Bu haliyle `Character` instantiate edilemez:

```python
character = Character("Hodor")   # TypeError
```

Subclass abstract method'u implement etmek zorundadir.

```python
class Stark(Character):
    """Representing the Stark family."""

    def die(self):
        """Change alive state to False."""
        super().die()
```

Not: Python'da abstract method govdesi olabilir. Subclass isterse `super()` ile
onu cagirabilir. Bu C++'taki pure virtual function'dan biraz daha esnektir.

## 14. Polymorphism

C++'ta polymorphism genellikle inheritance + virtual function uzerinden anlatilir.
Python'da polymorphism daha cok "duck typing" ile dogal olarak ortaya cikar.

```python
class Stark:
    def die(self):
        print("Stark died")


class Lannister:
    def die(self):
        print("Lannister died")


def kill(character):
    character.die()


kill(Stark())
kill(Lannister())
```

`kill` fonksiyonu objenin tam tipini umursamaz. `die` metodu varsa yeter.

Python felsefesi:

> If it walks like a duck and quacks like a duck, it is a duck.

Yani "bu obje Character'dan inherit ediyor mu?" sorusu yerine, sık sık "ihtiyacim
olan davranisa sahip mi?" sorusu daha onemlidir.

## 15. Interface Var mi?

Python'da C++/Java tarzi zorunlu interface keyword'u yoktur.

Alternatifler:

- Abstract base class kullanmak.
- `typing.Protocol` kullanmak.
- Sadece duck typing'e guvenmek.

### Abstract Base Class

```python
from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
```

### Protocol

`Protocol`, static type checking icin kullanislidir.

```python
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> None:
        ...


def render(item: Drawable) -> None:
    item.draw()
```

Bu runtime'da inheritance zorlamaz; type checker'a "draw metodu olan her sey
Drawable gibi davranabilir" der.

42 piscine icin genelde `abc.ABC` ve `abstractmethod` yeterlidir.

## 16. Encapsulation Python'da Nasil Dusunulur?

Python'da encapsulation daha cok API tasarimi ve convention ile saglanir.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    @property
    def balance(self):
        return self._balance
```

Kullanim:

```python
account = BankAccount(100)
account.deposit(50)
print(account.balance)      # 150
```

Burada `_balance` internal state'tir. Disaridan okunmasi icin `balance` property
verilmistir.

## 17. Property

Python'da getter/setter yazmanin idiomatik yolu `property` kullanmaktir.

Basit hali:

```python
class King:
    def __init__(self):
        self._eyes = "brown"

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value
```

Kullanim:

```python
joffrey = King()
print(joffrey.eyes)     # brown
joffrey.eyes = "blue"
print(joffrey.eyes)     # blue
```

Disaridan normal attribute gibi gorunur ama arka tarafta method calisir.

C++ karsiligi:

```cpp
std::string getEyes() const;
void setEyes(std::string value);
```

Python'da subject bazen explicit `get_eyes()` ve `set_eyes()` bekleyebilir. O
durumda subjecte uymak gerekir.

```python
class King:
    def __init__(self):
        self.eyes = "brown"

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, color):
        self.eyes = color
```

## 18. Magic Methods / Dunder Methods

Python'da `__init__`, `__str__`, `__repr__`, `__add__` gibi iki tarafinda cift
underscore olan metodlara dunder method denir.

Bunlar Python'in built-in davranislarini ozellestirir.

### `__str__`

Kullanici dostu string temsili.

```python
class Character:
    def __init__(self, first_name):
        self.first_name = first_name

    def __str__(self):
        return self.first_name


ned = Character("Ned")
print(ned)              # Ned
```

### `__repr__`

Debug/developer dostu temsil. Mumkunse objeyi yeniden yaratabilecek gibi olmali.

```python
class Character:
    def __init__(self, first_name):
        self.first_name = first_name

    def __repr__(self):
        return f"Character({self.first_name!r})"


ned = Character("Ned")
print(repr(ned))        # Character('Ned')
```

### Subjectteki Garip Cikti

42 subjectindeki ex01 expected output'ta su tarz bir cikti var:

```text
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
```

Bu, tester'in `print(Robert.__str__)` yazmasindan kaynaklanir. Yani method
cagrilmiyor, method objesi yazdiriliyor. Eger tester `print(Robert)` veya
`print(Robert.__str__())` deseydi donen string gorunurdu.

Bu nedenle `__str__` ve `__repr__` metodlari string dondurmelidir:

```python
class Baratheon:
    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return self.__str__()
```

## 19. Operator Overloading

C++:

```cpp
Vector operator+(const Vector& rhs);
```

Python:

```python
class Calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        result = [x + scalar for x in self.vector]
        print(result)
```

Kullanim:

```python
v = Calculator([0.0, 1.0, 2.0])
v + 5                  # [5.0, 6.0, 7.0]
```

Yaygin operator metodlari:

```text
+      __add__
-      __sub__
*      __mul__
/      __truediv__
//     __floordiv__
%      __mod__
==     __eq__
<      __lt__
<=     __le__
>      __gt__
>=     __ge__
[]     __getitem__
len()  __len__
call   __call__
```

Subjectte ex03 icin beklenen:

```python
class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar) -> None:
        print([x + scalar for x in self.vector])

    def __mul__(self, scalar) -> None:
        print([x * scalar for x in self.vector])

    def __sub__(self, scalar) -> None:
        print([x - scalar for x in self.vector])

    def __truediv__(self, scalar) -> None:
        if scalar == 0:
            print("Error: division by zero")
            return
        print([x / scalar for x in self.vector])
```

Normal Python tasariminda operator method'larinin yeni deger dondurmesi daha
beklenir. Ama bu subjectte `-> None` ve expected output `print` uzerinden
verildigi icin print etmek mantiklidir.

## 20. Decorator Nedir?

Decorator, bir function veya method'u saran/degistiren yapidir.

```python
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@my_decorator
def hello():
    print("hello")
```

Bu syntax aslinda suna denktir:

```python
hello = my_decorator(hello)
```

OOP'te en sik gorecegin decorator'lar:

- `@classmethod`
- `@staticmethod`
- `@property`
- `@abstractmethod`

## 21. `@staticmethod` ile Sinifi Instantiate Etmeden Method Cagirmak

Subject ex04 tam olarak bunu ister:

```python
class calculator:
    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        result = sum(a * b for a, b in zip(v1, v2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        result = [float(a + b) for a, b in zip(v1, v2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        result = [float(a - b) for a, b in zip(v1, v2)]
        print(f"Sous Vector is: {result}")
```

Kullanim:

```python
calculator.dotproduct([5, 10, 2], [2, 4, 3])
```

Burada object state'i yoktur. Bu nedenle `staticmethod` dogru secimdir.

## 22. Type Hints

Python dinamik tiplidir. Degiskenin tipi runtime'da belirlenir.

```python
x = 42
x = "Ned"      # Python izin verir
```

Ama type hint yazabilirsin:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Bu runtime'da zorlayici degildir:

```python
add("a", "b")  # calisir, "ab" dondurur
```

Type hint'ler:

- Okunabilirligi artirir.
- IDE desteğini guclendirir.
- `mypy`, `pyright` gibi static type checker'larla anlam kazanir.

OOP ornegi:

```python
class Character:
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        self.is_alive = False
```

## 23. Python'da Virtual Function Var mi?

C++'ta polymorphism icin `virtual` gerekir.

Python'da method lookup runtime'da yapildigi icin tum instance methodlar zaten
dinamik dispatch gibi davranir.

```python
class Base:
    def speak(self):
        print("base")


class Derived(Base):
    def speak(self):
        print("derived")


def call_speak(obj):
    obj.speak()


call_speak(Derived())   # derived
```

Python'da `virtual` keyword'u yoktur. Override etmek icin ayni isimli method'u
subclass'ta tanimlamak yeterlidir.

## 24. Override Keyword'u Var mi?

Python'da klasik anlamda built-in `override` keyword'u yoktur. Python 3.12 ile
`typing.override` geldi ama bu runtime davranisini degistirmez; type checker icin
anlamlidir.

Python 3.10 kullanan 42 subjecti icin genellikle override belirtmeden method
yazarsin.

```python
class Character:
    def die(self):
        self.is_alive = False


class Stark(Character):
    def die(self):
        super().die()
```

## 25. Overloading Var mi?

C++'ta ayni isimde farkli parametrelerle function overloading vardir.

```cpp
void f(int);
void f(std::string);
```

Python'da ayni class icinde ayni isimle ikinci method yazarsan birincinin ustune
yazarsin.

```python
class Example:
    def f(self, x):
        print("one arg")

    def f(self, x, y):
        print("two args")
```

Burada sadece ikinci `f` kalir.

Python'daki alternatifler:

### Default Parameter

```python
def greet(name, title=None):
    if title is None:
        print(f"Hello {name}")
    else:
        print(f"Hello {title} {name}")
```

### `*args`

```python
def add(*values):
    return sum(values)
```

### Type Kontrolu

```python
def describe(value):
    if isinstance(value, int):
        return "integer"
    if isinstance(value, str):
        return "string"
    return "unknown"
```

### `functools.singledispatch`

Daha ileri bir konu olarak runtime type'a gore dispatch yapabilir.

## 26. `object` Base Class'i

Python 3'te tum class'lar otomatik olarak `object`'ten inherit eder.

```python
class Character:
    pass
```

Aslinda:

```python
class Character(object):
    pass
```

gibi dusunulebilir.

Bu yuzden her objede temel dunder methodlari vardir.

```python
print(Character.__mro__)
```

## 27. `__dict__`

Bir objenin instance attribute'larini gormek icin `__dict__` kullanilabilir.

```python
class Character:
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True


ned = Character("Ned")
print(ned.__dict__)
```

Cikti:

```text
{'first_name': 'Ned', 'is_alive': True}
```

42 subjectindeki tester'lar sik sik `__dict__` bastirir. Bu yuzden attribute
isimleri expected output ile birebir uyumlu olmalidir.

Ornegin subject `hairs` bekliyorsa `hair` yazmak ciktiyi bozar.

## 28. Docstring

Subject ozellikle tum function, class ve method'larda documentation `__doc__`
olmasini ister.

```python
class Character:
    """Representing a character."""

    def __init__(self, first_name):
        """Initialize a character."""
        self.first_name = first_name

    def die(self):
        """Change alive state to False."""
        self.is_alive = False
```

Docstring'e erisim:

```python
print(Character.__doc__)
print(Character.__init__.__doc__)
print(Character.die.__doc__)
```

Python'da docstring, class/function/method govdesindeki ilk string literal'dir.

## 29. Global Scope ve `main()`

Subject der ki: global scope'ta kod yok, `main()` kullan.

Kotu:

```python
print("test")
```

Iyi:

```python
def main() -> None:
    """Run local tests."""
    print("test")


if __name__ == "__main__":
    main()
```

Bu pattern sayesinde dosya import edildiginde test kodu calismaz. Sadece dosya
direkt calistirildiginda calisir.

## 30. Exception Handling

Subject, yakalanmamis exception'larin egzersizi gecersiz kilabilecegini soyler.
Bu nedenle beklenen hatalari yakalamak gerekir.

```python
def safe_divide(a: float, b: float) -> float | None:
    """Divide two numbers safely."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
```

Python 3.10'da `float | None` syntax'i kullanilabilir.

ex03 icin subject sadece division by zero handling ister:

```python
def __truediv__(self, scalar) -> None:
    """Divide vector by scalar."""
    if scalar == 0:
        print("Error: division by zero")
        return
    print([x / scalar for x in self.vector])
```

## 31. Import Kurallari

Subject:

- Explicit import kullan.
- `from module import *` yasak.

Iyi:

```python
from abc import ABC, abstractmethod
import numpy as np
```

Kotu:

```python
from pandas import *
```

Kendi dosyalarinda:

```python
from S1E9 import Character
```

## 32. Python'da Const Var mi?

C++'ta:

```cpp
void f() const;
const int x = 5;
```

Python'da gercek `const` yoktur. Convention kullanilir.

```python
MAX_SIZE = 100
```

Buyuk harfle yazmak "constant gibi davran" demektir ama runtime'da degistirilebilir.

```python
MAX_SIZE = 200    # Python buna izin verir
```

Method seviyesinde `const method` karsiligi yoktur. Bir method'un object state'ini
degistirmeyecegi convention ve tasarimla anlatilir.

## 33. Reference, Pointer, Value Semantics

Python'da degiskenler object reference tutar.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)          # [1, 2, 3, 4]
```

C++'taki pointer/reference/value ayrimi Python'da ayni sekilde yoktur. Isimler
nesnelere baglanir.

Immutable object ornegi:

```python
x = 5
y = x
y += 1

print(x)          # 5
print(y)          # 6
```

Burada integer immutable oldugu icin `y += 1` yeni bir int object'e baglanir.

Mutable object ornegi:

```python
items = []
other = items
other.append("Ned")

print(items)      # ['Ned']
```

OOP yazarken mutable state paylasimina dikkat etmek gerekir.

## 34. Shallow Copy ve Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print(shallow)    # [[1, 2, 99], [3, 4]]
print(deep)       # [[1, 2], [3, 4]]
```

Class attribute olarak list/dict kullanirken veya object icinde nested mutable
state tasirken bu konu onemlidir.

## 35. Dataclass

Python'da sadece veri tasiyan class'lar icin `dataclasses` modulu vardir.

```python
from dataclasses import dataclass


@dataclass
class Character:
    first_name: str
    is_alive: bool = True
```

Bu otomatik olarak `__init__`, `__repr__`, `__eq__` gibi metodlari uretir.

Kullanim:

```python
ned = Character("Ned")
print(ned)        # Character(first_name='Ned', is_alive=True)
```

42 subjectindeki egzersizlerde dataclass kullanmak gerekmez; hatta expected
output'lar attribute sirasi ve custom method davranislari bekledigi icin klasik
class yazmak daha guvenlidir.

## 36. `__slots__`

Normalde Python objeleri attribute'larini `__dict__` icinde tutar.

```python
class Character:
    pass


ned = Character()
ned.first_name = "Ned"
ned.weapon = "Ice"
```

Python yeni attribute eklemeye izin verir.

`__slots__` bunu kisitlayabilir:

```python
class Character:
    __slots__ = ("first_name", "is_alive")

    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True
```

Artik yeni attribute eklemek hata verir:

```python
ned.weapon = "Ice"      # AttributeError
```

Bu C++'taki sabit member layout hissine biraz daha yakindir ama 42 subjectinde
`__dict__` bekleniyorsa `__slots__` kullanmamak gerekir. Cunku `__slots__`
varsayilan `__dict__` davranisini degistirir.

## 37. Composition vs Inheritance

C++'ta oldugu gibi Python'da da "inheritance mi composition mi?" sorusu onemlidir.

Inheritance:

```python
class SwordWeapon:
    def attack(self):
        print("slash")


class Knight(SwordWeapon):
    pass
```

Composition:

```python
class Sword:
    def attack(self):
        print("slash")


class Knight:
    def __init__(self):
        self.weapon = Sword()

    def attack(self):
        self.weapon.attack()
```

Genel prensip:

- "is-a" iliskisi varsa inheritance dusun.
- "has-a" iliskisi varsa composition dusun.

42'nin bu gunu inheritance ogretmeyi hedefledigi icin egzersizlerde inheritance
kullanmak beklenir.

## 38. Python'da Eksik veya Farkli Olan C++ OOP Ozellikleri

C++'tan gelen biri icin onemli farklar:

- Access modifier yok: `public`, `protected`, `private` keyword'leri yok.
- Header/source ayrimi yok.
- Methodlar default olarak virtual gibi davranir.
- Function overloading yok.
- Constructor overloading yok; default args veya classmethod factory kullanilir.
- Destructor deterministic degildir.
- Const correctness yok.
- Template yerine dynamic typing, generics ve type hints kullanilir.
- Multiple inheritance vardir ama MRO C3 linearization ile calisir.
- Operator overloading vardir ama Python dunder method isimleriyle yapilir.
- Attribute'lar dinamik eklenebilir.
- Abstract class icin `abc` modulu kullanilir.

## 39. Python'da Ekstra Gelen veya Daha Belirgin Olan Ozellikler

Python tarafinda C++'a gore daha one cikan ozellikler:

- Duck typing.
- `@property`.
- `@classmethod` ile alternative constructor/factory pattern.
- `@staticmethod`.
- Decorator mekanizmasi.
- Dunder methodlarla dil protokollerine katilma.
- Runtime introspection: `__dict__`, `type`, `isinstance`, `dir`, `mro`.
- Dynamic attribute ekleme.
- Context manager: `with`.
- Dataclass.
- Protocol/type hint sistemi.

## 40. 42 Python OOP Subjecti Icin Pratik Checklist

Her egzersiz icin:

- Dosya adi subject ile birebir ayni mi?
- Class adi subject ile birebir ayni mi?
- Attribute isimleri expected output ile birebir ayni mi?
- Global scope'ta test kodu var mi? Varsa `main()` icine al.
- Tüm class/function/method'larda docstring var mi?
- `from module import *` kullanilmamis mi?
- Abstract class gereken yerde `ABC` ve `@abstractmethod` kullanilmis mi?
- `__str__` ve `__repr__` string donduruyor mu?
- `@classmethod`, `@staticmethod`, `@property` gereken yerde dogru secilmis mi?
- Division by zero gibi subjectin istedigi hata durumlari yakalaniyor mu?
- `flake8` temiz mi?

## 41. Mini OOP Ornegi: Subject Tarzina Yakin

```python
from abc import ABC, abstractmethod


class Character(ABC):
    """Representing an abstract character."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a character."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Change alive state to False."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def die(self) -> None:
        """Change alive state to False."""
        super().die()


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Change alive state to False."""
        super().die()

    def __str__(self) -> str:
        """Return informal string representation."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self) -> str:
        """Return official string representation."""
        return self.__str__()
```

## 42. C++ - Python Kisa Karsilastirma Tablosu

| Kavram | C++ | Python |
| --- | --- | --- |
| Constructor | `ClassName(...)` | `__init__(self, ...)` |
| Destructor | `~ClassName()` | `__del__` var ama nadiren kullanilir |
| this | `this` | `self` |
| Inheritance | `class B : public A` | `class B(A):` |
| Base constructor | `B() : A()` | `super().__init__()` |
| Virtual method | `virtual` | Varsayilan dinamik dispatch |
| Pure virtual | `= 0` | `@abstractmethod` |
| Interface | Abstract class | ABC veya Protocol |
| Private | `private:` | Convention `_x`, name mangling `__x` |
| Static method | `static` | `@staticmethod` |
| Class factory | static member | `@classmethod` |
| Operator overload | `operator+` | `__add__` |
| Function overload | Desteklenir | Dogrudan desteklenmez |
| Const | `const` | Yok, convention |
| Template | `template <typename T>` | Dynamic typing, generics, type hints |
| Multiple inheritance | Var | Var, MRO/C3 ile |
| Runtime introspection | Sinirli | Cok guclu |

## Son Not

Python'da OOP yazarken C++ reflekslerini tamamen birakmak gerekmez; class,
inheritance, polymorphism, encapsulation ayni temel fikirlerdir. Ama Python daha
dinamik, convention odakli ve runtime davranislarina acik bir dildir.

42'nin bu subjectinde asil hedef sunlari pratik etmek:

- Abstract class
- Inheritance
- Multiple inheritance ve MRO
- Classmethod / staticmethod
- Property veya getter/setter mantigi
- Dunder methods
- Operator overloading
- Docstring ve temiz module yapisi
