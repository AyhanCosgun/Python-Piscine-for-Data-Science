# Ex03 - Dataclass Açıklaması

Bu alıştırmada senden `ex03/new_student.py` içinde bir `Student` sınıfı yazman isteniyor. Subject'e göre bu sınıf bir **dataclass** olmalı.

Subject'in verdiği iskelet yaklaşık olarak şu:

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

Beklenen kullanım:

```python
from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
```

Beklenen çıktı:

```text
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
```

`id` random olduğu için her çalıştırmada farklı olabilir.

Subject ayrıca şunu istiyor:

```python
Student(name="Edward", surname="agle", id="toto")
```

Bu kullanım hata vermeli:

```text
TypeError: Student.__init__() got an unexpected keyword argument 'id'
```

Yani `id` ve `login` dışarıdan verilememeli. Bunlar sınıfın kendisi tarafından otomatik oluşturulmalı.

Bu alıştırma için mantıklı çözüm şuna benzer:

```python
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
```

## 1. Alıştırmanın Amacı ve Yöntemi

Alıştırmanın amacı, Python'daki `dataclass` yapısını kullanarak veri tutan bir sınıf yazmayı öğretmek.

Bu egzersizde elle klasik bir sınıf yazmak yerine:

```python
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.active = True
        ...
```

şeklinde uzun uzun `__init__` yazmıyorsun. Onun yerine:

```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
```

yazıyorsun. Python senin için otomatik olarak `__init__`, `__repr__`, `__eq__` gibi bazı metodları üretiyor.

Bu alıştırmada yapılması gerekenler:

- `Student` bir dataclass olacak.
- `name` ve `surname` dışarıdan alınacak.
- `active` otomatik olarak `True` olacak.
- `login` dışarıdan alınmayacak, `name[0] + surname` şeklinde üretilecek.
- `id` dışarıdan alınmayacak, `generate_id()` ile random üretilecek.
- Sınıf içinde `__str__` veya `__repr__` yazılmayacak.

Neden `__str__` ve `__repr__` yazılmıyor?

Çünkü dataclass zaten otomatik bir `__repr__` üretir. Subject'in beklediği çıktı da dataclass'ın otomatik `repr` formatıdır:

```text
Student(name='Edward', surname='agle', active=True, login='Eagle', id='...')
```

## 2. Dataclass Ne Demek?

`dataclass`, veri taşımak için kullanılan sınıfları daha az kodla yazmanı sağlayan bir Python yapısıdır.

Normalde şu sınıfı elle yazman gerekebilir:

```python
class Student:
    def __init__(self, name: str, surname: str, active: bool = True):
        self.name = name
        self.surname = surname
        self.active = active

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"surname={self.surname!r}, "
            f"active={self.active!r})"
        )
```

Dataclass ile bunu şöyle yazarsın:

```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
```

Python otomatik olarak buna benzer bir `__init__` oluşturur:

```python
def __init__(self, name: str, surname: str, active: bool = True):
    self.name = name
    self.surname = surname
    self.active = active
```

Ayrıca otomatik olarak anlamlı bir gösterim de verir:

```python
student = Student("Edward", "agle")
print(student)
```

Çıktı:

```text
Student(name='Edward', surname='agle', active=True)
```

Dataclass'ın bilmen gereken temel özellikleri:

- Alanlar type annotation ile yazılır: `name: str`.
- Default değer verilebilir: `active: bool = True`.
- Otomatik `__init__` üretir.
- Otomatik `__repr__` üretir.
- Varsayılan olarak `__eq__` üretir, yani iki dataclass nesnesini alanlarına göre karşılaştırabilir.
- `field()` ile alanların davranışı ayrıntılı şekilde ayarlanabilir.
- `__post_init__` ile otomatik `__init__` bittikten sonra ek işlem yapılabilir.

Dataclass kullanmanın avantajları:

- Daha az boilerplate kod yazarsın.
- Veri modeli daha okunaklı olur.
- Hangi alanların olduğu sınıfın başında açıkça görünür.
- `print(obj)` çıktısı otomatik olarak anlaşılır olur.
- `==` karşılaştırması çoğu durumda doğrudan işe yarar.
- Default değerler ve otomatik üretilen alanlar daha düzenli tanımlanır.

## 3. `field` Ne Demek?

`field`, dataclass alanlarının davranışını daha ayrıntılı ayarlamak için kullanılan bir yardımcı fonksiyondur.

Basit dataclass alanı şöyle yazılır:

```python
active: bool = True
```

Ama bazen alan için daha özel ayar yapmak istersin. O zaman `field()` kullanırsın:

```python
login: str = field(init=False)
```

Bu örnekte `init=False` şu anlama gelir:

> Bu alan otomatik `__init__` metoduna parametre olarak eklenmesin.

Yani şu geçerli olmaz:

```python
Student(name="Edward", surname="agle", login="custom")
```

Çünkü `login` dışarıdan alınmamalı.

Bu egzersizde iki alan için `field` kullanmak mantıklı:

```python
login: str = field(init=False)
id: str = field(default_factory=generate_id, init=False)
```

`field()` fonksiyonunun `init` dışında başka parametreleri de vardır. En yaygın olanlar:

```python
field(
    default=...,
    default_factory=...,
    init=True,
    repr=True,
    compare=True,
    hash=None,
    metadata=None,
    kw_only=False,
)
```

Önemli olanları:

### `default`

Alana sabit bir varsayılan değer verir.

```python
active: bool = field(default=True)
```

Bu şuna benzer:

```python
active: bool = True
```

### `default_factory`

Alanın default değerini üretmek için bir fonksiyon kullanır.

```python
id: str = field(default_factory=generate_id)
```

Burada `generate_id` fonksiyonu her yeni nesne için yeniden çağrılır.

### `init`

Bu alan `__init__` içine girsin mi girmesin mi onu belirler.

```python
login: str = field(init=False)
```

`init=False` ise kullanıcı bu alanı constructor'da veremez.

### `repr`

Bu alan `print(obj)` çıktısında görünsün mü onu belirler.

```python
password: str = field(repr=False)
```

Böyle yaparsan `password` alanı otomatik `repr` çıktısında görünmez.

### `compare`

Bu alan `==` karşılaştırmasına dahil edilsin mi onu belirler.

```python
id: str = field(compare=False)
```

Böyle yaparsan iki nesne karşılaştırılırken `id` dikkate alınmaz.

### `metadata`

Alanla ilgili ek bilgi tutmak için kullanılır. Dataclass bunu doğrudan kullanmaz, ama framework'ler veya senin kodun kullanabilir.

```python
name: str = field(metadata={"label": "Student name"})
```

## 4. `default_factory` Ne Demek?

`default_factory`, bir dataclass alanının varsayılan değerini üretmek için kullanılan fonksiyondur.

Özellikle şu durumlarda kullanılır:

- Her nesne için farklı bir default değer gerekiyorsa.
- Default değer dinamik üretilecekse.
- Liste, dict, set gibi mutable default değerler gerekiyorsa.

Bu egzersizde:

```python
id: str = field(default_factory=generate_id, init=False)
```

şu anlama gelir:

> Her yeni `Student` nesnesi oluşturulduğunda `generate_id()` çağrılacak ve dönen değer `id` alanına yazılacak.

Dikkat: `default_factory` içine fonksiyonun kendisi verilir, fonksiyon çağrısı verilmez.

Doğru:

```python
id: str = field(default_factory=generate_id)
```

Yanlış:

```python
id: str = field(default_factory=generate_id())
```

Yanlış olan kullanımda `generate_id()` sınıf tanımlanırken hemen çalışır. Oysa bizim istediğimiz, her yeni nesne oluşturulduğunda çalışmasıdır.

Bu fark çok önemlidir.

Örnek:

```python
student1 = Student("Edward", "agle")
student2 = Student("Ada", "lovelace")
```

`default_factory=generate_id` sayesinde:

```text
student1.id başka bir random değer
student2.id başka bir random değer
```

olur.

Mutable değerlerde de `default_factory` önemlidir.

Yanlış kullanım:

```python
@dataclass
class Classroom:
    students: list = []
```

Bu tehlikelidir, çünkü aynı liste birden fazla nesne arasında paylaşılabilir.

Doğru kullanım:

```python
@dataclass
class Classroom:
    students: list = field(default_factory=list)
```

Burada her `Classroom` nesnesi için yeni ve bağımsız bir liste oluşturulur.

## 5. `generate_id()` Fonksiyonunun Parça Parça Açıklaması

Subject'in verdiği fonksiyon:

```python
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))
```

Bu fonksiyon 15 karakter uzunluğunda, küçük harflerden oluşan random bir string üretir.

Parça parça bakalım.

### `def generate_id() -> str:`

```python
def generate_id() -> str:
```

Bu bir fonksiyon tanımıdır.

`generate_id` fonksiyonun adıdır.

Parantezin içi boş:

```python
()
```

Yani dışarıdan parametre almıyor.

Şu kısım:

```python
-> str
```

return type annotation'dır. Yani bu fonksiyonun string döndürmesinin beklendiğini söyler. Python bunu runtime'da otomatik zorlamaz, ama kodu okuyan kişi ve type checker'lar için bilgi verir.

### `string.ascii_lowercase`

```python
string.ascii_lowercase
```

`string` modülündeki küçük İngilizce harfleri içeren hazır string'dir.

Değeri şuna benzer:

```python
"abcdefghijklmnopqrstuvwxyz"
```

Yani random seçim yapılacak karakter havuzu budur.

### `random.choices(...)`

```python
random.choices(string.ascii_lowercase, k=15)
```

`random.choices`, verilen popülasyondan birden fazla rastgele seçim yapar.

Burada popülasyon:

```python
string.ascii_lowercase
```

Yani küçük harfler.

`k=15`:

```python
k=15
```

15 tane seçim yapılacağını söyler.

Örnek sonuç:

```python
['t', 'r', 'a', 'n', 'n', 'x', 'h', 'n', 'd', 'g', 't', 'o', 'l', 'v', 'h']
```

`choices` ile seçilen karakterler tekrar edebilir. Mesela aynı harf birden fazla kez gelebilir. Çünkü `random.choices` varsayılan olarak replacement ile seçim yapar.

Yani sonuçta `n` harfi birkaç defa gelebilir; bu normaldir.

### `"".join(...)`

```python
"".join(...)
```

`join`, bir iterable içindeki string parçalarını birleştirir.

Burada ayırıcı string boştur:

```python
""
```

Yani karakterlerin arasına hiçbir şey koymadan birleştirir.

Örnek:

```python
letters = ["a", "b", "c"]
"".join(letters)
```

Sonuç:

```python
"abc"
```

Eğer şöyle olsaydı:

```python
"-".join(["a", "b", "c"])
```

sonuç şu olurdu:

```python
"a-b-c"
```

Bizim fonksiyonda:

```python
return "".join(random.choices(string.ascii_lowercase, k=15))
```

şu demektir:

1. Küçük harflerden 15 tane random karakter seç.
2. Bu karakterleri liste olarak al.
3. Aralarına hiçbir şey koymadan birleştir.
4. Oluşan string'i döndür.

Örnek dönüş:

```text
trannxhndgtolvh
```

## 6. `__post_init__` Metodu Ne Demek?

`__post_init__`, dataclass'ın otomatik oluşturduğu `__init__` metodu çalıştıktan hemen sonra çağrılan özel bir metoddur.

Örnek:

```python
@dataclass
class Student:
    name: str
    surname: str
    login: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
```

Şu nesne oluşturulunca:

```python
student = Student(name="Edward", surname="agle")
```

dataclass önce yaklaşık olarak şunu yapar:

```python
self.name = "Edward"
self.surname = "agle"
```

Sonra otomatik olarak:

```python
self.__post_init__()
```

çağrılır.

Bu sayede `login` gibi başka alanlardan türetilen değerleri hesaplayabilirsin:

```python
self.login = self.name[0] + self.surname
```

Bu egzersizde:

```python
name = "Edward"
surname = "agle"
```

olduğu için:

```python
self.name[0]
```

şu değerdir:

```python
"E"
```

Sonra:

```python
"E" + "agle"
```

sonuç:

```python
"Eagle"
```

Bu yüzden `login` alanı:

```python
login='Eagle'
```

olur.

`__post_init__` dataclass'a özgü bir hook metodudur. Yani genel olarak her Python sınıfında otomatik çağrılan standart bir metod değildir.

Normal bir sınıfta şöyle yazarsan:

```python
class A:
    def __post_init__(self):
        print("çalıştı")
```

ve sonra:

```python
a = A()
```

dersen `__post_init__` otomatik çalışmaz.

Ama `@dataclass` kullanınca ve dataclass kendi `__init__` metodunu üretince, `__post_init__` varsa onu otomatik çağırır.

Yani:

```text
__init__      -> genel Python constructor metodudur.
__post_init__ -> dataclass'ın otomatik __init__ sonrasında çağırdığı özel hook'tur.
```

## Bu Egzersizde Alanların Rolleri

Final sınıfta alanlar şöyle düşünülmeli:

```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)
```

### `name`

```python
name: str
```

Kullanıcı tarafından verilir:

```python
Student(name="Edward", surname="agle")
```

### `surname`

```python
surname: str
```

Kullanıcı tarafından verilir.

### `active`

```python
active: bool = True
```

Default değeri `True` olur.

Bu alan `init=True` olduğu için kullanıcı isterse değiştirebilir:

```python
Student(name="Edward", surname="agle", active=False)
```

Subject sadece default olarak `True` olmasını istiyor.

### `login`

```python
login: str = field(init=False)
```

Kullanıcı tarafından verilemez.

Şu hata vermelidir:

```python
Student(name="Edward", surname="agle", login="custom")
```

Değeri `__post_init__` içinde hesaplanır:

```python
self.login = self.name[0] + self.surname
```

### `id`

```python
id: str = field(default_factory=generate_id, init=False)
```

Kullanıcı tarafından verilemez.

Şu hata vermelidir:

```python
Student(name="Edward", surname="agle", id="toto")
```

Değeri her yeni nesne için `generate_id()` ile otomatik üretilir.

## Neden Alan Sırası Önemli?

Dataclass'ta default değeri olmayan alanlar, default değeri olan alanlardan önce gelmelidir.

Doğru:

```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
```

Yanlış:

```python
@dataclass
class Student:
    active: bool = True
    name: str
    surname: str
```

Bu hata verir, çünkü Python fonksiyon parametrelerinde de default değeri olmayan parametreler default değeri olanlardan sonra gelemez.

Dataclass otomatik `__init__` ürettiği için aynı kural burada da geçerlidir.

## Özet

Bu egzersizin ana fikri şu:

```text
Dataclass ile veri sınıfı oluştur.
field(init=False) ile dışarıdan verilmemesi gereken alanları kapat.
default_factory ile her nesneye özel random id üret.
__post_init__ ile name ve surname'den login türet.
Dataclass'ın otomatik __repr__ çıktısını kullan.
```

Kavramların kısa karşılığı:

```text
@dataclass:
    Sınıfa otomatik __init__, __repr__, __eq__ gibi metodlar ekler.

field:
    Dataclass alanının davranışını ayarlar.

init=False:
    Bu alan constructor'dan alınmasın demektir.

default_factory:
    Default değeri üretmek için fonksiyon kullanır.

__post_init__:
    Dataclass'ın otomatik __init__ işleminden sonra çalışan hook metodudur.
```

## Sorulara Cevaplar

### 1. "Alanlar type annotation ile yazılır: `name: str`" derken alan ne demek?

Buradaki **alan** kelimesi İngilizcedeki **field** kelimesinin Türkçe karşılığıdır.

Dataclass bağlamında alan şudur:

```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
```

Bu sınıfta:

```text
name
surname
active
```

birer dataclass alanıdır.

Normal class terminolojisinde bunlara çoğu zaman **attribute** da deriz. Yani evet, dataclass'taki field/alan kavramı büyük ölçüde attribute kavramıyla ilişkilidir. Ama tamamen aynı şey gibi düşünmemek daha doğru olur.

Normal bir sınıfta attribute genelde şöyle oluşur:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Burada `self.name` bir instance attribute'tur.

Dataclass'ta ise attribute'ları sınıfın başında bildirirsin:

```python
@dataclass
class Student:
    name: str
```

Dataclass bu bildirime bakarak otomatik `__init__` üretir. Yani şunu sen yazmamış olsan bile dataclass yaklaşık olarak senin yerine yazar:

```python
def __init__(self, name: str):
    self.name = name
```

Bu yüzden dataclass'ta "alan" dediğimiz şey:

```text
Dataclass'ın okuyup __init__, __repr__, __eq__ gibi metodları üretirken kullandığı tanımlı attribute bilgisi.
```

Yani:

```python
name: str
```

şu bilgileri verir:

```text
Bu sınıfta name adlı bir alan var.
Bu alanın beklenen tipi str.
Bu alan __init__ içine parametre olarak girsin.
Bu alan repr çıktısında görünsün.
Bu alan karşılaştırmalarda kullanılsın.
```

Tabii bu davranışların bazıları `field()` ile değiştirilebilir.

`field` kelimesinin bununla alakası var mı?

Evet, doğrudan alakası var. `field()` fonksiyonu, dataclass alanının ayarlarını detaylandırmak için kullanılır.

Mesela:

```python
login: str = field(init=False)
```

Burada `login` yine bir dataclass alanıdır. Ama `field(init=False)` diyerek bu alanın otomatik `__init__` içine girmemesini söylüyoruz.

Yani:

```python
name: str
```

basit alan tanımıdır.

```python
login: str = field(init=False)
```

özel ayarlı alan tanımıdır.

Kısaca:

```text
attribute:
    Nesnenin üzerinde bulunan değer.

dataclass field / alan:
    Dataclass'ın özel olarak tanıdığı, type annotation ile bildirilen attribute tanımı.

field():
    Bu dataclass alanının davranışını ayarlayan yardımcı fonksiyon.
```

### 2. `default_factory=generate_id` normal sınıfta her nesne için id üretmek gibi mi çalışıyor?

Evet, mantık olarak çok benzer.

Normal bir sınıfta şöyle yazabilirdin:

```python
class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.id = generate_id()
```

Burada her yeni `Student` nesnesi oluşturulduğunda `__init__` çalışır ve:

```python
self.id = generate_id()
```

satırı sayesinde yeni bir id üretilir.

Dataclass'taki şu kullanım:

```python
id: str = field(default_factory=generate_id, init=False)
```

buna benzer bir iş yapar.

Şu anlama gelir:

```text
Bu alanın değerini oluştururken generate_id fonksiyonunu çağır.
Ama id alanını __init__ parametresi olarak kullanıcıdan alma.
```

Yaklaşık zihinsel karşılığı:

```python
def __init__(self, name, surname, active=True):
    self.name = name
    self.surname = surname
    self.active = active
    self.id = generate_id()
```

Burada çok önemli bir detay var:

```python
default_factory=generate_id
```

yazıyoruz.

Şunu yazmıyoruz:

```python
default_factory=generate_id()
```

Çünkü `default_factory` fonksiyonun kendisini ister. Dataclass o fonksiyonu nesne oluşturulurken kendisi çağırır.

Amaç id için uniqueness mi?

Bu egzersizde amaç öncelikle şudur:

```text
Her Student nesnesine otomatik ve random bir id vermek.
```

Bu random id pratikte "unique olsun" niyetiyle kullanılıyor gibi düşünülebilir. Ama teknik olarak bu fonksiyon uniqueness garantisi vermez.

Çünkü:

```python
random.choices(string.ascii_lowercase, k=15)
```

random seçim yapar. Teorik olarak aynı 15 harfli string iki farklı öğrenciye denk gelebilir. İhtimal çok düşüktür, ama sıfır değildir.

Yani doğru ifade:

```text
generate_id random id üretir.
Bu id'nin çakışma ihtimali düşüktür.
Ama bu kod uniqueness garantisi vermez.
```

Gerçek bir sistemde kesin unique id istiyorsan genelde şunlar kullanılır:

```python
uuid.uuid4()
```

veya veritabanı unique constraint gibi mekanizmalar.

Ama subject sadece `random` ve `string` kullanımına izin verdiği için bu egzersizde verilen `generate_id()` fonksiyonu kullanılmalı.

### 3. `random.choices` normalde liste mi dönüyor? O yüzden mi `.join` kullanıyoruz?

Evet.

`random.choices(...)` bir **list** döndürür.

Örnek:

```python
import random
import string

result = random.choices(string.ascii_lowercase, k=5)
print(result)
```

Olası çıktı:

```text
['a', 'q', 'm', 'z', 'b']
```

Bu bir string değildir, listedir.

Ama bizim istediğimiz id şu şekilde bir string:

```text
aqmzb
```

Bu yüzden `join` kullanıyoruz:

```python
"".join(['a', 'q', 'm', 'z', 'b'])
```

Sonuç:

```python
"aqmzb"
```

Subject'teki kullanım:

```python
"".join(random.choices(string.ascii_lowercase, k=15))
```

şöyle okunabilir:

```text
Küçük harflerden 15 tanesini liste olarak seç.
Sonra bu listedeki karakterleri araya boşluk koymadan birleştir.
```

Eğer `"".join(...)` yerine `"-".join(...)` kullansaydın:

```python
"-".join(["a", "q", "m"])
```

sonuç şu olurdu:

```python
"a-q-m"
```

Ama id için araya karakter koymak istemiyoruz. O yüzden ayırıcı olarak boş string kullanıyoruz:

```python
""
```

Ek not: `random.choice(...)` ve `random.choices(...)` farklıdır.

```python
random.choice(string.ascii_lowercase)
```

tek bir eleman döndürür:

```python
"a"
```

Ama:

```python
random.choices(string.ascii_lowercase, k=5)
```

liste döndürür:

```python
["a", "q", "m", "z", "b"]
```

Bu yüzden `choices` sonucunu string yapmak için `join` mantıklı bir çözümdür.

### 4. "Hook metodu" ne demek?

Hook metodu, bir sistemin veya framework'ün belirli bir anda otomatik olarak çağırdığı, senin de o ana özel davranış eklemek için tanımladığın metoddur.

Kelime anlamıyla "hook", bir yere tutunma noktası gibi düşünülebilir.

Programlama açısından:

```text
Sistem bir akış yürütür.
Bu akışın belirli noktalarında sana özel kod yazabilmen için bazı metod adları tanımlar.
Sen o metodları yazarsan, sistem doğru zamanda onları çağırır.
```

Dataclass'ta:

```python
def __post_init__(self):
    ...
```

bir hook metodudur.

Çünkü dataclass otomatik `__init__` çalıştıktan sonra bu metod var mı diye bakar. Varsa çağırır.

Sen doğrudan şunu yazmazsın:

```python
student.__post_init__()
```

Normal kullanımda dataclass senin yerine çağırır.

Örnek:

```python
@dataclass
class Student:
    name: str
    surname: str
    login: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
```

Akış:

```text
Student(...) çağrılır.
Dataclass'ın ürettiği __init__ çalışır.
name ve surname atanır.
Sonra dataclass __post_init__ metodunu otomatik çağırır.
login hesaplanır.
```

Bilmen gereken bazı hook benzeri metodlara örnekler:

### `__init__`

Python nesne oluşturulurken çağırır.

```python
class User:
    def __init__(self, name):
        self.name = name
```

`__init__`, genel Python sınıflarında kullanılan çok temel bir hook gibi düşünülebilir. Nesne initialize edilirken otomatik çağrılır.

### `__post_init__`

Dataclass'a özgüdür.

```python
@dataclass
class User:
    name: str

    def __post_init__(self):
        self.name = self.name.strip()
```

Dataclass'ın otomatik `__init__` işleminden sonra çağrılır.

### `__str__`

Nesne `str(obj)` ile string'e çevrilirken veya `print(obj)` sırasında çağrılır.

```python
class User:
    def __str__(self):
        return "User object"
```

Bu egzersizde subject özellikle `__str__` yazmamayı söylüyor.

### `__repr__`

Nesnenin geliştiriciye yönelik temsili gerektiğinde çağrılır.

```python
class User:
    def __repr__(self):
        return "User(...)"
```

Dataclass bunu otomatik üretir. Bu egzersizde manuel yazılmamalı.

### `__len__`

`len(obj)` çağrıldığında çalışır.

```python
class Team:
    def __init__(self):
        self.members = []

    def __len__(self):
        return len(self.members)
```

### `__enter__` ve `__exit__`

`with` bloğuna girerken ve çıkarken çağrılır.

```python
class Resource:
    def __enter__(self):
        print("kaynak açıldı")
        return self

    def __exit__(self, exc_type, exc, traceback):
        print("kaynak kapandı")
```

Kullanım:

```python
with Resource() as resource:
    print("içerideyim")
```

### `setUp` ve `tearDown`

Python'un `unittest` framework'ünde testlerden önce ve sonra çağrılan hook metodlarıdır.

```python
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        print("Her testten önce çalışır")

    def tearDown(self):
        print("Her testten sonra çalışır")
```

Burada `setUp` ve `tearDown` Python dilinin magic method'u değildir, ama `unittest` framework'ünün tanıdığı hook metodlarıdır.

Kısa özet:

```text
Hook metodu:
    Senin doğrudan çağırmadığın,
    ama Python'un, dataclass'ın veya bir framework'ün
    belirli bir anda otomatik çağırdığı özel metod.
```

Bu yüzden `__post_init__` için en doğru cümle şu olur:

```text
__post_init__, dataclass'ın otomatik __init__ işleminden sonra çağırdığı dataclass hook metodudur.
```
