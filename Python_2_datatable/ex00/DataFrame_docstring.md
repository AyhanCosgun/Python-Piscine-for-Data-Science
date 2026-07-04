# Pandas `DataFrame`

<div align="center">

<span style="background:#2563eb;color:white;padding:6px 10px;border-radius:999px;">2 Boyutlu</span>
<span style="background:#16a34a;color:white;padding:6px 10px;border-radius:999px;">Etiketli Satır/Sütun</span>
<span style="background:#f97316;color:white;padding:6px 10px;border-radius:999px;">Boyutu Değişebilir</span>
<span style="background:#9333ea;color:white;padding:6px 10px;border-radius:999px;">Farklı Veri Tipleri</span>

</div>

---

## Kısa Tanım

<div style="border-left:5px solid #2563eb;background:#eff6ff;padding:12px 16px;border-radius:8px;">

`DataFrame`, pandas'ın ana veri yapısıdır. İki boyutlu, satır ve sütunlardan oluşan,
etiketli, boyutu değiştirilebilir ve farklı veri tiplerini aynı anda taşıyabilen
tablosal bir yapıdır.

</div>

Bir `DataFrame` şu şekilde düşünülebilir:

- Excel tablosu gibi satır ve sütunlardan oluşur.
- Her sütun aslında bir `Series` nesnesi gibi davranır.
- Satırların ve sütunların etiketleri vardır.
- Aritmetik işlemler satır ve sütun etiketlerine göre hizalanır.
- Sözlük benzeri şekilde sütunlara erişilebilir.

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Ada", "Linus", "Grace"],
    "score": [95, 88, 100],
})

print(df)
```

```text
    name  score
0    Ada     95
1  Linus     88
2  Grace    100
```

---

## Parametreler

### `data`

<div style="border-left:5px solid #16a34a;background:#f0fdf4;padding:12px 16px;border-radius:8px;">

`DataFrame` içine koyulacak asıl veridir.

</div>

Kabul edilebilecek yaygın veri tipleri:

| Veri tipi | Açıklama |
| --- | --- |
| `ndarray` | NumPy dizisi olabilir. |
| `Iterable` | Liste veya benzeri yinelenebilir yapılar olabilir. |
| `dict` | En sık kullanılan biçimlerden biridir. Anahtarlar genelde sütun adı olur. |
| `DataFrame` | Var olan bir `DataFrame` üzerinden yeni `DataFrame` oluşturulabilir. |
| `Series` | Etiketlerine göre hizalanarak tabloya eklenebilir. |
| `dataclass` | Dataclass nesnelerinden tablo üretilebilir. |

> Dict kullanılırsa sütun sırası, sözlüğe eklenme sırasını takip eder.

```python
d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=d)
```

### `index`

<div style="border-left:5px solid #f97316;background:#fff7ed;padding:12px 16px;border-radius:8px;">

Satır etiketlerini belirler.

</div>

Eğer `index` verilmezse pandas genellikle `RangeIndex` kullanır:

```text
0, 1, 2, 3, ...
```

Örnek:

```python
df = pd.DataFrame(
    {"score": [95, 88, 100]},
    index=["student_1", "student_2", "student_3"],
)
```

### `columns`

<div style="border-left:5px solid #9333ea;background:#faf5ff;padding:12px 16px;border-radius:8px;">

Sütun etiketlerini belirler.

</div>

Eğer veri içinde sütun adları yoksa `columns` ile ad verilebilir. Veri zaten sütun
etiketi içeriyorsa, `columns` aynı zamanda sütun seçimi yapmak için de kullanılabilir.

```python
df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6]],
    columns=["a", "b", "c"],
)
```

### `dtype`

<div style="border-left:5px solid #dc2626;background:#fef2f2;padding:12px 16px;border-radius:8px;">

Veri tipini zorlamak için kullanılır.

</div>

Sadece tek bir `dtype` verilebilir. `None` bırakılırsa pandas veri tipini kendisi
tahmin eder.

```python
import numpy as np

df = pd.DataFrame(
    {"col1": [1, 2], "col2": [3, 4]},
    dtype=np.int8,
)
```

### `copy`

<div style="border-left:5px solid #0891b2;background:#ecfeff;padding:12px 16px;border-radius:8px;">

Girdi verisinin kopyalanıp kopyalanmayacağını belirler.

</div>

| Değer | Davranış |
| --- | --- |
| `True` | Veri kopyalanır. |
| `False` | Uygunsa veri kopyalanmadan kullanılır. |
| `None` | Girdi tipine göre pandas varsayılan davranışı seçer. |

Kısa not:

- `dict` için `copy=None`, genellikle `copy=True` gibi davranır.
- `DataFrame` veya 2 boyutlu `ndarray` için `copy=None`, genellikle `copy=False` gibi davranır.

---

## Benzer Yapıcılar

| Metot | Ne işe yarar? |
| --- | --- |
| `DataFrame.from_records` | Tuple'lardan veya record array yapılarından `DataFrame` üretir. |
| `DataFrame.from_dict` | Dict içindeki `Series`, array veya dict yapılarından tablo üretir. |
| `read_csv` | CSV dosyasını `DataFrame` olarak okur. |
| `read_table` | Genel ayrılmış metin dosyalarını okur. |
| `read_clipboard` | Panodaki metni `DataFrame` olarak okur. |

---

## Orijinal Örnekler

### Dict ile `DataFrame` Oluşturma

```python
d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=d)
df
```

```text
   col1  col2
0     1     3
1     2     4
```

Pandas burada veri tipini otomatik olarak `int64` tahmin eder:

```python
df.dtypes
```

```text
col1    int64
col2    int64
dtype: object
```

Tek bir veri tipini zorlamak için:

```python
df = pd.DataFrame(data=d, dtype=np.int8)
df.dtypes
```

```text
col1    int8
col2    int8
dtype: object
```

### Dict İçinde `Series` Kullanma

```python
d = {
    "col1": [0, 1, 2, 3],
    "col2": pd.Series([2, 3], index=[2, 3]),
}

pd.DataFrame(data=d, index=[0, 1, 2, 3])
```

```text
   col1  col2
0     0   NaN
1     1   NaN
2     2   2.0
3     3   3.0
```

<div style="border-left:5px solid #eab308;background:#fefce8;padding:12px 16px;border-radius:8px;">

Buradaki önemli nokta: `Series` kendi index değerlerine göre hizalanır. Bu yüzden
`0` ve `1` satırlarında `col2` için değer yoktur ve sonuç `NaN` olur.

</div>

### NumPy `ndarray` ile Oluşturma

```python
df2 = pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    columns=["a", "b", "c"],
)

df2
```

```text
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9
```

### Etiketli NumPy Dizisinden Sütun Seçme

```python
data = np.array(
    [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
    dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")],
)

df3 = pd.DataFrame(data, columns=["c", "a"])
df3
```

```text
   c  a
0  3  1
1  6  4
2  9  7
```

### Dataclass ile Oluşturma

```python
from dataclasses import make_dataclass

Point = make_dataclass("Point", [("x", int), ("y", int)])

pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
```

```text
   x  y
0  0  0
1  0  3
2  2  3
```

### `Series` veya Başka Bir `DataFrame` ile Oluşturma

```python
ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame(data=ser, index=["a", "c"])
df
```

```text
   0
a  1
c  3
```

```python
df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
df2 = pd.DataFrame(data=df1, index=["a", "c"])
df2
```

```text
   x
a  1
c  3
```

---

## Kısa ve Güzel Ek Örnekler

### 1. CSV Dosyasını Okuyup İlk Satırlara Bakmak

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
```

```text
head()  -> ilk 5 satırı gösterir
shape   -> (satır_sayısı, sütun_sayısı) döndürür
```

### 2. Sütun Seçmek

```python
students = pd.DataFrame({
    "name": ["Ada", "Linus", "Grace"],
    "score": [95, 88, 100],
    "passed": [True, True, True],
})

students["name"]
```

```text
0      Ada
1    Linus
2    Grace
Name: name, dtype: object
```

Birden fazla sütun seçmek:

```python
students[["name", "score"]]
```

### 3. Koşula Göre Filtreleme

```python
high_scores = students[students["score"] >= 90]
high_scores
```

```text
    name  score  passed
0    Ada     95    True
2  Grace    100    True
```

### 4. Yeni Sütun Eklemek

```python
students["grade"] = ["A", "B", "A+"]
students
```

```text
    name  score  passed grade
0    Ada     95    True     A
1  Linus     88    True     B
2  Grace    100    True    A+
```

### 5. Basit İstatistik Almak

```python
students["score"].mean()
```

```text
94.33333333333333
```

```python
students.describe()
```

### 6. Satırları Sıralamak

```python
students.sort_values(by="score", ascending=False)
```

```text
    name  score  passed grade
2  Grace    100    True    A+
0    Ada     95    True     A
1  Linus     88    True     B
```

### 7. Index'i Anlamlı Hale Getirmek

```python
students = students.set_index("name")
students
```

```text
       score  passed grade
name
Ada       95    True     A
Linus     88    True     B
Grace    100    True    A+
```

<div style="border-left:5px solid #2563eb;background:#eff6ff;padding:12px 16px;border-radius:8px;">

Özet fikir: `DataFrame`, Python'da tabloyla çalışmanın merkezidir. CSV okuma,
sütun seçme, filtreleme, yeni sütun üretme, sıralama ve istatistik alma gibi
günlük veri işlemleri çoğunlukla bu yapı üzerinden yapılır.

</div>
