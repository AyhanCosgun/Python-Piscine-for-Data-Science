# Python 1 Array - Calisma Context Notlari

Bu dosya, bu projedeki sohbet context'ini baska bir bilgisayara veya yeni bir
Codex/VS Code oturumuna tasimak icin hazirlandi.

## Proje

- Proje adi: `Training Piscine Python for datascience - 1 / Array`
- Subject dosyasi: `Python_1_array_subject.pdf`
- Version: `1.1`
- Ana konu: array/list manipulations, NumPy, image loading, image slicing,
  transpose ve color filters.

## Genel Kurallar

- Python `3.10` kullanilmali.
- Importlar explicit olmali: `import numpy as np` gibi.
- `from module import *` yasak.
- Global variable yok.
- Global scope'ta calisan kod olmamali. Programlarda `main()` ve
  `if __name__ == "__main__": main()` yapisi kullanilmali.
- Yakalanmamis exception egzersizi gecersiz yapabilir.
- Tum fonksiyonlarin docstring'i olmali.
- Kod `flake8` ile norm kontrolunden gecmeli.
- Sadece git reposundaki dogru klasor/dosya isimleri degerlendirilir.

## Kavramsal Notlar

### Array

Programlama baglaminda array, indekslenmis ve duzenli veri koleksiyonudur.
Sayisal verilerden olusuyorsa matematiksel olarak vector, matrix veya tensor
gibi yorumlanabilir.

Kritik ayrim:

- Her sayisal vector bir array ile temsil edilebilir.
- Ama her array matematiksel vector uzayi elemani gibi davranmak zorunda degil.
- Ornegin `np.array(["Ali", "Ayse", "Mehmet"])` string array'dir. Uzerinde
  uygun toplama ve skaler carpma tanimlanirsa soyut matematikte bir vector
  uzayi modeli kurulabilir, ama NumPy bunu otomatik olarak lineer cebir nesnesi
  gibi kullanmaz.

### Python list ve NumPy array farki

Python list genel amaclidir:

```python
[1, 2, 3] * 2
# [1, 2, 3, 1, 2, 3]
```

NumPy array sayisal/toplu islem odaklidir:

```python
np.array([1, 2, 3]) * 2
# array([2, 4, 6])
```

### Shape

`shape`, array'in eksen uzunluklarini veren tuple'dir.

```text
np.array([1, 2, 3]).shape        -> (3,)
np.array([[1], [2], [3]]).shape  -> (3, 1)
np.array([[1, 2, 3]]).shape      -> (1, 3)
```

Matematiksel yorum:

- `(3,)`: 1D array, R^3 icindeki coordinate tuple gibi. Satir/sutun yonelimi
  yoktur.
- `(3, 1)`: 2D array, 3x1 column vector gibi.
- `(1, 3)`: 2D array, 1x3 row vector gibi.

NumPy'da `(3,)`, `3x1` matrix degildir. 1D array'in transpose'u yine `(3,)`
kalir. Column vector isteniyorsa acikca `(3, 1)` shape'i olusturulmali.

### 2D slicing

Slicing, bir array/list'in indeks araligi ile parcasini almaktir.

```python
numbers = [10, 20, 30, 40, 50]
numbers[1:4]
# [20, 30, 40]
```

2D durumda bu, alt matrix almak gibi dusunulebilir. Bu projedeki `ex01`
ozellikle satir slicing istiyor:

```python
family[start:end]
```

Bu satirlari keser, sutunlari aynen birakir.

### 3D array

3D array'i `A x B x C` kartezyen carpimindan alinan tek bir ornek gibi degil,
bu indeks grid'i uzerinde tanimli bir fonksiyon/tablo gibi dusunmek daha dogru:

```text
T : {0,...,a-1} x {0,...,b-1} x {0,...,c-1} -> Values
```

Image ornegi:

```text
image.shape == (height, width, channels)
```

RGB image icin:

```text
image[i, j, 0] -> red channel
image[i, j, 1] -> green channel
image[i, j, 2] -> blue channel
```

## Egzersiz Ozeti

### ex00 - Give my BMI

Teslim dosyasi:

```text
ex00/give_bmi.py
```

Istenen fonksiyonlar:

```python
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    ...

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ...
```

`give_bmi`, boy ve kilo listelerinden BMI hesaplar:

```text
BMI = weight / height ** 2
```

`apply_limit`, BMI degerlerini limit ile karsilastirir:

```text
value > limit -> True
otherwise     -> False
```

Subject'teki hata ifadesi:

```text
You have to handle error cases if the lists are not the same size,
are not int or float...
```

Bu ifade iki sekilde yorumlanabilir:

1. Minimal yorum:
   - Parametrelerin zaten list geldigi varsayilir.
   - Sadece uzunluklar ve eleman tipleri kontrol edilir.

2. Daha defensive yorum:
   - Parametrelerin list olup olmadigi da kontrol edilir.
   - Cunku Python type hint'leri runtime'da zorunlu degildir.

Bu proje icin daha guvenli yaklasim:

- `height` ve `weight` list mi kontrol et.
- Uzunluklari ayni mi kontrol et.
- Elemanlar `int` veya `float` mi kontrol et.
- `bool` degerlerini sayi kabul etme.
- Height degerleri `0`'dan buyuk olmali.
- Hata durumunda acik mesaj yaz ve `[]` don.
- Fonksiyon disariya yakalanmamis exception firlatmamali.

Not: `float(h)` ile donusturme yapmak, `"2.71"` gibi stringleri de kabul eder.
Subject `int | float` dedigi icin bu cok gevsek bir yorumdur. Daha dogru kontrol:

```python
def is_number(value):
    """Return True if value is int or float, but not bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)
```

`int(h)` kontrolune gerek yoktur. BMI icin float height zaten normaldir.
`float("2.71")` gecer ama `int("2.71")` patlar; bu, int kontrolu eklemek icin
iyi bir sebep degildir.

Onerilen ex00 validation yapisi:

```python
def is_number(value):
    """Return True if value is int or float, but not bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI values from height and weight lists."""
    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: height and weight must be lists.")
        return []

    if len(height) != len(weight):
        print("Error: height and weight must have the same length.")
        return []

    if not all(is_number(h) for h in height):
        print("Error: height must contain only int or float values.")
        return []

    if not all(is_number(w) for w in weight):
        print("Error: weight must contain only int or float values.")
        return []

    if not all(h > 0 for h in height):
        print("Error: height values must be greater than zero.")
        return []

    return [w / (h ** 2) for h, w in zip(height, weight)]
```

`apply_limit` icin de defensive kontrol mantigi:

```python
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value above the limit."""
    if not isinstance(bmi, list):
        print("Error: bmi must be a list.")
        return []

    if not isinstance(limit, int) or isinstance(limit, bool):
        print("Error: limit must be an integer.")
        return []

    if not all(is_number(value) for value in bmi):
        print("Error: bmi must contain only int or float values.")
        return []

    return [value > limit for value in bmi]
```

### ex01 - 2D array

Teslim dosyasi:

```text
ex01/array2D.py
```

Fonksiyon:

```python
def slice_me(family: list, start: int, end: int) -> list:
    ...
```

Istenen:

- 2D array/list al.
- Eski shape'i yazdir.
- Slicing ile `family[start:end]` al.
- Yeni shape'i yazdir.
- Sonucu list olarak don.

Hata durumlari:

- `family` list degilse.
- 2D rectangular degilse.
- Ic listelerin uzunluklari ayni degilse.

### ex02 - Load my image

Teslim dosyasi:

```text
ex02/load_image.py
```

Fonksiyon:

```python
def ft_load(path: str) -> array:
    ...
```

Istenen:

- Image dosyasini yukle.
- En az JPG/JPEG destekle.
- Shape yazdir.
- Pixel icerigini RGB formatinda goster.
- Hata durumunda acik mesaj ver.

Image shape ornegi:

```text
(257, 450, 3)
```

Bu su demektir:

- 257 pixel height
- 450 pixel width
- 3 color channels: RGB

### ex03 - Zoom on me

Teslim dosyalari:

```text
ex03/load_image.py
ex03/zoom.py
```

Program `animal.jpeg` yukler, bilgileri yazdirir ve zoom/crop yapilmis
goruntuyu gosterir.

Beklenen yaklasim:

- Original image shape ve pixel array yazdir.
- Kare bir bolge kes.
- Genellikle grayscale/tek kanal hale getir.
- Yeni shape `(400, 400, 1)` veya `(400, 400)` olabilir.
- Matplotlib ile x/y scale gorunecek sekilde display et.

### ex04 - Rotate me

Teslim dosyalari:

```text
ex04/load_image.py
ex04/rotate.py
```

Program `animal.jpeg` yukler, kare bir bolge keser ve transpose eder.

Kritik kural:

- Transpose islemi library ile yapilamaz.
- `np.transpose`, `.T` gibi hazir transpose kullanma.
- Satir/sutun degisimini kendin loop veya list comprehension ile yap.

### ex05 - Pimp my image

Teslim dosyalari:

```text
ex05/load_image.py
ex05/pimp_image.py
```

Fonksiyonlar:

```python
def ft_invert(array) -> array:
    ...

def ft_red(array) -> array:
    ...

def ft_green(array) -> array:
    ...

def ft_blue(array) -> array:
    ...

def ft_grey(array) -> array:
    ...
```

Istenen:

- Her filtre image shape'ini korumali.
- Transform edilmis imageler display edilmeli.
- Fonksiyonlarin docstring'i olmali.

Operator kisitlari:

```text
invert: =, +, -, *
red:    =, *
green:  =, -
blue:   =
grey:   =, /
```

## Type Hint Notu

Python'daki su imza runtime'da strict kontrol yapmaz:

```python
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    ...
```

Bu sadece type hint'tir. Editor, autocomplete, mypy/pyright gibi araclar icin
faydalidir; ama Python yorumlayicisi yanlis tipleri otomatik reddetmez.

Bu nedenle runtime validation, TypeScript'teki compile-time strictlikten farkli
olarak `if isinstance(...)` gibi kontrollerle elle yapilir.

## Bu Dosyanin Kullanimi

Yeni bilgisayarda veya yeni VS Code/Codex oturumunda bu dosyayi once okut:

```text
Bu projede once CONTEXT_python_1_array.md dosyasini oku ve oradaki context'e
gore devam et.
```

Boylece sohbet gecmisi birebir tasinmasa bile proje kararlari ve kavramsal
baglam korunur.
