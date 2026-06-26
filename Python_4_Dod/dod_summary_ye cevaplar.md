# DOD Summary Ek Sorulara Cevaplar

Bu dosya, `python_dod_summary.md` dosyasindan sonra gelen ek sorulara detayli ve ornekli cevap vermek icin hazirlandi.

## 1. `*args`, `**kwargs`, yildizlar ve argumanlarin paylasilmasi

### `*args` her zaman tuple mi olur?

Fonksiyon taniminda su sekilde yazarsan:

```python
def f(*args):
    print(args)
    print(type(args))
```

ve fonksiyonu soyle cagirirsan:

```python
f(10, 20, 30)
```

cikti:

```text
(10, 20, 30)
<class 'tuple'>
```

Yani evet: fonksiyon taniminda `*args` kullanildiginda, yakalanan fazladan positional argument'lar tuple olarak gelir.

Ama burada ozel olan `args` kelimesi degil, basindaki `*` isaretidir.

Su da ayni sekilde calisir:

```python
def f(*numbers):
    print(numbers)
    print(type(numbers))


f(10, 20, 30)
```

Cikti:

```text
(10, 20, 30)
<class 'tuple'>
```

Yani `args` bir keyword degil, sadece geleneksel bir isimdir. Python toplulugunda herkes bu ismi kullandigi icin okunmasi kolay olur.

### `**kwargs` her zaman dict mi olur?

Fonksiyon taniminda su sekilde yazarsan:

```python
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
```

ve fonksiyonu soyle cagirirsan:

```python
f(name="Ayhan", age=25)
```

cikti:

```text
{'name': 'Ayhan', 'age': 25}
<class 'dict'>
```

Yani evet: fonksiyon taniminda `**kwargs` kullanildiginda, yakalanan fazladan keyword argument'lar dict olarak gelir.

Burada da ozel olan `kwargs` kelimesi degil, basindaki `**` isaretidir.

Su da ayni sekilde calisir:

```python
def f(**options):
    print(options)


f(name="Ayhan", age=25)
```

Cikti:

```text
{'name': 'Ayhan', 'age': 25}
```

Ama Python'daki yaygin isim `kwargs` oldugu icin genelde onu kullaniriz. `kwargs`, "keyword arguments" kisaltmasidir.

### Yildizlar ne ise yariyor?

Yildizlarin Python'da iki temel kullanimi var:

1. Fonksiyon taniminda toplamak.
2. Fonksiyon cagrilarinda acmak.

Bu ikisi birbirine ters hareket gibi dusunulebilir.

### Fonksiyon taniminda `*`: positional argument'lari toplar

```python
def f(*args):
    print(args)


f(1, 2, 3)
```

Burada `*args`, gelen positional argument'lari toplar:

```text
(1, 2, 3)
```

### Fonksiyon taniminda `**`: keyword argument'lari toplar

```python
def f(**kwargs):
    print(kwargs)


f(a=1, b=2)
```

Burada `**kwargs`, gelen keyword argument'lari toplar:

```text
{'a': 1, 'b': 2}
```

### Fonksiyon cagrilarinda `*`: iterable'i positional argument'lara acar

```python
def f(a, b, c):
    print(a, b, c)


values = [1, 2, 3]
f(*values)
```

Bu su anlama gelir:

```python
f(1, 2, 3)
```

Cikti:

```text
1 2 3
```

### Fonksiyon cagrilarinda `**`: dict'i keyword argument'lara acar

```python
def f(name, age):
    print(name, age)


data = {"name": "Ayhan", "age": 25}
f(**data)
```

Bu su anlama gelir:

```python
f(name="Ayhan", age=25)
```

Cikti:

```text
Ayhan 25
```

### Yildizlar `args` ve `kwargs` isimlerini ozel keyword mu yapiyor?

Hayir.

`args` ve `kwargs` kelimeleri ozel keyword degildir.

Asil ozel olan:

- `*`
- `**`

isaretleridir.

Yani bunlar ayni mantikla calisir:

```python
def f(*args, **kwargs):
    print(args)
    print(kwargs)
```

```python
def f(*positional_values, **named_values):
    print(positional_values)
    print(named_values)
```

Ama standart, okunabilir ve beklenen isimlendirme `args` ve `kwargs` oldugu icin projelerde genellikle bunlar kullanilir.

### C dilindeki pointer ile alakasi var mi?

Hayir. Python'daki `*args` ve `**kwargs` C dilindeki pointer mantigiyla ilgili degildir.

C'de `*` isareti pointer dereference veya pointer declaration icin kullanilabilir:

```c
int *p;
```

Python'da fonksiyon argumanlarindaki `*` ve `**`:

- arguman toplama,
- arguman acma,
- keyword-only ayrimi

gibi anlamlara gelir.

Yani gorsel olarak ayni sembol kullaniliyor ama anlamlari farklidir.

### Positional argument ve keyword argument nedir?

Python'da fonksiyona verilen argumanlar kabaca ikiye ayrilir:

1. Positional argument
2. Keyword argument

Positional argument, siraya gore verilen argumandir:

```python
f(1, 42, 360)
```

Burada isim yoktur. Degerler sirayla gider.

Keyword argument, isimle verilen argumandir:

```python
f(toto="mean")
```

Burada `toto` keyword argument'in ismidir, `"mean"` degeridir.

### `=` veya `:` isaretine gore mi paylasiliyor?

Fonksiyon cagrilarinda keyword argument yazarken `=` kullanilir:

```python
ft_statistics(1, 42, toto="mean")
```

Burada:

- `1`, `42` positional argument'tir.
- `toto="mean"` keyword argument'tir.

`:` isareti fonksiyon cagrilarinda keyword argument icin kullanilmaz. `:` daha cok dict literal icinde kullanilir:

```python
data = {"toto": "mean"}
```

Yani:

```python
ft_statistics(toto: "mean")
```

gecerli bir fonksiyon cagrisi degildir.

Ex00 icin:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean")
```

fonksiyon tanimi suysa:

```python
def ft_statistics(*args, **kwargs):
    ...
```

Python bunu soyle ayirir:

```python
args = (1, 42, 360, 11, 64)
kwargs = {"toto": "mean"}
```

Buradaki ayrim, fonksiyon cagrisi yaziminda degerin isimle verilip verilmemesine gore yapilir.

### Once `toto="mean"` sonra sayilari yazarsak ne olur?

Su cagri gecersizdir:

```python
ft_statistics(toto="mean", 1, 42, 360, 11, 64)
```

Python bunu daha calistirmadan syntax error verir.

Sebep: Python'da normal yazimda positional argument'lar keyword argument'lardan once gelmelidir.

Yani bu dogru:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean")
```

Bu yanlis:

```python
ft_statistics(toto="mean", 1, 42, 360, 11, 64)
```

Alabilecegin hata su tarz olur:

```text
SyntaxError: positional argument follows keyword argument
```

Yani Python diyor ki:

> Keyword argument yazmaya basladiktan sonra tekrar normal positional argument yazamazsin.

### Neden positional argument'lar once gelmek zorunda?

Cunku positional argument'lar siraya gore yerlestirilir. Keyword argument'lar ise isimle yerlestirilir.

Ornek:

```python
def person(name, age, city):
    print(name, age, city)
```

Su net ve dogrudur:

```python
person("Ayhan", 25, city="Istanbul")
```

Python bunu soyle anlar:

```text
name = "Ayhan"
age = 25
city = "Istanbul"
```

Ama su karisik olur:

```python
person(city="Istanbul", "Ayhan", 25)
```

Python buna izin vermez. Cunku keyword argument yazildiktan sonra siraya dayali arguman vermeye devam etmek okunabilirligi ve kurali bozar.

### Ex00'da `*args` ve `**kwargs` tam olarak nasil paylasiyor?

Fonksiyon:

```python
def ft_statistics(*args, **kwargs):
    print(args)
    print(kwargs)
```

Cagri:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median")
```

Sonuc:

```python
args = (1, 42, 360, 11, 64)
kwargs = {"toto": "mean", "tutu": "median"}
```

Burada `*args` sayilari yakalar, cunku onlar positional argument'tir.

`**kwargs` ise `toto="mean"` ve `tutu="median"` kisimlarini yakalar, cunku onlar keyword argument'tir.

### Keyword argument her zaman string key mi olur?

Direkt fonksiyon cagrisi yazarken:

```python
f(toto="mean")
```

`kwargs` icindeki key string olur:

```python
{"toto": "mean"}
```

Ama su yazimda key zaten identifier olmak zorundadir:

```python
f(123="mean")
```

Bu gecersizdir.

Eger `**` ile dict aciyorsan, key'lerin string olmasi gerekir:

```python
data = {"toto": "mean"}
f(**data)
```

Bu calisir.

Ama:

```python
data = {123: "mean"}
f(**data)
```

bu hata verir, cunku keyword isimleri string olmak zorundadir.

## 2. Inner/outer yapisi generator mantigiyla ayni mi?

### Benzer taraflari var

Evet, ex01'deki inner/outer yapisi ile generator arasinda sezgisel bir benzerlik var.

Ikisi de:

- bir durumu hatirlayabilir,
- her cagrida yeni bir sonuc uretebilir,
- bir onceki adima bagli davranabilir,
- disaridan bakinca "cagirdikca ilerliyor" gibi gorunebilir.

Ex01:

```python
my_counter = outer(3, square)

print(my_counter())  # 9
print(my_counter())  # 81
print(my_counter())  # 6561
```

Bu, generator gibi "her cagrida siradaki degeri veriyor" hissi verir.

Ama teknik olarak generator degildir.

### En onemli fark: generator `yield` ile calisir

Generator fonksiyon soyle yazilir:

```python
def gen():
    yield 1
    yield 2
    yield 3
```

Bunu kullanmak icin:

```python
g = gen()
print(next(g))
print(next(g))
print(next(g))
```

Cikti:

```text
1
2
3
```

Generator fonksiyon cagrildiginda normal sonucu hemen dondurmez. Bir generator object dondurur.

### Closure ise normal fonksiyon dondurur

Ex01'deki mantik:

```python
def outer(x, function):
    def inner():
        ...

    return inner
```

Burada `outer`, bir fonksiyon dondurur.

Kullanim:

```python
my_counter = outer(3, square)
my_counter()
```

Yani `my_counter` normal cagrilabilir bir fonksiyondur.

### Generator ve closure arasindaki temel farklar

Generator:

- `yield` kullanir.
- `next()` ile ilerletilir.
- `for` dongusuyle gezilebilir.
- Iterator protokolune uyar.
- Bir noktada bitebilir ve `StopIteration` olusturur.
- Fonksiyonun calismasi `yield` satirinda durur, sonra oradan devam eder.

Closure:

- `yield` kullanmak zorunda degildir.
- Normal fonksiyon gibi `()` ile cagrilir.
- Icindeki degiskenleri hatirlayabilir.
- Bitmek zorunda degildir.
- Iterator protokolune uymak zorunda degildir.
- Her cagri bastan baslar ama closure'daki saklanan degiskenler eski degerini korur.

### "Her cagrida siradaki degeri vermek" generator olmak icin yeterli mi?

Hayir.

Bir seyin her cagrida yeni deger vermesi onu generator yapmaz.

Ornek closure:

```python
def make_counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

Bu generator degildir. Cunku `yield` yok, `next(c)` kullanilmaz.

Ornek generator:

```python
def make_counter():
    count = 0
    while True:
        count += 1
        yield count


c = make_counter()
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
```

Bu generator'dur.

### Ex01 generator ile yazilabilir miydi?

Teorik olarak benzer davranisi generator ile kurabilirsin. Ama subject'in prototipi bunu istemiyor.

Subject:

```python
my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
```

Eger generator olsaydi tester muhtemelen soyle olurdu:

```python
my_counter = outer(3, square)
print(next(my_counter))
print(next(my_counter))
print(next(my_counter))
```

Subject `my_counter()` diyor. Yani `outer`, cagrilabilir bir fonksiyon dondurmeli.

### Ex01'in amaci ne?

Ex01'in asil amaci:

- fonksiyonu arguman olarak almak,
- inner function dondurmek,
- closure ile state saklamak,
- `global` kullanmadan degerin son halini korumak,
- `nonlocal` mantigini kullanmak.

Generator konusu degil.

## 3. `nonlocal`, `global`, scope ve closure'in hafizasi

### `nonlocal` tam olarak ne yapar?

`nonlocal`, inner fonksiyon icinde bir degiskene atama yaparken, bu degiskenin local degil dis fonksiyon scope'undaki degisken oldugunu soyler.

Ornek:

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 1
        return x

    return inner
```

Burada `inner` icindeki:

```python
nonlocal x
```

su anlama gelir:

> Bu `x`, `inner` fonksiyonunun kendi local degiskeni degil. En yakin enclosing function scope'ta bulunan `x` degiskenidir.

Yani `x = x + 1` satiri, `outer` icindeki `x` degerini gunceller.

### `nonlocal` "hangi tarzda degistirecegini" mi beyan eder?

Evet, soyle dusunebilirsin:

`nonlocal x`, Python'a sunu beyan eder:

> Bu fonksiyon icinde `x` ismine atama yapacagim. Ama yeni bir local `x` olusturmak istemiyorum. Dis fonksiyonun scope'undaki `x`'i kullanip guncellemek istiyorum.

Bu, degiskenin nereden bulunacagini belirler.

Yani:

- degerin turunu belirlemez,
- nasil artirilacagini belirlemez,
- sadece isim cozme/scope kuralini belirler.

### `nonlocal` olmazsa ne olur?

Su kod hata verir:

```python
def outer():
    x = 10

    def inner():
        x = x + 1
        return x

    return inner


f = outer()
print(f())
```

Hata:

```text
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```

Neden?

Python bir fonksiyon icinde bir degiskene atama yapildigini gorurse, varsayilan olarak onu local degisken sayar.

Yani `inner` icindeki:

```python
x = x + 1
```

satirini gorunce Python der ki:

> Bu fonksiyon icinde `x`'e atama var, o zaman `x` local degiskendir.

Ama ayni satirda once sag tarafta `x` okunuyor:

```python
x + 1
```

Python local `x`'i okumaya calisir. Fakat local `x` daha olusmamistir. Bu yuzden hata gelir.

`nonlocal x` yazinca Python dis scope'taki `x`'i kullanir.

### Sadece okumak icin `nonlocal` gerekir mi?

Hayir.

Sadece okumak istiyorsan gerekmez:

```python
def outer():
    x = 10

    def inner():
        return x + 1

    return inner
```

Bu calisir. Cunku `inner`, `x`'e atama yapmiyor, sadece okuyor.

Ama atama varsa:

```python
x = x + 1
```

`nonlocal` gerekir.

### `global` ile farki ne?

`global`, module seviyesindeki degiskeni kullanacagini soyler.

Ornek:

```python
x = 10


def f():
    global x
    x = x + 1
    return x
```

Burada `x`, herhangi bir outer fonksiyonun degiskeni degil, dosya/module seviyesindeki `x`'tir.

`nonlocal` ise module seviyesini degil, en yakin dis fonksiyon scope'unu hedefler.

Ornek:

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 1
        return x

    return inner
```

Burada `x`, module seviyesinde degil, `outer` fonksiyonu icindedir.

Kisa fark:

```text
local     = fonksiyonun kendi ici
nonlocal  = dis fonksiyonun ici
global    = dosya/module seviyesi
```

### `nonlocal` benzeri baska kelimeler var mi?

Scope ile ilgili en yakin anahtar kelimeler:

- `global`
- `nonlocal`

Bunlarin gorevleri farklidir.

`global`:

```python
count = 0


def f():
    global count
    count += 1
```

`nonlocal`:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    return inner
```

Bu projede global variable yasak oldugu icin `global` kullanmamak gerekir. Ex01 ve ex02'de dogru yol `nonlocal` kullanmaktir.

### Inner'in outer'daki degiskenin son durumunu hatirlamasini saglayan sey ne?

Bunu saglayan mekanizmaya closure denir.

Python'da bir inner fonksiyon, dis fonksiyondaki bir degiskene referans veriyorsa, Python o degiskeni fonksiyonla birlikte saklar.

Ornek:

```python
def outer():
    x = 10

    def inner():
        return x

    return inner


f = outer()
print(f())
```

Normalde `outer()` calisip bitmistir. Ama `inner`, `x` degiskenini kullandigi icin Python `x`'i yok etmez. `inner` fonksiyonunun closure'i icinde saklar.

Bu yuzden:

```python
f = outer()
```

dedikten sonra `f`, sadece fonksiyon kodunu degil, ihtiyac duydugu dis degiskenleri de beraberinde tasir.

### Outer'in scope'u bitmiyor mu?

Outer fonksiyonun normal calismasi biter. Yani `outer()` cagrisi tamamlanir ve `return inner` yapar.

Ama `outer` icindeki tum local degiskenler otomatik olarak yok olmak zorunda degildir.

Eger bir inner fonksiyon bu degiskenlere referans veriyorsa, Python bu degiskenleri closure hucrelerinde saklar.

Yani daha dogru ifade su:

> Outer fonksiyonun calismasi biter, ama inner fonksiyonun ihtiyac duydugu dis degiskenler closure olarak yasamaya devam eder.

Scope "hic bitmiyor" demek biraz kaba olur. Fonksiyon cagrisi biter, stack frame normal anlamda kapanir; fakat gerekli degiskenler closure icinde tutulur.

### Neden tekrar `x = 10` olmuyor?

Cunku `x = 10` satiri sadece `outer()` cagrildiginda calisir.

Ornek:

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1
        return x

    return inner


f = outer()
print(f())  # 11
print(f())  # 12
print(f())  # 13
```

Burada `outer()` sadece bir kere cagrildi. Bu yuzden `x = 10` sadece bir kere olustu.

Sonraki cagrilar:

```python
f()
```

aslinda `inner()` cagrilaridir. `outer()` tekrar cagrilmiyor. Bu yuzden `x` tekrar 10'a donmuyor.

Ama soyle yaparsan:

```python
f1 = outer()
f2 = outer()

print(f1())  # 11
print(f1())  # 12
print(f2())  # 11
print(f2())  # 12
```

Burada iki farkli closure olusur. `f1` kendi `x`'ini, `f2` kendi `x`'ini saklar.

### Closure'in icinde ne var, gormek mumkun mu?

Evet, Python'da teknik olarak bakabilirsin:

```python
def outer():
    x = 10

    def inner():
        return x

    return inner


f = outer()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
```

Cikti benzeri:

```text
(<cell at 0x...: int object at 0x...>,)
10
```

Bu, `inner` fonksiyonunun disaridan bir degeri closure olarak sakladigini gosterir.

Gundelik kodda `__closure__` kullanman gerekmez. Ama mekanizmayi anlamak icin faydalidir.

## 4. Ex00'da key uydurmak normal mi, daha sik bir yol yok mu?

### Normal uygulamada boyle tasarim cok sik degil

Ex00'daki kullanim:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
```

gercek projelerde cok sik tercih edilecek bir API tasarimi degildir.

Cunku `toto`, `tutu`, `tata` gibi key'ler anlamsizdir. Fonksiyonun asil ilgilendigi sey key degil, value'dur:

```python
"mean"
"median"
"quartile"
```

Bu tasarim, okunabilirlik acisindan zayiftir.

### Daha sik bir tasarim nasil olurdu?

Gercek bir projede sunlardan biri daha okunabilir olurdu.

#### Secenek 1: Istenen islemleri liste olarak vermek

```python
ft_statistics([1, 42, 360, 11, 64], ["mean", "median", "quartile"])
```

Fonksiyon:

```python
def ft_statistics(values, operations):
    ...
```

Bu daha nettir:

- ilk parametre veri,
- ikinci parametre istenen islemler.

#### Secenek 2: Veri positional, islemler keyword olarak anlamli isimlerle

```python
ft_statistics(1, 42, 360, 11, 64, mean=True, median=True, quartile=True)
```

Burada key'ler anlamlidir.

Fonksiyon:

```python
def ft_statistics(*values, mean=False, median=False, quartile=False):
    ...
```

Bu da okunaklidir.

#### Secenek 3: Tek tek boolean parametreler

```python
ft_statistics(
    values=[1, 42, 360, 11, 64],
    mean=True,
    median=True,
    quartile=True,
)
```

Bu daha profesyonel bir API gibi durur.

#### Secenek 4: Enum veya sabitler

Daha buyuk projelerde:

```python
ft_statistics(values, operations={MEAN, MEDIAN, QUARTILE})
```

gibi daha kontrollu yapilar kurulabilir.

### Peki subject neden boyle istemis?

Evet, buyuk ihtimalle asil sebep `*args` ve `**kwargs` yapisini ogretmek.

Subject'in bilerek soyle bir tester vermesi:

```python
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
```

sana sunu ogretmek istiyor:

- `*args` gelen sayilari toplar.
- `**kwargs` gelen isimli istekleri toplar.
- Keyword isimleri her zaman anlamli olmak zorunda degildir.
- Fonksiyon bazen key'e degil value'ya bakabilir.
- `kwargs.values()` kullanman gerekebilir.

Yani egzersiz gercek dunya API guzelliginden cok, Python arguman mekanigini ogretmeye odaklaniyor.

### "Key uydurmak zorunda kalmak" neden rahatsiz hissettiriyor?

Cunku normalde dictionary'de key'ler anlam tasir.

Ornek:

```python
person = {
    "name": "Ayhan",
    "age": 25,
}
```

Burada key'ler anlamlidir.

Ama ex00'da:

```python
{
    "toto": "mean",
    "tutu": "median",
}
```

`toto` ve `tutu` anlamsizdir. Asil anlam value'dadir.

Bu normal yazilim tasariminda cok guzel degildir. Ama egzersiz, `kwargs`'in key-value yapisini gostermek icin bu tarz bir tester kullanmis.

## 5. Quartile hazir fonksiyonlari, izin durumu ve Tukey's method

### Quartile hesaplamanin hazir fonksiyonu var mi?

Evet, Python ekosisteminde quartile/percentile hesaplamak icin hazir yollar var.

Ornekler:

- `numpy.percentile`
- `numpy.quantile`
- `statistics.quantiles`

Ornek NumPy:

```python
import numpy as np

values = [1, 11, 42, 64, 360]
print(np.percentile(values, [25, 75]))
```

Ornek Python `statistics`:

```python
import statistics

values = [1, 11, 42, 64, 360]
print(statistics.quantiles(values))
```

Ama bu proje icin mesele sadece "hazir fonksiyon var mi?" degil, subject'in izin verip vermedigi ve expected output'a uyup uymadigidir.

### Subject'e gore hazir fonksiyon kullanmaya izin var mi?

Ex00'da subject soyle diyor:

```text
Allowed functions : None
```

Bu nedenle ex00 icin hazir istatistik fonksiyonlarini kullanmak risklidir.

Ozellikle:

- `statistics.mean`
- `statistics.median`
- `statistics.quantiles`
- `numpy.percentile`
- `numpy.quantile`

gibi fonksiyonlari kullanmak subject ruhuna uygun degildir.

Ayrica dosyanin adi zaten:

```text
statistics.py
```

oldugu icin Python'un kendi `statistics` moduluyle isim cakismasi da olabilir.

En guvenli yol:

- sort islemini kendin yapmak,
- mean'i kendin hesaplamak,
- median'i kendin hesaplamak,
- quartile'i expected output'a uyacak sekilde kendin hesaplamak,
- variance ve std'yi kendin hesaplamak.

### Built-in `sorted` kullanmak uygun mu?

Subject'te "Allowed functions: None" yazdigi icin cok kati yorumda hazir fonksiyon kullanmamak gerekir denebilir. Ama 42 Python piscine egzersizlerinde pratikte bu ifade genellikle "ozel dis fonksiyon/lib kullanma" anlaminda degerlendirilebiliyor.

Yine de en guvenli yorum:

- Hazir istatistik hesaplayan fonksiyon kullanma.
- Basit Python built-in'lerini abartmadan kullan.

Eger tamamen risksiz gitmek istersen, siralamayi bile kendin yazabilirsin. Ama cogu degerlendirmede `sorted` kullanimi problem edilmez. Burada kampus/evaluator yorumu fark edebilir.

### Neden farkli quartile yontemleri var?

Quartile, veriyi dort parcaya bolme fikridir. Ama ozellikle veri sayisi azsa "25% noktasi"nin tam olarak hangi elemana veya hangi ara degere denk geldigi konusunda farkli istatistiksel yontemler vardir.

Ornek veri:

```text
1, 11, 42, 64, 360
```

Farkli yontemler su tarz sonuclar verebilir:

- `[11.0, 64.0]`
- `[6.0, 212.0]`
- `[11.0, 64.0]` ama farkli ara mantikla
- interpolasyonlu baska degerler

Bu yuzden subject'in expected output'u hangi yontemi ima ediyor ona bakmak gerekir.

### Subject hangi davranisi bekliyor?

Subject'in verisi:

```python
1, 42, 360, 11, 64
```

Siralaninca:

```python
[1, 11, 42, 64, 360]
```

Beklenen:

```python
[11.0, 64.0]
```

Bu beklenen cikti, su basit indeks mantigiyla uyumludur:

```python
q1 = values[int(len(values) * 0.25)]
q3 = values[int(len(values) * 0.75)]
```

5 elemanda:

```text
int(5 * 0.25) = 1 -> values[1] = 11
int(5 * 0.75) = 3 -> values[3] = 64
```

Sonuc:

```python
[11.0, 64.0]
```

### Tukey's method kullandim, uygun mu?

Bu sorunun cevabi kullandigin Tukey yorumuna ve kodunun diger testlerde ne uretecegine bagli.

Tukey's hinges yonteminde genel fikir:

- veri siralanir,
- alt yari ve ust yari ayrilir,
- bu yarilarin median'lari Q1 ve Q3 olur.

Tek sayida eleman varsa ortadaki elemanin yarilara dahil edilip edilmeyecegi farkli yorumlarda degisebilir.

Veri:

```python
[1, 11, 42, 64, 360]
```

Ortadaki eleman:

```python
42
```

Ortadaki elemani disarida birakirsan:

```python
lower = [1, 11]
upper = [64, 360]
```

Q1:

```text
(1 + 11) / 2 = 6
```

Q3:

```text
(64 + 360) / 2 = 212
```

Bu subject'e uymaz.

Ortadaki elemani iki yariya da dahil edersen:

```python
lower = [1, 11, 42]
upper = [42, 64, 360]
```

Q1:

```text
11
```

Q3:

```text
64
```

Bu subject'e uyar.

Yani "Tukey's method kullandim" tek basina yeterli cevap degil. Hangi varyanti kullandigin onemli.

### En guvenli cevap ne?

Bu subject icin en guvenli davranis expected output'a birebir uyan basit indeks yontemidir:

```python
values = sorted(args)
q1 = float(values[int(len(values) * 0.25)])
q3 = float(values[int(len(values) * 0.75)])
```

Bu yontem subject ornegiyle net uyumlu.

Eger Tukey varyantin:

```text
[1, 11, 42, 64, 360] -> [11.0, 64.0]
```

uretiyorsa ilk tester'i gecer. Ama gizli testlerde subject'in bekledigi yontem basit indeks ise, Tukey bazi veri uzunluklarinda farkli sonuc verebilir.

Bu yuzden ben subject uyumu icin basit indeks yontemini oneririm.

### Hazir fonksiyon kullanmak neden riskli?

Hazir fonksiyonlar farkli default yontemler kullanabilir.

Ornegin NumPy'nin percentile/quantile fonksiyonlari interpolation/method ayarlarina gore farkli sonuc verebilir.

Senin amacin bu egzersizde istatistik teorisindeki en akademik yontemi secmek degil; subject'in expected output'una uyan davranisi yazmak.

## 6. Ex01'de verilen `outer` fonksiyonundaki `count = 0` ne ise yarayacak?

### Subject prototipi neden `count = 0` koymus?

Subject ex01 icin su prototipi veriyor:

```python
def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        # your code here
```

Ama expected output'a bakinca asil gereken sey, her cagrida son sonucu hatirlamak.

Ornek:

```python
my_counter = outer(3, square)
print(my_counter())  # 9
print(my_counter())  # 81
print(my_counter())  # 6561
```

Burada `count = 0` dogrudan ciktiyi hesaplamak icin zorunlu gorunmuyor.

### `count` cagri sayisini tutmak icin konmus olabilir

`count`, normalde sunu takip etmek icin kullanilabilir:

```text
inner kac defa cagrildi?
```

Ornek:

```python
def outer(x, function):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("call number:", count)
        return function(x)

    return inner
```

Ama subject'in beklenen ciktisinda cagri sayisi yazdirilmiyor.

Bu yuzden `count` ya:

- egzersizin closure mantigini gostermek icin konmus bir ipucu,
- ya da subject yazarinin gereksiz birakmis oldugu bir degisken,
- ya da `x` yerine sonucu `count` uzerinden saklamani bekleyen ama prototipte net olmayan bir yonlendirme olabilir.

### Expected output icin `count` gerekli mi?

Hayir, expected output'u uretmek icin `count` gerekli degil.

Su mantik yeterlidir:

```python
def outer(x, function):
    result = x

    def inner():
        nonlocal result
        result = function(result)
        return result

    return inner
```

Bu:

```python
my_counter = outer(3, square)
print(my_counter())  # 9
print(my_counter())  # 81
print(my_counter())  # 6561
```

uretir.

### Peki subject `count = 0` verdiyse silmek sorun olur mu?

42 subject'lerinde verilen prototipe cok yakin kalmak genelde iyidir. Ama kullanilmayan degisken `flake8` tarafindan sorun olarak gorulebilir:

```text
F841 local variable 'count' is assigned to but never used
```

Bu yuzden `count = 0` satirini aynen birakip kullanmazsan norm hatasi alabilirsin.

Iki secenek var:

1. `count` kullanmadan daha temiz cozum yazmak.
2. `count`'u gercekten kullanmak ama ciktiyi bozmamak.

### `count` kullanarak ama ciktiyi bozmadan nasil yazilabilir?

`count`, cagri sayisini tutabilir; asil sonuc ayri bir degiskende tutulur:

```python
def outer(x, function):
    count = 0
    result = x

    def inner():
        nonlocal count
        nonlocal result
        count += 1
        result = function(result)
        return result

    return inner
```

Bu kodda:

- `count` inner'in kac defa cagrildigini tutar,
- `result` son sonucu tutar,
- sadece `result` return edilir,
- `count` yazdirilmaz.

Ama burada `count` yine subject ciktisi icin gerekli degildir; sadece prototipteki degiskeni anlamli sekilde kullanmis olursun.

### Daha sade cozum hangisi?

Benim gozumde expected output icin en sade ve dogru fikir:

```python
def outer(x, function):
    result = x

    def inner():
        nonlocal result
        result = function(result)
        return result

    return inner
```

Ama subject prototipine yakin durmak istersen:

```python
def outer(x, function):
    count = 0
    result = x

    def inner():
        nonlocal count
        nonlocal result
        count += 1
        result = function(result)
        return result

    return inner
```

Bu da calisir.

### `count` ile sadece sayi uzerinden cozum yapilabilir mi?

Bu egzersizde asil hesap onceki sonuca dayandigi icin `count` tek basina yetmez.

Mesela:

```python
my_counter = outer(3, square)
```

Sonuclar:

```text
9
81
6561
```

Bu dizi, sadece cagri sayisindan degil, onceki sonuctan gelir.

Yani bilmen gereken ana state:

```text
son sonuc
```

`count` sadece yardimci bilgi olabilir:

```text
kac kere cagrildi
```

### Kisa cevap

Ex01'deki `count = 0`, expected output icin zorunlu degil. Muhtemelen closure ve state saklama fikrine ipucu olarak konmus. Asil gerekli olan, `x` veya `result` gibi bir degiskenin son sonucunu closure icinde saklamak ve her `inner()` cagrildiginda onu guncellemektir.

