# Python Iterable ve Veri Yapıları Çalışma Notu

Bu dosya, Python'da sık göreceğin şu yapıları birlikte çalışmak için hazırlandı:

- `list`
- `tuple`
- `string`
- `set`
- `dict`
- `range`
- `file object`
- `generator`
- `csv.reader`
- `enumerate`
- `zip`

Amaç sadece bunların ne olduğunu söylemek değil. Şunları da netleştireceğiz:

- Hangisi gerçek bir veri yapısı, hangisi daha çok bir iterator/yardımcı yapı
- Hangisi değiştirilebilir, hangisi değiştirilemez
- Hangisinde sıra vardır, hangisinde yoktur
- Hangisi indekslenebilir
- Hangisi iterable'dır
- `for ... in ...`, `list(...)`, `comprehension`, `next(...)` gibi kullanımlar bu yapılarda nasıl çalışır

## 1. Önce Temel Kavramlar

Bu kavramlar netleşmeden aşağıdaki yapıların davranışını tam anlamak zor olur.

### 1.1 Iterable nedir?

**Iterable**, üzerinde sırayla dolaşabildiğin yapıdır.

Örnek:

```python
numbers = [10, 20, 30]

for n in numbers:
    print(n)
```

Burada `numbers` bir iterable'dır.

Python'da şunlar iterable olabilir:

- list
- tuple
- string
- set
- dict
- range
- file object
- generator
- `csv.reader`
- `enumerate`
- `zip`

Yani ortak nokta şudur:

```python
for item in x:
    ...
```

yazabiliyorsan `x` büyük ihtimalle iterable'dır.

### 1.2 Iterator nedir?

**Iterator**, elemanları birer birer veren yapıdır.

En tipik özellik:

```python
next(iterator)
```

ile bir sonraki elemanı alabilmendir.

Örnek:

```python
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

Elemanlar bitince:

```python
StopIteration
```

hatası oluşur.

### 1.3 Iterable ile iterator farkı

Çok önemli ayrım:

- Her iterator iterable'dır.
- Ama her iterable doğrudan iterator değildir.

Örnek:

```python
numbers = [10, 20, 30]
print(type(numbers))
# <class 'list'>

it = iter(numbers)
print(type(it))
# <class 'list_iterator'>
```

Yani:

- `list` bir veri yapısıdır
- `iter(list)` sonucu iterator'dır

### 1.4 Mutable / immutable

Python'da bazı yapılar değiştirilebilir, bazıları değiştirilemez.

**Mutable**: sonradan değiştirilebilir

- `list`
- `set`
- `dict`

**Immutable**: oluşturulduktan sonra içeriği doğrudan değiştirilemez

- `tuple`
- `string`
- `range`

Not:

- `generator`, `enumerate`, `zip`, `csv.reader`, `file object` klasik anlamda veri deposu değil; bunlar daha çok akış/iterator nesneleridir.

### 1.5 Sıra, indeks ve tekrar

Bir yapıyı tanırken şu üç soruyu sor:

1. Eleman sırası önemli mi?
2. İndeks ile erişebilir miyim?
3. Aynı eleman birden fazla kez bulunabilir mi?

Bu sorular aşağıda her yapı için tek tek açıklanacak.

## 2. `list`

### 2.1 Nedir?

`list`, Python'da en temel veri yapılarından biridir.

Örnek:

```python
numbers = [10, 20, 30]
names = ["ali", "ayse", "mehmet"]
mixed = [1, "hello", 3.14, True]
```

### 2.2 Özellikleri

- Sıralıdır
- İndekslenebilir
- Değiştirilebilir
- Tekrarlı eleman içerebilir
- Farklı türde elemanları birlikte tutabilir

Örnek:

```python
data = ["km", "price", "km"]

print(data[0])   # km
print(data[1])   # price
print(len(data)) # 3
```

### 2.3 Sık işlemler

```python
items = [1, 2, 3]

items.append(4)       # [1, 2, 3, 4]
items.insert(0, 99)   # [99, 1, 2, 3, 4]
items.pop()           # son elemanı çıkarır
items.remove(2)       # değeri 2 olan ilk elemanı siler
```

### 2.4 List comprehension

```python
squares = [x * x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

Filtreli:

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

### 2.5 Ne zaman kullanılır?

- Elemanlar üzerinde sık değişiklik yapılacaksa
- İndeksle erişmek istiyorsan
- Sıra önemliyse

## 3. `tuple`

### 3.1 Nedir?

`tuple`, listeye benzeyen ama değiştirilemeyen bir yapıdır.

Örnek:

```python
point = (10, 20)
person = ("Ali", 25, "Ankara")
```

### 3.2 Özellikleri

- Sıralıdır
- İndekslenebilir
- Değiştirilemez
- Tekrarlı eleman içerebilir

### 3.3 Örnek

```python
t = ("km", "price")
print(t[0])  # km
print(t[1])  # price
```

Şu geçersizdir:

```python
t[0] = "year"
```

Çünkü `tuple` immutable'dır.

### 3.4 Packing ve unpacking

Tuple'lar Python'da çok sık "birden fazla değeri birlikte taşımak" için kullanılır.

```python
pair = (10, 20)
x, y = pair

print(x)  # 10
print(y)  # 20
```

Bu yapı `enumerate` ve `zip` çıktılarında çok önemlidir.

### 3.5 Tuple oluşturma notu

Parantez çoğu zaman görünür ama asıl önemli olan virgüldür:

```python
t1 = (1, 2, 3)
t2 = 1, 2, 3
```

Tek elemanlı tuple için:

```python
single = (5,)
```

## 4. `string`

### 4.1 Nedir?

`string`, metin tutar.

```python
name = "Python"
```

### 4.2 Özellikleri

- Sıralıdır
- İndekslenebilir
- Değiştirilemez
- Karakterlerden oluşur

### 4.3 Çok önemli nokta

String iterable'dır. Yani karakter karakter dolaşılır:

```python
text = "abc"

for ch in text:
    print(ch)
```

çıktı:

```python
a
b
c
```

### 4.4 Comprehension ile ilişkisi

Şu kullanım:

```python
[ch for ch in "km,price"]
```

şu sonucu verir:

```python
['k', 'm', ',', 'p', 'r', 'i', 'c', 'e']
```

Yani string'i sütunlara bölmez, **karakterlerine ayırır**.

Virgüle göre bölmek için:

```python
"km,price".split(",")
```

çıktı:

```python
['km', 'price']
```

### 4.5 Sık metotlar

```python
text = "  Price  "

print(text.strip())   # "Price"
print(text.lower())   # "  price  "
print(text.upper())   # "  PRICE  "
print(text.split())   # ['Price']
```

### 4.6 String üretmek

String comprehension diye ayrı bir sözdizimi yoktur. Genelde `join` kullanılır:

```python
result = "".join(ch.upper() for ch in "abc")
print(result)  # ABC
```

## 5. `set`

### 5.1 Nedir?

`set`, benzersiz elemanlar kümesidir.

```python
values = {1, 2, 3}
```

### 5.2 Özellikleri

- Tekrarlı eleman tutmaz
- İndekslenemez
- Değiştirilebilir
- Matematiksel küme işlemleri için uygundur
- Sıra mantığına güvenilmez

### 5.3 Örnek

```python
s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}
```

### 5.4 Set comprehension

```python
result = {x * 2 for x in [1, 2, 2, 3]}
print(result)  # {2, 4, 6}
```

### 5.5 Sık işlemler

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # birleşim
print(a & b)  # kesişim
print(a - b)  # fark
```

### 5.6 Ne zaman kullanılır?

- Tekrarları kaldırmak için
- Üyelik kontrolü için
- Küme işlemleri için

## 6. `dict`

### 6.1 Nedir?

`dict`, anahtar-değer eşleşmesi tutar.

```python
car = {
    "km": 120000,
    "price": 5000
}
```

### 6.2 Özellikleri

- Anahtar-değer yapısıdır
- Anahtar ile erişilir
- Değiştirilebilir
- Anahtarlar benzersizdir
- Modern Python'da ekleme sırası korunur

### 6.3 Erişim

```python
print(car["km"])     # 120000
print(car["price"])  # 5000
```

### 6.4 Dict üzerinde dolaşma

Doğrudan dict üzerinde dolaşırsan anahtarlar gelir:

```python
car = {"km": 120000, "price": 5000}

for key in car:
    print(key)
```

çıktı:

```python
km
price
```

Değerleri almak için:

```python
for value in car.values():
    print(value)
```

Hem anahtar hem değer için:

```python
for key, value in car.items():
    print(key, value)
```

### 6.5 Dict comprehension

```python
squares = {x: x * x for x in range(5)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 6.6 Set ile dict karışıklığı

```python
{1, 2, 3}          # set
{"a": 1, "b": 2}   # dict
```

Ayırt eden şey `:` kullanımıdır.

## 7. `range`

### 7.1 Nedir?

`range`, belirli bir sayı aralığını temsil eder.

```python
r = range(5)
```

### 7.2 Özellikleri

- Iterable'dır
- Tembel davranır; tüm sayıları baştan liste olarak üretmez
- İndekslenebilir
- Immutable kabul edilir

### 7.3 Örnek

```python
print(range(5))        # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
```

### 7.4 Kullanımlar

```python
for i in range(3):
    print(i)
```

çıktı:

```python
0
1
2
```

Adım verilebilir:

```python
list(range(2, 10, 2))
# [2, 4, 6, 8]
```

## 8. `file object`

### 8.1 Nedir?

Dosyayı `open(...)` ile açınca bir **file object** elde edersin.

```python
f = open("data.csv", "r")
```

Bu nesne dosyayı okumak/yazmak için kullanılır.

### 8.2 Özellikleri

- Iterable olabilir
- Satır satır okunabilir
- İç durum taşır; okundukça ileri gider

### 8.3 Örnek

```python
with open("data.csv", "r") as file:
    for line in file:
        print(line)
```

Burada `file` iterable gibi davranır ve satır satır verir.

### 8.4 Önemli davranış

Bir kez okudukça dosya imleci ilerler.

```python
with open("data.csv", "r") as file:
    print(file.readline())
    print(file.readline())
```

İlk çağrı ilk satırı, ikinci çağrı ikinci satırı verir.

### 8.5 Sık metotlar

```python
file.read()       # tüm içerik
file.readline()   # tek satır
file.readlines()  # tüm satırlar liste olarak
```

## 9. `generator`

### 9.1 Nedir?

Generator, değerleri gerektiğinde üreten yapıdır.

Bellekte her şeyi bir anda tutmak zorunda değildir.

### 9.2 Generator expression

```python
g = (x * x for x in range(5))
print(g)
```

çıktı:

```python
<generator object ...>
```

Liste değildir. Tüketmek gerekir:

```python
print(next(g))   # 0
print(next(g))   # 1
print(list(g))   # [4, 9, 16]
```

### 9.3 `yield` ile generator fonksiyonu

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

Kullanım:

```python
g = count_up_to(3)
print(list(g))  # [1, 2, 3]
```

### 9.4 Özellikleri

- Iterator gibi davranır
- Bir kez tüketilince biter
- Büyük verilerde verimlidir

## 10. `csv.reader`

### 10.1 Nedir?

`csv.reader`, CSV dosyasını satır satır ve sütun sütun okuyan bir nesnedir.

```python
import csv

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
```

### 10.2 Özellikleri

- Iterable'dır
- Iterator gibi tüketilir
- Her turda bir satırı liste olarak verir

### 10.3 Örnek

Dosya:

```csv
km,price
120000,5000
150000,4200
```

Kod:

```python
import csv

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

çıktı:

```python
['km', 'price']
['120000', '5000']
['150000', '4200']
```

### 10.4 `reader` tipi

```python
print(type(reader))
# <class '_csv.reader'>
```

### 10.5 `list(reader)` ne yapar?

`reader` içindeki tüm satırları tüketip liste haline getirir:

```python
rows = list(reader)
```

sonuç:

```python
[
    ['km', 'price'],
    ['120000', '5000'],
    ['150000', '4200']
]
```

## 11. `enumerate`

### 11.1 Nedir?

`enumerate`, bir iterable'ın elemanlarını **indeks + eleman** şeklinde verir.

### 11.2 Örnek

```python
names = ["ali", "ayse", "mehmet"]

for item in enumerate(names):
    print(item)
```

çıktı:

```python
(0, 'ali')
(1, 'ayse')
(2, 'mehmet')
```

### 11.3 En sık kullanım

```python
for i, name in enumerate(names):
    print(i, name)
```

### 11.4 `start` parametresi

```python
for i, name in enumerate(names, start=1):
    print(i, name)
```

çıktı:

```python
1 ali
2 ayse
3 mehmet
```

### 11.5 Tipi

```python
e = enumerate(["a", "b"])
print(type(e))
```

çıktı:

```python
<class 'enumerate'>
```

### 11.6 Comprehension ile kullanım

```python
result = [f"{i}:{value}" for i, value in enumerate(["km", "price"], start=1)]
print(result)
# ['1:km', '2:price']
```

## 12. `zip`

### 12.1 Nedir?

`zip`, birden fazla iterable'ı birlikte dolaştırır.

### 12.2 Örnek

```python
keys = ["km", "price"]
values = [120000, 5000]

for pair in zip(keys, values):
    print(pair)
```

çıktı:

```python
('km', 120000)
('price', 5000)
```

### 12.3 En sık kullanım

```python
for key, value in zip(keys, values):
    print(key, value)
```

### 12.4 Dikkat

`zip`, en kısa iterable kadar gider.

```python
a = [1, 2, 3]
b = ["a", "b"]

print(list(zip(a, b)))
# [(1, 'a'), (2, 'b')]
```

### 12.5 Dict oluşturmak

```python
keys = ["km", "price"]
values = [120000, 5000]

d = dict(zip(keys, values))
print(d)
# {'km': 120000, 'price': 5000}
```

## 13. Comprehension Türleri

Burada en önemli yapı taşlarından biri budur.

### 13.1 List comprehension

Genel form:

```python
[ifade for eleman in iterable]
```

Örnek:

```python
[x * 2 for x in [1, 2, 3]]
# [2, 4, 6]
```

Filtreli:

```python
[x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

### 13.2 Set comprehension

```python
{x for x in [1, 2, 2, 3]}
# {1, 2, 3}
```

### 13.3 Dict comprehension

```python
{x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 13.4 Generator expression

```python
(x * x for x in range(5))
```

Bu comprehension'a çok benzer ama liste yerine generator üretir.

### 13.5 Çok önemli kural

Çıktı türünü çoğu zaman dıştaki yazım belirler:

```python
[x for x in data]        # list
{x for x in data}        # set
{x: x*x for x in data}   # dict
(x for x in data)        # generator
```

## 14. Comprehension Benzeri Diğer Kullanımlar

Comprehension tek modern kısa yazım biçimi değildir. Sık göreceğin diğer yapılar:

### 14.1 `list(...)`

Bir iterable'ı listeye çevirir:

```python
list(range(5))         # [0, 1, 2, 3, 4]
list("abc")            # ['a', 'b', 'c']
list(zip([1, 2], [3, 4]))  # [(1, 3), (2, 4)]
```

### 14.2 `tuple(...)`

```python
tuple([1, 2, 3])  # (1, 2, 3)
```

### 14.3 `set(...)`

```python
set([1, 2, 2, 3])  # {1, 2, 3}
```

### 14.4 `dict(...)`

```python
dict([("km", 120000), ("price", 5000)])
# {'km': 120000, 'price': 5000}
```

### 14.5 `map(...)`

Her elemana bir fonksiyon uygular:

```python
result = map(str.upper, ["km", "price"])
print(list(result))
# ['KM', 'PRICE']
```

### 14.6 `filter(...)`

Şarta uyan elemanları bırakır:

```python
result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(result))
# [2, 4]
```

Not:

- `map` ve `filter` Python 3'te iterator benzeri nesneler döndürür.
- Birçok durumda list comprehension daha okunabilir olur.

## 15. Aynı Veriden Farklı Çıktılar

Aynı iterable'dan farklı yapı türleri üretilebilir.

Örnek:

```python
data = ["km", "price", "km"]
```

Liste:

```python
[x for x in data]
# ['km', 'price', 'km']
```

Set:

```python
{x for x in data}
# {'km', 'price'}
```

Tuple:

```python
tuple(x for x in data)
# ('km', 'price', 'km')
```

Dict:

```python
{i: x for i, x in enumerate(data)}
# {0: 'km', 1: 'price', 2: 'km'}
```

String:

```python
",".join(x for x in data)
# 'km,price,km'
```

## 16. Sık Karışan Noktalar

### 16.1 String iterable'dır ama sütunlara bölünmez

```python
[x for x in "abc"]
# ['a', 'b', 'c']
```

### 16.2 `dict` üzerinde dolaşınca key gelir

```python
d = {"km": 120000, "price": 5000}
print([x for x in d])
# ['km', 'price']
```

### 16.3 `set` indekslenemez

```python
s = {1, 2, 3}
s[0]
```

Bu hata verir.

### 16.4 `generator` bir kez tüketilir

```python
g = (x for x in range(3))

print(list(g))  # [0, 1, 2]
print(list(g))  # []
```

### 16.5 `enumerate` indeks ve elemanı birlikte verir

```python
list(enumerate(["a", "b"]))
# [(0, 'a'), (1, 'b')]
```

### 16.6 `zip` en kısa iterable kadar çalışır

```python
list(zip([1, 2, 3], ["a"]))
# [(1, 'a')]
```

## 17. Hızlı Karşılaştırma Tablosu

| Yapı | Sıralı mı? | İndekslenir mi? | Mutable mı? | Tekrar kabul eder mi? | Tipik kullanım |
|---|---|---:|---:|---:|---|
| `list` | Evet | Evet | Evet | Evet | Genel amaçlı sıralı veri |
| `tuple` | Evet | Evet | Hayır | Evet | Sabit veri grubu |
| `string` | Evet | Evet | Hayır | Evet | Metin |
| `set` | Güvenilmez | Hayır | Evet | Hayır | Benzersiz elemanlar |
| `dict` | Evet | Anahtar ile | Evet | Anahtar tekrarı hayır | Anahtar-değer eşleşmesi |
| `range` | Evet | Evet | Hayır | Sayı aralığı | Döngü/sayı üretimi |
| `file object` | Satır sırasıyla | Doğrudan hayır | Akış nesnesi | Dosyaya bağlı | Dosya okuma/yazma |
| `generator` | Üretim sırasıyla | Hayır | Tüketilir | Üretime bağlı | Tembel üretim |
| `csv.reader` | Satır sırasıyla | Hayır | Tüketilir | Dosyaya bağlı | CSV satırları |
| `enumerate` | Evet | Hayır | Tüketilir | Girdiye bağlı | İndeks + eleman |
| `zip` | Evet | Hayır | Tüketilir | Girdiye bağlı | Paralel dolaşma |

## 18. Mini Pratikler

Bu kısmı kendin yazıp çalıştır.

### Pratik 1

```python
data = ["km", "price", "year"]
```

Şunları üret:

- aynı elemanlardan liste
- aynı elemanlardan set
- indeksleriyle dict
- büyük harfli yeni liste

### Pratik 2

```python
text = "km,price"
```

Şunların farkını incele:

```python
[x for x in text]
text.split(",")
list(text)
```

### Pratik 3

```python
names = ["ali", "ayse", "mehmet"]
ages = [20, 21, 22]
```

Şunları dene:

```python
list(enumerate(names))
list(zip(names, ages))
{name: age for name, age in zip(names, ages)}
```

### Pratik 4

Bir generator üret:

```python
g = (x * 10 for x in range(5))
```

Sonra:

```python
print(next(g))
print(next(g))
print(list(g))
print(list(g))
```

ve neden ikinci `list(g)` boş geliyor anlamaya çalış.

## 19. Kendine Soracağın Kontrol Soruları

Bir yapıyı görünce kendine şunları sor:

1. Bu iterable mı?
2. Bu iterator mı?
3. Bunun elemanları hangi sırayla gelir?
4. Buna indeksle erişebilir miyim?
5. Bu mutable mı?
6. Bunu `list(...)` yaparsam ne çıkar?
7. Bunun üstünde comprehension kullanırsam tek tek hangi elemanlar dolaşılır?

## 20. Çok Kısa Özet

- `list`, `tuple`, `string`, `set`, `dict` klasik veri yapılarıdır.
- `range` sayı aralığı temsil eder.
- `file object`, `generator`, `csv.reader`, `enumerate`, `zip` daha çok iterable/iterator tabanlı yapılardır.
- Comprehension yapılarında:

```python
[x for x in data]
```

sonuç her zaman `list` olur.

- Şunlar farklı türler üretir:

```python
[x for x in data]      # list
{x for x in data}      # set
{k: v for ...}         # dict
(x for x in data)      # generator
```

- Bir yapının üstünden "nasıl dolaşıldığı" çok önemlidir:
  - `string` -> karakter karakter
  - `dict` -> key key
  - `file` -> satır satır
  - `csv.reader` -> satır satır, her satır liste
  - `enumerate` -> `(index, value)`
  - `zip` -> paralel tuple'lar

## 21. Sonraki Çalışma Önerisi

Bu dosyayı bitirdikten sonra şu başlıklara geçebilirsin:

- slicing: `data[1:4]`
- shallow copy / deep copy
- `iter()` ve `next()`
- `*args` ve unpacking
- nested comprehension
- `map`, `filter`, `sorted`, `any`, `all`

