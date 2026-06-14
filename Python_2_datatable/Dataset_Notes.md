# Dataset, NumPy, Pandas ve DataFrame Notları

Bu belge; dataset, NumPy array, Pandas, Series, DataFrame, indeks ve `merge()`
kavramlarını açıklayan çalışma notudur.

## 1. Dataset Nedir?

**Dataset**, belirli bir amaçla düzenlenmiş veri koleksiyonudur. Python'a ait
özel bir veri tipi değildir.

Örnek bir öğrenci dataset'i:

| name | age | score |
|---|---:|---:|
| Ayşe | 21 | 85 |
| Mehmet | 23 | 92 |
| Zeynep | 20 | 78 |

Bu tabloda:

- Her **satır** bir gözlem veya kayıttır.
- Her **sütun** bir özellik veya değişkendir.
- Her **hücre** tek bir değerdir.
- Sütun başlıkları verinin anlamını belirtir.

Bir dataset farklı biçimlerde saklanabilir:

- CSV dosyası
- Excel dosyası
- JSON
- SQL tablosu
- Pandas `DataFrame`
- NumPy array
- Python listeleri

Subject'teki aşağıdaki gösterimde `Dataset` gerçek bir Python tipi değildir:

```python
def load(path: str) -> Dataset:
    ...
```

Bu ifade, kullanılan kütüphanenin uygun veri yapısının döndürülmesi gerektiğini
anlatır. Pandas kullanıldığında dönüş tipi `DataFrame` olur.

## 2. NumPy Array Nedir?

NumPy array, özellikle sayısal hesaplamalar için tasarlanmış N boyutlu bir veri
yapısıdır:

```python
import numpy as np

array = np.array([
    [21, 85],
    [23, 92],
])
```

Bu örnekte:

- Array iki boyutludur.
- İki satırı ve iki sütunu vardır.
- Şekli `(2, 2)` olur.
- Hücrelerdeki `21`, `85`, `23` ve `92` değerleri array'in elemanlarıdır.

```python
print(array.shape)
# (2, 2)

print(array.dtype)
# int64 gibi bir integer dtype
```

### 2.1 Eleman ve satır ayrımı

“Array'in elemanları” ifadesi satırları değil, her bir hücredeki entry'leri
kapsar:

```text
21, 85, 23, 92
```

NumPy array'in kendisinin tek bir `dtype` değeri bulunur. Girdi olarak farklı
Python tipleri verilirse NumPy mümkün olduğunda bunları ortak bir tipe
dönüştürür.

Örneğin integer ve float birlikte verilirse:

```python
array = np.array([1, 2.5, 3])

print(array)
# [1.  2.5 3. ]

print(array.dtype)
# float64
```

Integer değerler ortak tip olan `float64` türüne yükseltilmiştir.

Sayı ve string birlikte verilirse NumPy tüm değerleri string'e çevirebilir:

```python
array = np.array([1, 2.5, "hello"])
```

Sonuç yaklaşık olarak şöyledir:

```text
['1' '2.5' 'hello']
```

Dolayısıyla değerler NumPy'ye verilmeden önce farklı Python tiplerinde olabilir,
ancak normal bir NumPy array bunları tek bir ortak `dtype` ile saklamaya
çalışır.

### 2.2 Object array istisnası

Bir array içinde farklı Python nesnelerini tutmak mümkündür:

```python
array = np.array(
    [1, "hello", [10, 20]],
    dtype=object,
)

print(array.dtype)
# object
```

Bu durumda her hücre farklı bir Python nesnesine referans verebilir. Fakat
`object` array'ler, NumPy'nin homojen sayısal array'lere sağladığı performans
ve bellek avantajlarının önemli bir kısmını kaybeder.

Özet:

> Bir NumPy array'in hücreleri farklı Python nesnelerine referans verebilir,
> fakat array'in kendisinin yalnızca bir `dtype` değeri vardır.

### 2.3 Satırlar eşit uzunlukta olmalı mı?

Gerçek ve düzenli bir iki boyutlu NumPy array oluşturmak için satırların eşit
uzunlukta olması gerekir:

```python
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(array.shape)
# (2, 3)
```

Eşit olmayan satırlar dikdörtgen bir 2D array oluşturamaz:

```python
np.array([
    [1, 2],
    [3, 4, 5],
])
```

Modern NumPy sürümleri bu kullanımda genellikle hata verir.

`dtype=object` ile düzensiz listeler saklanabilir:

```python
array = np.array(
    [
        [1, 2],
        [3, 4, 5],
    ],
    dtype=object,
)

print(array.shape)
# (2,)
```

Bu, iki boyutlu sayısal bir array değildir. İçinde iki farklı Python listesi
bulunan tek boyutlu bir object array'dir.

## 3. DataFrame Nedir?

`DataFrame`, Pandas'ın iki boyutlu, satır ve sütun etiketlerine sahip tablo
veri yapısıdır:

```python
import pandas as pd

data = {
    "name": ["Ayşe", "Mehmet", "Zeynep"],
    "age": [21, 23, 20],
    "score": [85, 92, 78],
}

students = pd.DataFrame(data)
```

Sonuç:

```text
      name  age  score
0     Ayşe   21     85
1  Mehmet   23     92
2   Zeynep   20     78
```

Burada:

- `name`, `age` ve `score` sütun etiketleridir.
- `0`, `1` ve `2` satır indeksleridir.
- Her sütun bir Pandas `Series` nesnesidir.
- Tüm tablo bir Pandas `DataFrame` nesnesidir.

Kavramsal yapı:

```text
DataFrame
├── Index
├── Columns
├── name  -> Series
├── age   -> Series
└── score -> Series
```

### 3.1 DataFrame özel bir array midir?

DataFrame'e doğrudan “özel bir array” demek doğru değildir.

DataFrame, array benzeri işlemleri destekleyen etiketli bir tablo veri
yapısıdır. Pandas, verileri içeride NumPy array'leri veya başka array
yapılarıyla saklayabilir; fakat DataFrame'in kendisi `numpy.ndarray` değildir:

```python
import numpy as np
import pandas as pd

array = np.array([[21, 85], [23, 92]])
frame = pd.DataFrame(array)

print(type(array))
# <class 'numpy.ndarray'>

print(type(frame))
# <class 'pandas.core.frame.DataFrame'>
```

### 3.2 NumPy array ve DataFrame farkları

| Özellik | NumPy array | Pandas DataFrame |
|---|---|---|
| Yapı | N boyutlu dizi | İki boyutlu tablo |
| Etiketler | Normalde yok | Satır ve sütun etiketleri var |
| Veri tipleri | Tek ortak `dtype` | Her sütun farklı `dtype` taşıyabilir |
| Erişim | Genellikle konuma göre | Konuma veya etikete göre |
| Eksik veri | Daha sınırlı destek | Gelişmiş destek |
| Temel kullanım | Matematik ve matris işlemleri | Tablosal veri analizi |
| Sütun seçimi | Sayısal konum | İsim veya konum |

NumPy erişim örneği:

```python
array[0, 1]
# 85
```

DataFrame erişim örneği:

```python
frame.loc[0, "score"]
# 85
```

## 4. DataFrame Nasıl Oluşturulur?

DataFrame'lerin yalnızca sütun sütun, NumPy array'lerin yalnızca satır satır
oluşturulduğu söylenemez. Her ikisi için de farklı oluşturma yöntemleri vardır.

### 4.1 DataFrame'i sütunlardan oluşturmak

Dictionary anahtarları sütun adı olur:

```python
df = pd.DataFrame({
    "name": ["Ayşe", "Mehmet"],
    "age": [21, 23],
})
```

Kavramsal olarak:

```text
name -> ["Ayşe", "Mehmet"]
age  -> [21, 23]
```

### 4.2 DataFrame'i satırlardan oluşturmak

Her kayıt ayrı bir dictionary olabilir:

```python
df = pd.DataFrame([
    {"name": "Ayşe", "age": 21},
    {"name": "Mehmet", "age": 23},
])
```

İç içe listeler de kullanılabilir:

```python
df = pd.DataFrame(
    [
        ["Ayşe", 21],
        ["Mehmet", 23],
    ],
    columns=["name", "age"],
)
```

### 4.3 NumPy array'i sütunlardan oluşturmak

NumPy array çoğunlukla iç içe satır listeleriyle oluşturulur, ancak sütunları
birleştirmek de mümkündür:

```python
first_column = np.array([1, 3])
second_column = np.array([2, 4])

array = np.column_stack((first_column, second_column))
```

Sonuç:

```text
[[1 2]
 [3 4]]
```

## 5. DataFrame İndeksi Bir Sütun mudur?

Hayır. DataFrame indeksi sütunlardan ayrı bir yapıdır:

```python
df = pd.DataFrame({
    "name": ["Ayşe", "Mehmet"],
    "age": [21, 23],
})
```

Görünüm:

```text
     name  age
0    Ayşe   21
1  Mehmet   23
```

Sol taraftaki `0` ve `1`, gizli veya sıfırıncı bir sütun değildir. Bunlar satır
indeksleridir:

```python
print(df.columns)
# Index(['name', 'age'], dtype='object')

print(df.index)
# RangeIndex(start=0, stop=2, step=1)
```

İlk gerçek sütuna konumla erişmek için:

```python
df.iloc[:, 0]
```

İndeks yapısına erişmek için:

```python
df.index
```

CSV dosyalarında ilk sütun bazen indeks olarak okunabilir, ancak bu
`read_csv()` seçeneklerine ve dosyanın yapısına bağlıdır. DataFrame'in ilk
sütununun her zaman satır etiketlerinden oluşması gibi bir kural yoktur.

## 6. Series Nedir?

`Series`, Pandas'ın tek boyutlu ve etiketli veri yapısıdır:

```python
ages = pd.Series([21, 23, 20], name="age")
```

Görünüm:

```text
0    21
1    23
2    20
Name: age, dtype: int64
```

Kısaca:

```text
Series    = etiketli tek boyutlu veri
DataFrame = ortak satır indeksini kullanan Series sütunları
```

## 7. Ortak İndeks Ne Demektir?

DataFrame içindeki sütunlar aynı satır etiketlerini paylaşır:

```python
df = pd.DataFrame({
    "name": ["Ayşe", "Mehmet"],
    "age": [21, 23],
})
```

`name` Series'i:

```text
0      Ayşe
1    Mehmet
```

`age` Series'i:

```text
0    21
1    23
```

İki Series'in ortak indeksi `0` ve `1` değerleridir. Bu sayede Pandas:

- `name` sütunundaki index `0` değerinin `Ayşe`,
- `age` sütunundaki index `0` değerinin `21`

olduğunu ve bunların aynı satıra ait olduğunu bilir.

İndeksin sayısal olması gerekmez:

```python
df = pd.DataFrame(
    {
        "name": ["Ayşe", "Mehmet"],
        "age": [21, 23],
    },
    index=["student_1", "student_2"],
)
```

Sonuç:

```text
              name  age
student_1     Ayşe   21
student_2   Mehmet   23
```

Ortak indeks bu kez `student_1` ve `student_2` değerleridir.

### 7.1 Pandas indekslere göre hizalama yapar

Series'ler farklı sırada verilse bile Pandas değerleri indeks etiketlerine göre
eşleştirir:

```python
names = pd.Series(
    ["Ayşe", "Mehmet"],
    index=[10, 20],
)

ages = pd.Series(
    [23, 21],
    index=[20, 10],
)

df = pd.DataFrame({
    "name": names,
    "age": ages,
})
```

Sonuç:

```text
      name  age
10    Ayşe   21
20  Mehmet   23
```

Eşleştirme liste sırasına göre değil, indeks etiketlerine göre yapılmıştır:

```text
index 10 -> Ayşe, 21
index 20 -> Mehmet, 23
```

## 8. DataFrame Özellikleri ve Metotları

### 8.1 Özellikler

Özellikler nesne hakkında bilgi taşır ve parantezsiz kullanılır:

```python
frame.shape
frame.columns
frame.index
frame.dtypes
frame.size
frame.ndim
frame.empty
```

| Özellik | Anlamı |
|---|---|
| `shape` | `(satır sayısı, sütun sayısı)` |
| `columns` | Sütun etiketleri |
| `index` | Satır etiketleri |
| `dtypes` | Sütunların veri tipleri |
| `size` | Toplam hücre sayısı |
| `ndim` | Boyut sayısı; DataFrame için `2` |
| `empty` | DataFrame boş mu? |

Ex00'da veri kümesinin boyutunu göstermek için `shape` kullanılır:

```python
print(frame.shape)
# (3, 3)
```

### 8.2 Metotlar

Metotlar nesne üzerinde işlem yapan fonksiyonlardır ve parantezle çağrılır:

```python
frame.head()
frame.tail()
frame.info()
frame.describe()
frame.dropna()
frame.sort_values("score")
```

| Metot | Görevi |
|---|---|
| `head()` | İlk satırları gösterir |
| `tail()` | Son satırları gösterir |
| `info()` | Sütun ve tip bilgilerini verir |
| `describe()` | İstatistiksel özet üretir |
| `dropna()` | Eksik değerleri kaldırır |
| `fillna()` | Eksik değerleri doldurur |
| `sort_values()` | Değerlere göre sıralar |
| `groupby()` | Verileri gruplar |
| `merge()` | DataFrame'leri anahtar üzerinden birleştirir |
| `to_csv()` | Veriyi CSV dosyasına yazar |

Özellik ve metot farkı:

```python
frame.shape
# Özellik

frame.head()
# Metot
```

## 9. `merge()` Nasıl Çalışır?

`merge()`, iki DataFrame'i ortak bir anahtar üzerinden ilişkilendirir. SQL'deki
`JOIN` işlemine benzer.

Birinci tablo:

```python
people = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ayşe", "Mehmet", "Zeynep"],
})
```

```text
   id    name
0   1    Ayşe
1   2  Mehmet
2   3  Zeynep
```

İkinci tablo:

```python
scores = pd.DataFrame({
    "id": [1, 2, 4],
    "score": [85, 92, 70],
})
```

```text
   id  score
0   1     85
1   2     92
2   4     70
```

Ortak `id` sütunu üzerinden birleştirme:

```python
result = people.merge(scores, on="id")
```

Sonuç:

```text
   id    name  score
0   1    Ayşe     85
1   2  Mehmet     92
```

İkinci tablonun `score` sütunu sonuç tablosuna eklenmiştir. Hangi satırların
eşleşeceğini `id` değerleri belirlemiştir.

### 9.1 Inner merge

```python
people.merge(scores, on="id", how="inner")
```

Yalnızca her iki tabloda bulunan `id` değerlerini korur:

```text
id: 1, 2
```

### 9.2 Left merge

```python
people.merge(scores, on="id", how="left")
```

Sol tablonun bütün satırlarını korur:

```text
   id    name  score
0   1    Ayşe   85.0
1   2  Mehmet   92.0
2   3  Zeynep    NaN
```

`id=3` için eşleşen skor bulunmadığından `score` değeri `NaN` olur.

### 9.3 Outer merge

```python
people.merge(scores, on="id", how="outer")
```

Her iki tablodaki bütün anahtarları korur:

```text
   id    name  score
0   1    Ayşe   85.0
1   2  Mehmet   92.0
2   3  Zeynep    NaN
3   4     NaN   70.0
```

Python 2 DataTable projesinin `ex03` alıştırmasında iki dataset ülke adına göre
birleştirilebilir:

```python
result = income.merge(
    life,
    on="country",
    how="inner",
)
```

Bu işlem aynı ülkeye ait gelir ve yaşam beklentisi değerlerini aynı satırda
toplar.

## 10. Pandas Nedir?

Pandas, Python için geliştirilmiş harici bir veri analizi kütüphanesidir.
Python'ın standart kurulumunun parçası değildir.

Kurulum:

```bash
python3 -m pip install pandas
```

Kullanım:

```python
import pandas as pd
```

Pandas'ın iki temel veri yapısı:

- `Series`: Tek boyutlu ve etiketli veri.
- `DataFrame`: İki boyutlu ve etiketli tablo.

Pandas ayrıca:

- CSV ve Excel dosyalarını okuyabilir.
- Verileri filtreleyebilir ve sıralayabilir.
- Eksik verileri yönetebilir.
- Tabloları birleştirebilir.
- Gruplama ve istatistiksel analiz yapabilir.
- Veriyi farklı dosya biçimlerine yazabilir.

## 11. Module, Package ve Library

Bu terimler günlük kullanımda birbirinin yerine kullanılabilse de teknik olarak
farklı anlamlara gelir.

### 11.1 Module

Tek bir Python dosyasıdır:

```text
load_csv.py
```

Başka bir Python dosyasından import edilebilir:

```python
import load_csv
```

### 11.2 Package

Birden fazla modülü ve alt package'ı düzenleyen yapıdır:

```text
my_package/
├── __init__.py
├── reader.py
├── cleaner.py
└── visualization/
    ├── __init__.py
    └── plot.py
```

Örnek kullanım:

```python
import my_package.reader
```

### 11.3 Library

Belirli bir işi gerçekleştirmek için hazırlanmış modül ve package
koleksiyonuna verilen genel isimdir.

Pandas:

- Teknik olarak kurulup import edilen büyük bir Python package'ıdır.
- Kullanım amacı bakımından bir veri analizi kütüphanesidir.
- Kendi içinde çok sayıda modül, alt package, sınıf ve fonksiyon barındırır.

Şema:

```text
Python ekosistemi
│
├── Standart kütüphane
│   ├── os
│   ├── sys
│   ├── csv
│   └── pathlib
│
└── Harici kütüphaneler
    ├── pandas
    │   ├── DataFrame
    │   ├── Series
    │   ├── read_csv()
    │   ├── core
    │   └── io
    │
    ├── numpy
    │   └── ndarray
    │
    └── matplotlib
        └── pyplot
```

### 11.4 Dağıtım paketi ve import adı

`pip`, dağıtım paketini kurar:

```bash
pip install pandas
```

Python, kurulan package'ı import eder:

```python
import pandas
```

Kurulum ve import isimleri çoğu zaman aynıdır, fakat bu zorunlu değildir:

```bash
pip install scikit-learn
```

```python
import sklearn
```

## 12. Import Takma Adları

Şu kullanımdaki `pd`, `pandas` için belirlenen kısa bir takma addır:

```python
import pandas as pd
```

Takma ad kullanmak zorunlu değildir:

```python
import pandas

data = pandas.read_csv("data.csv")
frame = pandas.DataFrame(...)
```

Takma adla aynı kod daha kısa yazılır:

```python
import pandas as pd

data = pd.read_csv("data.csv")
frame = pd.DataFrame(...)
```

Takma adların amaçları:

- Uzun isimleri tekrar tekrar yazmamak.
- Kodu daha kısa ve okunabilir tutmak.
- Python topluluğundaki yaygın kullanıma uymak.
- Gerektiğinde isim çakışmalarını önlemek.

Takma ad istenen geçerli Python ismi olabilir:

```python
import pandas as panda
import pandas as p
import pandas as tablo
```

Ancak Pandas için topluluk standardı `pd` olduğundan bunu kullanmak daha
okunabilir ve beklenebilir koddur.

Yaygın takma adlar:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## 13. Pandas ile CSV Yükleme

Ex00'ın merkezindeki işlem:

```python
dataset = pd.read_csv(path)
```

Burada:

- `pd`: `pandas` package'ının takma adı.
- `read_csv`: Pandas'ın sunduğu bir fonksiyon.
- `path`: CSV dosyasının yolu.
- `dataset`: Oluşturulan DataFrame.

İşlem akışı:

```text
CSV dosyası
    │
    ▼
pd.read_csv(path)
    │
    ▼
DataFrame
    ├── shape
    ├── columns
    ├── index
    ├── dtypes
    └── head(), info(), describe()...
```

Ex00 açısından temel mantık:

```python
dataset = pd.read_csv(path)
print(dataset.shape)
return dataset
```

Gerçek çözümde dosya okuma hataları yakalanmalı ve subject'in istediği biçimde
hata durumunda `None` döndürülmelidir.
