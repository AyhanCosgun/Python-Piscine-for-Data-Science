# Python OOP Soru Cevaplari

Bu dosya, `Python_OOP_Notlari.md` uzerine gelen sorulari detaylandirmak icin
hazirlandi. Anlatim C++ OOP bilen biri icin yazildi; once C++ refleksini
hatirlatiyor, sonra Python'daki karsiligini gosteriyor.

## 1. `__new__` Nedir, Ne Ise Yarar?

Python'da bir nesne olusturulurken iki asama vardir:

1. `__new__`: Nesneyi gercekten olusturur.
2. `__init__`: Olusturulan nesneyi initialize eder.

Genelde biz sadece `__init__` yazariz:

```python
class Character:
    """Representing a character."""

    def __init__(self, name):
        """Initialize a character."""
        self.name = name


ned = Character("Ned")
```

Ama arka planda kabaca su olur:

```python
obj = Character.__new__(Character)
Character.__init__(obj, "Ned")
```

Yani:

- `__new__` object'i yaratir.
- `__init__` object'in icini doldurur.

### Basit `__new__` Ornegi

```python
class Character:
    """Representing a character."""

    def __new__(cls, name):
        """Create a new Character object."""
        print("__new__ called")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        """Initialize a Character object."""
        print("__init__ called")
        self.name = name


ned = Character("Ned")
print(ned.name)
```

Cikti:

```text
__new__ called
__init__ called
Ned
```

Buradaki `cls`, class'in kendisidir. `super().__new__(cls)` ise base class'tan
gercek bos object'i olusturmasini ister.

### `__new__` Ne Zaman Kullanilir?

Gunluk Python kodunda nadirdir. Daha cok su durumlarda kullanilir:

- Immutable tiplerden inherit ederken (`int`, `str`, `tuple` gibi).
- Singleton gibi object creation kontrolu gereken tasarimlarda.
- Nesne olusturulmadan once hangi class'in dondurulecegine karar vermek
  istediginde.
- Metaclass veya framework yazarken.

### Immutable Type Ornegi

`str` immutable'dir. Yani string olustuktan sonra icerigi degismez. Bu yuzden
`__init__` icinde string degerini degistiremezsin; object daha `__new__`
asamasinda dogru degerle olusmalidir.

```python
class UpperString(str):
    """String that always stores uppercase text."""

    def __new__(cls, value):
        """Create an uppercase string object."""
        return super().__new__(cls, value.upper())


name = UpperString("ned stark")
print(name)             # NED STARK
print(type(name))       # <class '__main__.UpperString'>
```

Burada `__init__` ile yapmak isteseydik gec kalmis olurduk, cunku `str` nesnesi
zaten olusmus olurdu.

### Singleton Ornegi

```python
class DatabaseConnection:
    """Very small singleton example."""

    _instance = None

    def __new__(cls):
        """Return the same instance every time."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = DatabaseConnection()
b = DatabaseConnection()

print(a is b)           # True
```

Bu ornekte `__new__`, her cagri icin yeni object yaratmak yerine daha once
yaratilmis object'i dondurur.

42 subjectinde `__new__` kullanmana gerek yok. `__init__` yeterli.

## 2. Garbage Collector, `__del__` ve Context Manager Nedir?

### Sorun Ne?

C++'ta stack uzerinde olusturulan bir object scope bitince deterministik olarak
yok edilir:

```cpp
void f() {
    File file("data.txt");
} // scope biter, destructor hemen calisir
```

Bu RAII mantigidir. Kaynak yasami object yasamina baglanir.

Python'da ise object'lerin ne zaman yok edilecegi C++ kadar net dusunulmemelidir.
Nesne artik kullanilmiyor gibi gorunse bile onun memory'den ne zaman temizlenecegi
implementation detayidir.

Bu yuzden dosya, socket, lock gibi kaynaklari `__del__` metoduna birakmak
risklidir.

### Garbage Collector Nedir?

Garbage collector, artik kullanilmayan nesneleri otomatik olarak temizleyen
mekanizmadir.

Python'da degiskenler object reference tutar:

```python
items = [1, 2, 3]
other = items
```

Burada listeye iki isim baglidir: `items` ve `other`.

```python
items = None
```

Liste hala yasiyor, cunku `other` ona bagli.

```python
other = None
```

Artik listeye ulasan isim kalmadi. Garbage collector bir noktada bu nesneyi
temizleyebilir.

CPython'da reference counting vardir; cogu nesne referans sayisi 0 olunca hemen
temizlenir. Ama:

- Circular reference varsa is gecikebilir.
- Python implementation'i CPython olmak zorunda degildir.
- `__del__` olan cyclic object'lerde davranis daha karmasik olabilir.
- Program kapanirken global nesnelerin temizlenme sirasi sorun cikarabilir.

Bu nedenle `__del__` kaynak yonetimi icin guvenilir ana arac degildir.

### `__del__` Neden Riskli?

```python
class FileWrapper:
    """Bad resource management example."""

    def __init__(self, path):
        """Open file."""
        self.file = open(path, "w", encoding="utf-8")

    def write(self, text):
        """Write text."""
        self.file.write(text)

    def __del__(self):
        """Close file when object is destroyed."""
        self.file.close()
```

Bu kodun sorunu:

- `__del__` ne zaman calisacak kesin degildir.
- Program kapanirken `self.file` bekledigin durumda olmayabilir.
- Exception olursa dosya uzun sure acik kalabilir.
- Socket/lock gibi kaynaklarda bu ciddi bug uretebilir.

### Context Manager Nedir?

Context manager, bir kaynagin giris ve cikis davranisini garantiye alan Python
yapisidir. `with` ile kullanilir.

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("hello")
```

Bu sunu garanti eder:

- Blok basinda dosya acilir.
- Blok normal bitse de exception ile bitse de dosya kapatilir.

Yani bu:

```python
file = open("data.txt", "w", encoding="utf-8")
try:
    file.write("hello")
finally:
    file.close()
```

mantiginin daha temiz halidir.

### Kendi Context Manager'ini Yazmak

Bir class'in context manager olmasi icin iki method gerekir:

- `__enter__`
- `__exit__`

```python
class ManagedFile:
    """Simple context manager for files."""

    def __init__(self, path):
        """Store file path."""
        self.path = path
        self.file = None

    def __enter__(self):
        """Acquire resource."""
        print("opening file")
        self.file = open(self.path, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Release resource."""
        print("closing file")
        self.file.close()
```

Kullanim:

```python
with ManagedFile("data.txt") as file:
    file.write("hello")
```

`__exit__`, blok icinde exception olsa bile calisir. Bu yuzden kaynak yonetimi
icin `__del__` yerine context manager tercih edilir.

## 3. `obj.__secret` ve `obj._Character__secret` Farki Nedir?

Python'da cift underscore ile baslayan attribute'larda name mangling vardir.

```python
class Character:
    """Representing a character."""

    def __init__(self):
        """Initialize secret."""
        self.__secret = "winter"


obj = Character()
```

Sen `self.__secret` yazdiginda Python bunu class adini ekleyerek saklar:

```python
self._Character__secret
```

Yani object'in icinde attribute gercekte `__secret` adi ile degil,
`_Character__secret` adi ile durur.

Kontrol:

```python
print(obj.__dict__)
```

Cikti:

```text
{'_Character__secret': 'winter'}
```

Bu nedenle:

```python
print(obj.__secret)
```

calismaz. Cunku object'te `__secret` diye bir attribute yoktur.

Ama:

```python
print(obj._Character__secret)
```

calisir. Cunku gercek attribute adi budur.

### `_Character` Kismi Nedir?

`_Character` kismi class adindan gelir. Python, `__secret` ismini class adiyla
birlikte degistirir:

```text
__secret  ->  _Character__secret
```

Bunun amaci guvenlik degil, subclass'larda isim cakismasini azaltmaktir.

Ornek:

```python
class Base:
    """Base class."""

    def __init__(self):
        """Initialize base secret."""
        self.__secret = "base"


class Derived(Base):
    """Derived class."""

    def __init__(self):
        """Initialize both secrets."""
        super().__init__()
        self.__secret = "derived"


obj = Derived()
print(obj.__dict__)
```

Cikti:

```text
{'_Base__secret': 'base', '_Derived__secret': 'derived'}
```

Iki class da `__secret` kullanabildi ama birbirini ezmedi.

## 4. `@classmethod` Nedir? Yazmazsak Ne Degisir?

Decorator, bir function veya method'un davranisini degistiren/saran yapidir.
`@classmethod`, normal method'u class method'a cevirir.

Normal instance method:

```python
class Lannister:
    """Representing Lannister family."""

    def create_lannister(self, name):
        """Incorrect factory as instance method."""
        return Lannister(name)
```

Bu method'u cagirmak icin once instance gerekir:

```python
cersei = Lannister("Cersei")
jaime = cersei.create_lannister("Jaime")
```

Ama factory method'un amaci zaten instance olusturmaksa, onu cagirmak icin once
instance istemek mantiksizdir.

`@classmethod` ile:

```python
class Lannister:
    """Representing Lannister family."""

    def __init__(self, name, is_alive=True):
        """Initialize a Lannister."""
        self.name = name
        self.is_alive = is_alive

    @classmethod
    def create_lannister(cls, name, is_alive=True):
        """Create a Lannister."""
        return cls(name, is_alive)
```

Kullanim:

```python
jaime = Lannister.create_lannister("Jaime")
print(jaime.name)
```

Burada ilk parametre `self` degil `cls` olur. `cls`, method'un hangi class
uzerinden cagrildigini temsil eder.

### Somut Fark: Inheritance

`@classmethod` kullanmanin asil gucu inheritance'ta gorulur.

```python
class Lannister:
    """Representing Lannister family."""

    def __init__(self, name):
        """Initialize a Lannister."""
        self.name = name

    @classmethod
    def create(cls, name):
        """Create an instance of the calling class."""
        return cls(name)


class RoyalLannister(Lannister):
    """Representing royal Lannister family."""


obj = RoyalLannister.create("Joffrey")
print(type(obj))        # <class '__main__.RoyalLannister'>
```

Neden? Cunku `cls`, `RoyalLannister` olur.

Eger hard-coded class adi kullansaydin:

```python
class Lannister:
    """Representing Lannister family."""

    def __init__(self, name):
        """Initialize a Lannister."""
        self.name = name

    @staticmethod
    def create(name):
        """Create specifically Lannister."""
        return Lannister(name)


class RoyalLannister(Lannister):
    """Representing royal Lannister family."""


obj = RoyalLannister.create("Joffrey")
print(type(obj))        # <class '__main__.Lannister'>
```

Bu sefer subclass uzerinden cagirsan bile base class dondurur.

### `@classmethod` Yazmazsak Ne Olur?

```python
class Example:
    """Example class."""

    def build(cls):
        """This is not a real classmethod."""
        return cls()


Example.build()
```

Bu hata verir:

```text
TypeError: Example.build() missing 1 required positional argument: 'cls'
```

Cunku Python `build` method'unu normal instance method sayar. Class uzerinden
cagirinca otomatik `cls` vermez.

### Kac Tane Decorator Var?

Python'da decorator sayisi sinirli degildir. Decorator, callable donduren herhangi
bir callable olabilir. Yani sen de kendi decorator'unu yazabilirsin.

Ama OOP'te sik kullanilan built-in/standart decorator'lar:

- `@classmethod`
- `@staticmethod`
- `@property`
- `@abstractmethod`
- `@property_name.setter`
- `@property_name.deleter`

Type checking tarafinda:

- `@typing.overload`
- `@typing.final`
- `@typing.override` Python 3.12 ile geldi, 3.10'da yok.

Framework'ler de kendi decorator'larini kullanir. Ornegin Flask'ta `@app.route`,
pytest'te `@pytest.mark...` gibi.

## 5. MRO Nedir? `__main__` Ne Anlama Geliyor?

MRO, Method Resolution Order demektir. Python bir attribute veya method ararken
class'lara hangi sirayla bakacagini MRO ile belirler.

Ornek:

```python
class A:
    """Base class A."""

    def who(self):
        """Return class name."""
        return "A"


class B(A):
    """Class B."""

    def who(self):
        """Return class name."""
        return "B"


class C(A):
    """Class C."""

    def who(self):
        """Return class name."""
        return "C"


class D(B, C):
    """Class D."""


print(D.mro())
print(D().who())
```

Cikti:

```text
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
B
```

Bu liste su anlama gelir:

1. Once `D` icinde `who` var mi diye bak.
2. Yoksa `B` icinde bak.
3. Yoksa `C` icinde bak.
4. Yoksa `A` icinde bak.
5. Yoksa en temel base class olan `object` icinde bak.

`D` icinde `who` yoktur. `B` icinde vardir. Bu yuzden `D().who()` sonucu `"B"`
olur.

### `__main__` Nedir?

`__main__`, kodun calistirildigi ana module adidir.

Bir Python dosyasini direkt calistirdiginda:

```bash
python test.py
```

o dosyanin module adi `__main__` olur.

Bu yuzden class temsillerinde sunu gorursun:

```text
<class '__main__.D'>
```

Anlami:

- Class adi: `D`
- Bu class'in bulundugu module: `__main__`

Eger class `S1E7.py` dosyasindan import edilseydi sunu gorebilirdin:

```text
<class 'S1E7.Baratheon'>
```

Yani `__main__`, class'in o anda direkt calistirilan dosyada tanimli oldugunu
gosterir.

### Diamond Problem ve C3 Linearization

Diamond inheritance:

```text
    A
   / \
  B   C
   \ /
    D
```

Python, `D(B, C)` icin `A` class'ini iki kez cagirmamak ve tutarli bir siralama
kurmak icin C3 linearization kullanir.

`super()` kullanimi da bu MRO sirasi uzerinden calisir.

```python
class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


D()
```

Cikti:

```text
D
B
C
A
```

`super()` "direkt parent'i cagir" demek degildir. "MRO'daki bir sonraki class'a
devam et" demektir. Bu nokta Python multiple inheritance icin cok onemlidir.

## 6. C++ Polymorphism Nasil Idi, Python Karsiligi Nedir?

### C++'ta Polymorphism

C++'ta runtime polymorphism icin genellikle base class pointer/reference ve
`virtual` method kullanilir.

```cpp
#include <iostream>

class Character {
public:
    virtual void speak() const {
        std::cout << "Character" << std::endl;
    }

    virtual ~Character() {}
};

class Stark : public Character {
public:
    void speak() const override {
        std::cout << "Winter is coming" << std::endl;
    }
};

class Lannister : public Character {
public:
    void speak() const override {
        std::cout << "Hear me roar" << std::endl;
    }
};

void introduce(const Character& character) {
    character.speak();
}

int main() {
    Stark ned;
    Lannister cersei;

    introduce(ned);      // Winter is coming
    introduce(cersei);   // Hear me roar
}
```

Burada `speak` virtual olmazsa, base class reference uzerinden cagrida base
class'in `speak` metodu calisabilir. `virtual` dinamik dispatch saglar.

### Python'da Polymorphism

Python'da method lookup runtime'da yapilir. `virtual` keyword'u yoktur.

```python
class Stark:
    """Representing Stark family."""

    def speak(self):
        """Speak like a Stark."""
        print("Winter is coming")


class Lannister:
    """Representing Lannister family."""

    def speak(self):
        """Speak like a Lannister."""
        print("Hear me roar")


def introduce(character):
    """Introduce any object that can speak."""
    character.speak()


introduce(Stark())       # Winter is coming
introduce(Lannister())   # Hear me roar
```

Burada `Stark` ve `Lannister` ayni base class'tan inherit etmek zorunda bile
degildir. `speak` metodu varsa yeter.

Bu duck typing'dir.

### Python'da Inheritance ile Polymorphism

```python
from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract character."""

    @abstractmethod
    def speak(self):
        """Speak."""


class Stark(Character):
    """Representing Stark family."""

    def speak(self):
        """Speak like a Stark."""
        print("Winter is coming")


def introduce(character: Character):
    """Introduce character."""
    character.speak()
```

Bu C++'taki abstract base class + virtual function modeline daha yakindir.

## 7. C++ Encapsulation Nasil Idi, Python Karsiligi Nedir?

### C++'ta Encapsulation

C++'ta data private yapilir, kontrollu erisim public methodlarla verilir.

```cpp
#include <stdexcept>

class BankAccount {
private:
    double balance;

public:
    BankAccount(double initial) : balance(initial) {}

    double getBalance() const {
        return balance;
    }

    void deposit(double amount) {
        if (amount <= 0) {
            throw std::invalid_argument("amount must be positive");
        }
        balance += amount;
    }
};
```

Burada `balance` disaridan direkt degistirilemez.

### Python'da Encapsulation

Python'da C++ gibi zorlayici `private` yoktur. Convention kullanilir.

```python
class BankAccount:
    """Representing a bank account."""

    def __init__(self, initial):
        """Initialize account."""
        self._balance = initial

    @property
    def balance(self):
        """Return current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposit positive amount."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount
```

Kullanim:

```python
account = BankAccount(100)
account.deposit(50)
print(account.balance)      # 150
```

`_balance`, "internal attribute" anlamina gelir. Disaridan teknik olarak
erisilebilir:

```python
account._balance = -999
```

Ama Python kulturunde bu "bunu yapma, class'in ic detayi" demektir.

Daha sert gizleme istersen name mangling kullanabilirsin:

```python
class BankAccount:
    """Representing a bank account."""

    def __init__(self, initial):
        """Initialize account."""
        self.__balance = initial
```

Ama bu da mutlak guvenlik degildir:

```python
account._BankAccount__balance = -999
```

Python encapsulation anlayisi:

- API'yi temiz tasarla.
- Internal attribute icin `_name` kullan.
- Gerekirse `@property` ile kontrollu okuma/yazma sagla.
- C++ gibi compile-time enforcement bekleme.

## 8. `@property` Ne Ise Yarar? `@eyes.setter` Standart mi?

`@property`, bir method'u attribute gibi kullanmani saglar.

Normal getter:

```python
class King:
    """Representing a king."""

    def __init__(self):
        """Initialize king."""
        self._eyes = "brown"

    def get_eyes(self):
        """Return eye color."""
        return self._eyes


joffrey = King()
print(joffrey.get_eyes())
```

Bu calisir. Getter method olur.

`@property` ile:

```python
class King:
    """Representing a king."""

    def __init__(self):
        """Initialize king."""
        self._eyes = "brown"

    @property
    def eyes(self):
        """Return eye color."""
        return self._eyes


joffrey = King()
print(joffrey.eyes)
```

Burada `eyes` normal attribute gibi okunur ama aslinda method calisir.

### Neden Guzel?

Ilk basta basit attribute ile baslayabilirsin:

```python
class King:
    """Representing a king."""

    def __init__(self):
        """Initialize king."""
        self.eyes = "brown"
```

Kullanici kodu:

```python
print(joffrey.eyes)
```

Sonradan validation eklemek istediginde API'yi bozmadan property'ye cevirebilirsin:

```python
class King:
    """Representing a king."""

    def __init__(self):
        """Initialize king."""
        self._eyes = "brown"

    @property
    def eyes(self):
        """Return eye color."""
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        """Set eye color."""
        if not value:
            raise ValueError("eyes cannot be empty")
        self._eyes = value
```

Kullanici kodu ayni kalir:

```python
joffrey.eyes = "blue"
print(joffrey.eyes)
```

### `@eyes.setter` Ismi Standart mi?

Evet, syntax su sekildedir:

```python
@property
def eyes(self):
    ...

@eyes.setter
def eyes(self, value):
    ...
```

Buradaki `eyes`, yukarida tanimlanan property'nin adidir. Setter decorator'u da
o property uzerinden gelir.

Isimler ayni olmalidir:

```python
@property
def eyes(self):
    return self._eyes

@eyes.setter
def eyes(self, value):
    self._eyes = value
```

Yanlis:

```python
@property
def eyes(self):
    return self._eyes

@eyes.setter
def set_eyes(self, value):
    self._eyes = value
```

Bu beklenen property setter davranisini vermez. Property'nin setter method'u da
property ile ayni isimde yazilir.

### Subjectte Ne Yapmali?

Pythonic tasarimda `@property` guzel secimdir. Ama 42 subjectindeki tester:

```python
Joffrey.set_eyes("blue")
print(Joffrey.get_eyes())
```

bekliyorsa `set_eyes` ve `get_eyes` methodlarini yazmalisin. Istersen arkada
property de kullanabilirsin ama tester'in bekledigi method isimleri bulunmali.

## 9. `__repr__` Acilimi Nedir, Ne Amacla Kullanilir?

`repr`, "representation" kelimesinin kisaltmasidir.

`__repr__`, bir object'in developer/debug odakli string temsilini dondurur.

```python
class Character:
    """Representing a character."""

    def __init__(self, name):
        """Initialize character."""
        self.name = name

    def __repr__(self):
        """Return developer representation."""
        return f"Character({self.name!r})"


ned = Character("Ned")
print(repr(ned))
```

Cikti:

```text
Character('Ned')
```

Genel beklenti sudur:

- `__str__`: Kullanici dostu temsil.
- `__repr__`: Debug/developer dostu temsil.

Ornek:

```python
class Character:
    """Representing a character."""

    def __init__(self, name):
        """Initialize character."""
        self.name = name

    def __str__(self):
        """Return readable representation."""
        return self.name

    def __repr__(self):
        """Return developer representation."""
        return f"Character({self.name!r})"


ned = Character("Ned")
print(str(ned))          # Ned
print(repr(ned))         # Character('Ned')
```

Python shell, listeler ve dict'ler object'leri gosterirken genellikle `repr`
kullanir:

```python
items = [Character("Ned"), Character("Arya")]
print(items)
```

Cikti:

```text
[Character('Ned'), Character('Arya')]
```

Eger `__repr__` yazmazsan Python default object temsili verir:

```text
<__main__.Character object at 0x...>
```

Bu debug icin pek kullanisli degildir.

## 10. `__str__` ve `__repr__` String Dondurmek Zorunda mi?

Evet, bu genel Python kuralidir. `__str__` ve `__repr__` metodlari string
dondurmelidir.

Yanlis:

```python
class Character:
    """Bad representation example."""

    def __str__(self):
        """Return non-string value."""
        return 42


print(str(Character()))
```

Bu hata verir:

```text
TypeError: __str__ returned non-string (type int)
```

Dogru:

```python
class Character:
    """Good representation example."""

    def __str__(self):
        """Return string value."""
        return "Character"
```

Yani "string dondurmeli" kismi ex01'e ozel degil, genel Python kuralidir.

Ama ex01'deki gariplik sudur:

```python
print(Robert.__str__)
```

Bu method'u cagirmiyor. Method objesinin kendisini yazdiriyor. Cagirmak icin:

```python
print(Robert.__str__())
```

veya daha dogru olarak:

```python
print(Robert)
```

yazilirdi.

Subjectte expected output method objesini gosterdigi icin goruntu biraz garip.
Fakat yine de senin `__str__` ve `__repr__` methodlarin string dondurmelidir.

## 11. `@dataclass` Bazi Metotlari Otomatik mi Uretiyor?

Evet. `@dataclass`, veri tasiyan class'lar icin tekrar eden boilerplate kodlari
otomatik uretir.

Normal class:

```python
class Character:
    """Representing a character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize character."""
        self.first_name = first_name
        self.is_alive = is_alive

    def __repr__(self):
        """Return representation."""
        return (
            f"Character(first_name={self.first_name!r}, "
            f"is_alive={self.is_alive!r})"
        )

    def __eq__(self, other):
        """Compare characters."""
        if not isinstance(other, Character):
            return False
        return (
            self.first_name == other.first_name
            and self.is_alive == other.is_alive
        )
```

Dataclass ile:

```python
from dataclasses import dataclass


@dataclass
class Character:
    """Representing a character."""

    first_name: str
    is_alive: bool = True
```

Kullanim:

```python
ned = Character("Ned")
other = Character("Ned")

print(ned)
print(ned == other)
```

Cikti:

```text
Character(first_name='Ned', is_alive=True)
True
```

Dataclass default olarak sunlari uretebilir:

- `__init__`
- `__repr__`
- `__eq__`

Opsiyonlara gore sunlari da uretebilir:

- ordering metodlari: `__lt__`, `__le__`, `__gt__`, `__ge__`
- frozen behavior: immutable gibi davranma
- slots behavior: Python 3.10'da `slots=True` kullanilabilir

Ornek:

```python
from dataclasses import dataclass


@dataclass(order=True)
class Point:
    """Comparable point."""

    x: int
    y: int


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 < p2)          # True
```

Frozen dataclass:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Character:
    """Immutable-like character."""

    first_name: str
    is_alive: bool = True


ned = Character("Ned")
ned.first_name = "Robb"  # FrozenInstanceError
```

### 42 Subjectinde Dataclass Kullanilir mi?

Bu subject icin genelde gerekmez. Hatta bazen riskli olabilir, cunku subject:

- belirli attribute isimleri,
- belirli `__dict__` ciktisi,
- belirli custom `__str__` / `__repr__`,
- belirli inheritance davranisi

bekliyor.

Dataclass cok guzel bir Python ozelligidir ama bu projede temel OOP mekaniklerini
elle yazmak daha ogretici ve daha guvenli.

## Kisa Ozet

- `__new__`, nesneyi olusturur; `__init__`, nesneyi initialize eder.
- Garbage collector, kullanilmayan object'leri otomatik temizler ama kaynak
  kapatmayi ona birakmak iyi fikir degildir.
- Context manager, `with` blogu ile kaynak acma/kapama islemini garantiye alir.
- `__secret`, name mangling ile `_ClassName__secret` adina donusur.
- `@classmethod`, method'a instance yerine class'i verir.
- MRO, Python'in method arama sirasidir.
- `__main__`, direkt calistirilan module adidir.
- Python'da polymorphism icin `virtual` gerekmez; duck typing ve runtime method
  lookup vardir.
- Python encapsulation'i C++ kadar zorlayici degil, convention ve property
  odaklidir.
- `@property`, method'u attribute gibi kullandirir.
- `__repr__`, representation demektir ve debug temsili icindir.
- `__str__` ve `__repr__` genel kural olarak string dondurmelidir.
- `@dataclass`, `__init__`, `__repr__`, `__eq__` gibi metodlari otomatik
  uretebilir.
