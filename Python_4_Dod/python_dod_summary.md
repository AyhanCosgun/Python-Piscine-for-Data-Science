# Python 4 Dod - Data Oriented Design Ozeti

Bu dosya `/home/ayhan/Masaüstü/Python Piscine/piscine_github/Python_4_Dod/Python_4_Dod.pdf` subject dosyasina gore hazirlanmistir. Proje, Ecole 42 "Python for Data Science piscine" serisinin 4. projesidir.

## 1. Projenin konusu ve amaci

Projenin resmi basligi:

> Data Oriented Design

Subject kisa olsa da egzersizlerin asil amaci Python'da daha duzenli, tekrar kullanilabilir ve kontrollu yapilar kurmayi ogretmektir:

- Degisken sayida arguman almak: `*args`, `**kwargs`
- Fonksiyon icinde fonksiyon tanimlamak
- Bir fonksiyonun baska bir fonksiyonu dondurmesi
- Closure kullanmak
- `nonlocal` mantigini anlamak
- Decorator yazmak
- Wrapper fonksiyon kavramini anlamak
- Dataclass ile veri odakli sinif tanimlamak
- Otomatik uretilen `__init__`, `__repr__` gibi davranislari kullanmak
- Hata durumlarini programi patlatmadan yonetmek

Subject'in girisinde data scientist'lerin bazen cok fazla hard-coded, daginik ve bakimi zor kod yazdigindan bahsediliyor. Bu proje bu aliskanligin tersine, veriyi ve fonksiyon davranisini daha temiz tasarlamayi hedefliyor.

Buradaki "Data Oriented Design", oyun motorlarindaki ileri seviye DOD anlaminda cok derin bir konu olarak islenmiyor. Bu piscine projesinde daha cok "veri tasiyan yapilar", "fonksiyon davranisini veri gibi tasimak", "argumanlari esnek almak" ve "siniflari daha temiz veri modelleri olarak tanimlamak" uzerinden isleniyor.

## 2. Genel proje kurallari

Tum egzersizlerde su kurallar onemli:

- Python 3.10 kullanilmali.
- Kod global scope'ta calisan basit script gibi olmamali.
- Test kodu varsa `main()` icinde olmali:

```python
def main():
    # tests and error handling


if __name__ == "__main__":
    main()
```

- Global variable yasak.
- Yakalanmamis exception egzersizi gecersiz yapabilir.
- Importlar acik olmali. Ornek: `import numpy as np`; `from pandas import *` yasak.
- Tum function, class ve method'larin docstring'i olmali.
- Kod `flake8` normuna uygun olmali.
- Subject'e gore built-in fonksiyonlar, egzersizde ozellikle yasaklanmadiysa kullanilabilir.

Bu projede egzersizlerin cogu "Allowed functions: None" diyor. Bunu pratikte su sekilde dusunmek en guvenlisi:

- Hazir istatistik kutuphanesiyle isi bitirme.
- Gereken mantigi kendin kur.
- Gereksiz import kullanma.
- Built-in temel yapilarla, listelerle, dongulerle, fonksiyonlarla coz.

## 3. Projeye baslamadan bilinmesi gereken temel konular

### `*args` nedir?

`*args`, fonksiyona sayisi bastan belli olmayan positional argument aldirir.

Ornek:

```python
def f(*args):
    print(args)


f(1, 2, 3)
```

Burada `args` bir tuple olur:

```text
(1, 2, 3)
```

Yani ex00'daki:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean")
```

cagrisinda `*args` sunlari yakalar:

```python
(1, 42, 360, 11, 64)
```

### `**kwargs` nedir?

`**kwargs`, fonksiyona sayisi bastan belli olmayan named/keyword argument aldirir.

Ornek:

```python
def f(**kwargs):
    print(kwargs)


f(toto="mean", tutu="median")
```

Burada `kwargs` bir dictionary olur:

```python
{"toto": "mean", "tutu": "median"}
```

Yani `toto`, `tutu`, `tata`, `hello`, `world` gibi isimler istatistik turu degil. Onlar sadece key. Subject bilerek garip isimler vermis, cunku fonksiyonun key adina degil value degerine bakmasi isteniyor.

Su cagrida:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
```

asıl istekler `kwargs.values()` tarafindadir:

```python
"mean", "median", "quartile"
```

Bu yuzden `toto`, `tutu`, `tata` isimlerinin özel anlami yoktur.

### Closure nedir?

Closure, bir inner fonksiyonun, dis fonksiyon bitmis olsa bile dis fonksiyondaki bazi degiskenleri hatirlamasidir.

Basit ornek:

```python
def outer():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner
```

`outer()` cagrildiginda `inner` fonksiyonu dondurulur. Ama `inner`, `counter` degiskenini hatirlamaya devam eder.

Ex01 ve ex02'nin temel konusu budur.

### `nonlocal` nedir?

Bir inner fonksiyon, dis fonksiyondaki degiskeni sadece okumak istiyorsa normalde sorun yoktur. Ama o degiskeni yeniden atamak istiyorsa `nonlocal` gerekir.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 1
        return x

    return inner
```

`global` yasak oldugu icin ex01 ve ex02'de durum saklamak icin dogru yol closure + `nonlocal` kullanmaktir.

### Generator nedir?

Generator, `yield` kullanan ve her cagrida siradaki degeri ureten ozel bir iterator yapisidir.

```python
def gen():
    yield 1
    yield 2
    yield 3
```

Bu projede ex01 ve ex02 generator istemiyor. Cunku subject'te `yield`, iterator veya `next()` davranisi yok. Buradaki beklenti, cagrildikca ic durumunu hatirlayan normal inner fonksiyonlardir.

### Decorator nedir?

Decorator, bir fonksiyonun davranisini sarmalayarak degistiren yapidir.

```python
@decorator
def f():
    pass
```

su anlama gelir:

```python
def f():
    pass

f = decorator(f)
```

Ex02'nin asil konusu decorator yazmaktir.

### Wrapper nedir?

Wrapper, orijinal fonksiyonun etrafina sarilan ara fonksiyondur. Orijinal fonksiyon cagrilmadan once veya sonra ek kontrol yapabilir.

Ex02'de wrapper, fonksiyonun kac defa cagrildigini sayacak ve limit asildiysa orijinal fonksiyonu calistirmayacaktir.

## 4. Exercise 00 - Calculate my statistics

### Teslim bilgisi

- Klasor: `ex00/`
- Dosya: `statistics.py`
- Fonksiyon prototipi:

```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
    # your code here
```

### Istenen davranis

Fonksiyon, bilinmeyen sayida sayisal deger alacak ve `kwargs` icinde istenen istatistiklere gore sonuc yazdiracak.

Desteklenmesi gereken istekler:

- `"mean"`
- `"median"`
- `"quartile"`
- `"std"`
- `"var"`

Subject'teki tester:

```python
from statistics import ft_statistics

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

Beklenen cikti:

```text
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
```

### `toto`, `tutu`, `tata` neden var?

Bu isimlerin ozel anlami yok. Bunlar `kwargs` key'leri.

Fonksiyonun su mantikla calismasi beklenir:

```python
for request in kwargs.values():
    if request == "mean":
        ...
    elif request == "median":
        ...
```

Yani:

```python
toto="mean"
```

demek, "`toto` isimli istegin degeri `mean`" demektir. Istatistik tipi key'de degil value'dadir.

### Mean nedir?

Mean, aritmetik ortalamadir.

Formul:

```text
toplam / eleman_sayisi
```

Ornek:

```text
1, 42, 360, 11, 64
```

Toplam:

```text
478
```

Eleman sayisi:

```text
5
```

Mean:

```text
478 / 5 = 95.6
```

### Median nedir?

Median, siralanmis verinin ortadaki degeridir.

Ornek veri:

```text
1, 42, 360, 11, 64
```

Siralanmis hali:

```text
1, 11, 42, 64, 360
```

Ortadaki deger:

```text
42
```

Eleman sayisi tekse direkt orta eleman alinir. Eleman sayisi ciftse ortadaki iki degerin ortalamasi alinir.

### Quartile nedir?

Quartile, siralanmis veriyi dort parcaya bolmeye yarayan ceyrek degerlerdir.

Bu egzersizde istenen:

- 25% quartile
- 75% quartile

Yani verinin ilk ceyrek noktasi ve ucuncu ceyrek noktasi.

Subject'in bekledigi ornege gore:

```text
1, 42, 360, 11, 64
```

siralanir:

```text
1, 11, 42, 64, 360
```

Beklenen quartile:

```text
[11.0, 64.0]
```

Bu, pratikte su indeks mantigiyla uyumludur:

```python
q1_index = int(len(values) * 0.25)
q3_index = int(len(values) * 0.75)
```

5 eleman icin:

```text
int(5 * 0.25) = 1
int(5 * 0.75) = 3
```

Indeks 1:

```text
11
```

Indeks 3:

```text
64
```

Sonuc float olarak yazilir:

```text
[11.0, 64.0]
```

Not: Istatistikte quartile hesaplamanin birden fazla yontemi vardir. Bu subject icin onemli olan matematik kitabi tanimi degil, expected output ile uyumlu davranistir.

### Variance nedir?

Variance, degerlerin ortalamadan ne kadar saptigini olcer.

Bu subject'teki beklenen sonuc population variance yani `n`'e bolunen varyans ile uyumludur.

Formul:

```text
sum((x - mean) ** 2) / n
```

Subject'teki ikinci veri seti:

```text
5, 75, 450, 18, 597, 27474, 48575
```

Beklenen:

```text
var : 323377543.9183673
```

Bu, `n - 1` degil direkt `n` kullanildigini gosterir.

### Standard deviation nedir?

Standard deviation, variance'in karekokudur.

Formul:

```text
variance ** 0.5
```

Beklenen:

```text
std : 17982.70124086944
```

### Hata yonetimi

Eger sayisal veri yoksa ve istenen islem gecerlise `ERROR` yazdirilmali.

Ornek:

```python
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

Burada `args` bostur. Uc tane gecerli istek oldugu icin uc kere:

```text
ERROR
ERROR
ERROR
```

yazilir.

Gecersiz isteklerde bir sey yazdirilmaz.

Ornek:

```python
ft_statistics(5, 75, ejfhhe="heheh", ejdjdejn="kdekem")
```

`"heheh"` ve `"kdekem"` desteklenen istekler degildir. Expected output'ta bu bolumde ek bir satir yoktur.

### Ex00 icin dikkat edilmesi gerekenler

- `statistics.py` dosyasi Python'un kendi `statistics` moduluyle ayni isimde. Tester `from statistics import ft_statistics` dedigi icin local dosya dogru klasorden calistirilmalidir.
- Key isimlerine degil `kwargs` value degerlerine bakilmali.
- Bos veri durumunda exception firlatilmamali.
- Gecersiz istekler sessizce gecilebilir.
- Cikti formatlari subject ile ayni olmali:

```text
mean : ...
median : ...
quartile : [...]
std : ...
var : ...
ERROR
```

## 5. Exercise 01 - Outer_inner

### Teslim bilgisi

- Klasor: `ex01/`
- Dosya: `in_out.py`
- Fonksiyon prototipleri:

```python
def square(x: int | float) -> int | float:
    # your code here


def pow(x: int | float) -> int | float:
    # your code here


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        # your code here
```

### Istenen fonksiyonlar

`square(x)`:

```text
x'in karesi
```

Yani:

```python
x ** 2
```

`pow(x)`:

```text
x'in kendisi kadar kuvveti
```

Yani:

```python
x ** x
```

`outer(x, function)`:

Bir sayi ve bir fonksiyon alir. Geriye cagrilabilir bir nesne dondurur. Bu nesne her cagrildiginda son degeri hatirlar ve uzerine tekrar verilen fonksiyonu uygular.

### Subject tester

```python
from in_out import outer
from in_out import square
from in_out import pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
```

Beklenen cikti:

```text
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
```

### Bu nasil calisiyor?

Ilk kisim:

```python
my_counter = outer(3, square)
```

Baslangic degeri:

```text
3
```

Ilk cagri:

```text
square(3) = 9
```

Ikinci cagri artik 3'e degil 9'a uygulanir:

```text
square(9) = 81
```

Ucuncu cagri:

```text
square(81) = 6561
```

Yani `inner`, son sonucu hatirlamalidir.

Ikinci kisim:

```python
another_counter = outer(1.5, pow)
```

`pow(x)` burada `x ** x` demektir.

Ilk cagri:

```text
1.5 ** 1.5 = 1.8371173070873836
```

Ikinci cagri:

```text
1.8371173070873836 ** 1.8371173070873836 = 3.056683336818703
```

Ucuncu cagri:

```text
3.056683336818703 ** 3.056683336818703 = 30.42684786675409
```

### Ex01 generator ile mi kurulacak?

Hayir. Bu egzersiz generator egzersizi gibi gorunebilir, cunku fonksiyon her cagrida yeni bir deger uretiyor. Ama subject'te generator istenmiyor.

Generator olsaydi muhtemelen:

- `yield`
- `next()`
- iterator davranisi

gibi seyler gorurduk.

Burada asil konu:

- inner function
- closure
- fonksiyonun state hatirlamasi
- `nonlocal`
- global kullanmadan durum saklamak

`outer` fonksiyonu bir generator degil, cagrilabilir bir inner fonksiyon dondurmelidir.

### Ex01'in amaci generatorleri tanitmak mi?

Hayir. Daha dogru cevap: Ex01'in amaci closure ve higher-order function kavramlarini tanitmak.

Higher-order function, baska bir fonksiyonu arguman olarak alan veya fonksiyon donduren fonksiyondur.

`outer(x, function)` bunu yapar:

- `function` arguman olarak alinir.
- `inner` fonksiyonu dondurulur.

### Ex01 icin dikkat edilmesi gerekenler

- `global` kullanma.
- `inner` icinde disaridaki mevcut degeri guncellemek icin `nonlocal` kullanmak gerekir.
- Fonksiyonlarin docstring'i olmali.
- `pow` ismi Python built-in `pow` fonksiyonuyla ayni isimdir. Subject bunu istedigi icin dosyada bu isimle fonksiyon yazilmalidir.

## 6. Exercise 02 - My first decorating

### Teslim bilgisi

- Klasor: `ex02/`
- Dosya: `callLimit.py`
- Fonksiyon prototipi:

```python
def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            # your code here
```

### Istenen davranis

Bir decorator yazilacak. Bu decorator, bir fonksiyonun en fazla kac kere calisabilecegini sinirlayacak.

Subject tester:

```python
from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()
```

Beklenen cikti:

```text
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
```

Memory address kismi, yani `0x7fabdc243ee0`, her calismada degisebilir. Onemli olan formatin su mantiga benzemesidir:

```text
Error: <function g at ...> call too many times
```

### Decorator zinciri nasil calisir?

Bu ifade:

```python
@callLimit(3)
def f():
    print("f()")
```

aslinda su anlama gelir:

```python
def f():
    print("f()")


f = callLimit(3)(f)
```

Adim adim:

1. `callLimit(3)` cagrilir.
2. Bu fonksiyon `callLimiter` isimli decorator fonksiyonunu dondurur.
3. Python, orijinal `f` fonksiyonunu `callLimiter` icine verir.
4. `callLimiter`, `limit_function` isimli wrapper fonksiyonu dondurur.
5. Artik `f()` cagrildiginda aslinda `limit_function()` calisir.
6. `limit_function`, sayaci kontrol eder.
7. Limit asilmazsa orijinal `function` cagrilir.
8. Limit asilirsa hata mesaji yazdirilir.

### `*args` ve `**kwds` burada ne ise yariyor?

Wrapper fonksiyonun orijinal fonksiyonun her turlu argumanini tasiyabilmesi icin kullanilir.

Subject tester'da `f()` ve `g()` argumansizdir. Ama decorator genel yazilmalidir.

Ornek:

```python
@callLimit(2)
def hello(name, loud=False):
    print(name, loud)
```

Bu fonksiyon cagrilirsa:

```python
hello("Ayhan", loud=True)
```

wrapper bunu yakalamalidir:

```python
def limit_function(*args, **kwds):
    return function(*args, **kwds)
```

Burada:

- `args`: positional argument'lari tasir.
- `kwds`: keyword argument'lari tasir.

`kwds` ismi `kwargs` ile ayni mantiktadir. Sadece degisken adi farklidir.

### Ex02 generator mi kullanacak?

Hayir. Ex02 de generator istemiyor.

Burada her cagrida bir sayac artiyor, ama bu generator degil closure state'idir.

Dogru ana fikir:

- decorator
- wrapper
- closure
- call count saklama
- limit kontrolu

### "Wrappers" ipucu ne demek?

Subject'in "Wrappers" ipucu, decorator'un icinde orijinal fonksiyonu saran bir fonksiyon yazman gerektigini soyluyor.

Wrapper fonksiyonun gorevi:

- Orijinal fonksiyonun yerine gecmek.
- Cagri sayisini kontrol etmek.
- Limit dolmadiysa orijinal fonksiyonu calistirmak.
- Limit dolduysa hata yazmak.
- Argumanlari bozmadan orijinal fonksiyona iletmek.

### Ex02 icin dikkat edilmesi gerekenler

- `count` closure icinde saklanmali.
- `count` guncellenecegi icin wrapper icinde `nonlocal count` gerekir.
- Limit asildiginda exception firlatmak yerine subject'in bekledigi gibi `print` ile hata yazdirmak daha uygundur.
- Orijinal fonksiyonun return degeri varsa wrapper bunu dondurmelidir.
- `function` objesini direkt f-string icinde yazdirmak expected output'a benzer:

```python
print(f"Error: {function} call too many times")
```

## 7. Exercise 03 - Data class

### Teslim bilgisi

- Klasor: `ex03/`
- Dosya: `new_student.py`
- Izinli kutuphaneler:
  - `dataclasses`
  - `random`
  - `string`

Subject prototipi:

```python
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    # your code here
```

### Istenen davranis

Bir `Student` dataclass'i yazilacak.

Constructor ile alinmasi gereken alanlar:

- `name`
- `surname`

Otomatik atanacak alanlar:

- `active=True`
- `login`
- `id`

Subject tester:

```python
from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
```

Beklenen cikti:

```text
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
```

`id` random oldugu icin her calismada degisir.

### Dataclass nedir?

Dataclass, veri tasimak icin kullanilan siniflari daha az kodla yazmayi saglayan Python ozelligidir.

Normalde su tarz bir sinif yazmak gerekir:

```python
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.active = True
```

Dataclass ile alanlari tanimlamak yeterlidir:

```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
```

Python otomatik olarak sunlari uretir:

- `__init__`
- `__repr__`
- `__eq__` gibi bazi yardimci davranislar

Bu yuzden `print(student)` dediginde anlamli bir cikti gelir.

### `field` ne ise yarar?

`field`, dataclass alanlarinin daha detayli davranisini ayarlamak icin kullanilir.

Bu egzersizde ozellikle lazim olan:

```python
field(init=False)
```

Bu, ilgili alanin `__init__` tarafindan kullanicidan alinmamasini saglar.

Subject diyor ki:

> The login and id should not be initializable and must return an error.

Yani su gecersiz olmali:

```python
Student(name="Edward", surname="agle", id="toto")
```

Beklenen:

```text
TypeError: Student.__init__() got an unexpected keyword argument 'id'
```

Bunu saglamak icin `id` alaninin `init=False` olmasi gerekir.

Ayni sekilde `login` de kullanicidan alinmamalidir.

### `id` nasil uretilmeli?

Subject'in verdigi fonksiyon:

```python
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))
```

Bu fonksiyon 15 karakterlik random kucuk harfli bir string uretir.

Dataclass'ta random veya dinamik degerler icin `default_factory` kullanmak dogru yaklasimdir:

```python
id: str = field(default_factory=generate_id, init=False)
```

`default_factory`, her yeni `Student` nesnesi icin fonksiyonu yeniden cagirir.

### `login` nasil uretilmeli?

Expected output'a gore:

```python
Student(name="Edward", surname="agle")
```

login:

```text
Eagle
```

Bu, `name` alaninin ilk harfi ile `surname` alaninin birlesimi gibi gorunuyor:

```python
name[0] + surname
```

Edward + agle:

```text
E + agle = Eagle
```

`login`, `name` ve `surname` degerlerinden turetilen bir alan oldugu icin `__post_init__` icinde atanabilir.

### `__post_init__` nedir?

Dataclass `__init__` islemini bitirdikten sonra otomatik olarak `__post_init__` methodunu cagirir.

Bu method, baska alanlardan turetilen alanlari hesaplamak icin kullanislidir.

Ornek:

```python
@dataclass
class Student:
    name: str
    surname: str
    login: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
```

### "`You must not use __str__, __repr__ in your class`" ne demek?

Bu uyari cok onemli.

Normalde bir nesne yazdirildiginda nasil gorunecegini belirlemek icin `__str__` veya `__repr__` yazilabilir.

Ama subject bunu yasakliyor. Neden?

Cunku dataclass zaten otomatik olarak `__repr__` uretir.

Beklenen cikti:

```text
Student(name='Edward', surname='agle', active=True, login='Eagle', id='...')
```

tam olarak dataclass'in otomatik `repr` formatina benzer.

Yani bu egzersizde beklenen:

- Manuel `__str__` yazma.
- Manuel `__repr__` yazma.
- Dataclass'in otomatik urettigi gosterimi kullan.

Eger elle `__repr__` yazarsan subject'in asil amacini bypass etmis olursun.

### Ex03 icin dikkat edilmesi gerekenler

- `@dataclass` kullanilmali.
- `name` ve `surname` init'ten alinmali.
- `active` default olarak `True` olmali.
- `login` kullanici tarafindan verilememeli.
- `id` kullanici tarafindan verilememeli.
- `id` random uretilmeli.
- `login`, `name[0] + surname` mantigiyla uretilmeli.
- `__str__` ve `__repr__` yazilmamali.
- `generate_id` fonksiyonu subject'teki gibi olmali.

## 8. Egzersizlerin birbirine baglandigi ana fikir

Bu proje dort farkli Python mekanizmasini birbirine yakin sekilde gosteriyor:

Ex00:

- Fonksiyon argumanlarini esnek almak.
- `*args` ve `**kwargs` ile veri/komut ayrimi yapmak.
- Basit veri islemleri yapmak.

Ex01:

- Fonksiyonu veri gibi arguman olarak almak.
- Fonksiyon dondurmek.
- Closure ile state saklamak.

Ex02:

- Decorator yazmak.
- Wrapper ile fonksiyon davranisini kontrol etmek.
- Closure ile call count saklamak.

Ex03:

- Veri modelini dataclass ile temiz tanimlamak.
- Otomatik uretilen init ve repr davranislarini kullanmak.
- Bazi alanlari init disinda hesaplamak.

Kisa ozetle proje, "Python'da fonksiyonlar ve class'lar sadece kod bloklari degil, tasarlanabilir davranis ve veri yapilaridir" fikrini ogretiyor.

## 9. Baslamadan once calisilmasi iyi olacak mini konu listesi

Projeye baslamadan su konulari bilmek isi cok kolaylastirir:

- Tuple ve dictionary farki
- `*args`
- `**kwargs`
- `for value in kwargs.values()`
- Fonksiyonun baska bir fonksiyonu arguman almasi
- Fonksiyonun inner fonksiyon dondurmesi
- Closure
- `nonlocal`
- Decorator syntax'i: `@decorator`
- Wrapper fonksiyon
- Dataclass
- `field(init=False)`
- `field(default_factory=...)`
- `__post_init__`
- Population variance ve standard deviation
- Median ve quartile hesaplama

## 10. Uygulama sirasinda en muhtemel hatalar

Ex00:

- `kwargs` key'lerine bakmak. Dogrusu value'lara bakmak.
- Bos `args` durumunda exception almak.
- Gecersiz isteklerde gereksiz hata yazmak.
- Variance'i `n - 1` ile bolmek. Subject `n` bekliyor.
- Quartile'i farkli istatistik yontemiyle hesaplayip expected output'tan sapmak.

Ex01:

- Her cagrida baslangic `x` degerini kullanmak. Dogrusu son sonucu hatirlamak.
- `global` kullanmak.
- `nonlocal` kullanmadan dis degiskeni guncellemeye calismak.
- Generator sanip `yield` kullanmak.

Ex02:

- Decorator katmanlarini karistirmak.
- Wrapper'da `*args`, `**kwds` ile orijinal argumanlari forward etmemek.
- Limit asildiginda hata mesaji yerine exception firlatmak.
- `count` degiskenini global yapmak.

Ex03:

- `__str__` veya `__repr__` yazmak.
- `id` veya `login` alanlarini init'te verilebilir birakmak.
- Random id icin `default_factory` yerine fonksiyonu class tanimlanirken bir kere cagirmak.
- `login` alanini `__post_init__` icinde hesaplamamak.

## 11. Subject'e gore teslim edilecek dosya yapisi

Beklenen dosya yapisi:

```text
Python_4_Dod/
├── ex00/
│   └── statistics.py
├── ex01/
│   └── in_out.py
├── ex02/
│   └── callLimit.py
└── ex03/
    └── new_student.py
```

Bu repository icinde sadece bu dosyalar degerlendirilecek. Dosya ve klasor isimleri subject ile birebir ayni olmali.

