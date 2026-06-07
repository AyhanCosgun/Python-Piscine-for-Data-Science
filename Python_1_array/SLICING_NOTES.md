# Python ve NumPy Slicing Notlari

Bu dosya, Python slicing ozelliklerini ve 2D NumPy array'lerde alt matris
secimini hizlica hatirlamak icin hazirlandi.

## 1. Slicing Bir List Metodu Degildir

Slicing, `.slice()` gibi cagrilan bir `list` metodu degildir. Python'un
indeksleme sozdiziminin bir ozelligidir:

```python
values[start:stop]
```

Ornegin:

```python
values = [10, 20, 30, 40, 50]

print(values[1:4])
# [20, 30, 40]
```

Kurallar:

- `start` indeksi dahildir.
- `stop` indeksi dahil degildir.

Python bunu arka planda bir `slice` nesnesiyle ifade edebilir:

```python
values[1:4]
values[slice(1, 4)]
```

Bu iki ifade esdegerdir.

## 2. Genel Slicing Sozdizimi

Slicing'in genel bicimi:

```python
sequence[start:stop:step]
```

- `start`: Baslangic indeksi, dahildir.
- `stop`: Bitis indeksi, dahil degildir.
- `step`: Elemanlarin kac adimla secilecegidir.

## 3. Temel Slicing Ornekleri

```python
values = [10, 20, 30, 40, 50, 60]
```

Ilk uc elemani alma:

```python
values[:3]
# [10, 20, 30]
```

Belirli bir indeksten sona kadar alma:

```python
values[2:]
# [30, 40, 50, 60]
```

Listenin tamamini alma:

```python
values[:]
# [10, 20, 30, 40, 50, 60]
```

Bu kullanim listenin bir shallow copy'sini olusturur.

Ikiser adimla secme:

```python
values[::2]
# [10, 30, 50]
```

Birinci indeksten baslayip ikiser adimla secme:

```python
values[1::2]
# [20, 40, 60]
```

Listeyi ters cevirme:

```python
values[::-1]
# [60, 50, 40, 30, 20, 10]
```

## 4. Negatif Indeksler

Negatif indeksler listenin sonundan baslayarak sayar:

```text
Deger:          10   20   30   40   50
Pozitif indeks:  0    1    2    3    4
Negatif indeks: -5   -4   -3   -2   -1
```

Ornek:

```python
values = [10, 20, 30, 40, 50]

values[1:-2]
# [20, 30]
```

`-2`, sondan ikinci elemanin indeksidir. `stop` dahil olmadigi icin `40`
sonuca dahil edilmez.

## 5. Slicing Sinir Disinda Hata Vermez

Normal indeks erisimi sinir disinda hata verir:

```python
values[100]
# IndexError
```

Slicing ise mevcut sinirlara uyarlanir:

```python
values[0:100]
# [10, 20, 30, 40, 50]
```

Baslangic bitisten sonraysa genellikle bos bir sequence doner:

```python
values[4:2]
# []
```

Bu nedenle slicing parametrelerine gereksiz yere kati sinir kontrolleri
uygulamamak gerekir.

## 6. Slicing ile Atama

Listelerin bir bolumu slicing ile degistirilebilir:

```python
values = [10, 20, 30, 40]
values[1:3] = [200, 300]

print(values)
# [10, 200, 300, 40]
```

## 7. Slicing Uygulanabilen Yapilar

Slicing yalnizca listelerde kullanilmaz:

```python
"Python"[1:4]
# "yth"

(10, 20, 30)[1:]
# (20, 30)
```

NumPy array'ler de slicing destekler.

## 8. ex01'de Slicing

`ex01` icin istenen islem:

```python
result = family[start:end]
```

Ornek:

```python
family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

result = family[0:2]
```

Sonuc:

```python
[
    [1.80, 78.4],
    [2.15, 102.7]
]
```

Shape degisimi:

```text
(4, 2) -> (2, 2)
```

Burada yalnizca dis liste, yani satirlar slice edilmistir. Ic listeler
degismedigi icin sutun sayisi ayni kalir.

Subject'teki negatif indeks ornegi:

```python
family[1:-2]
```

Sonuc:

```python
[
    [2.15, 102.7]
]
```

Shape:

```text
(1, 2)
```

## 9. Saf Python Listesinde Satir ve Sutun Secimi

Su ifade sadece satirlari secer:

```python
family[row_start:row_stop]
```

Sutunlari da secmek icin her satira ayri slicing uygulamak gerekir:

```python
submatrix = [
    row[column_start:column_stop]
    for row in matrix[row_start:row_stop]
]
```

Ornek:

```python
matrix = [
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]

submatrix = [row[1:4] for row in matrix[0:2]]
```

Sonuc:

```python
[
    [11, 12, 13],
    [21, 22, 23]
]
```

Orijinal shape `(3, 5)`, yeni shape `(2, 3)` olur.

## 10. NumPy ile Iki Eksenli Slicing

Asagidaki kodda `matrix`, bir degisken adidir; Python anahtar kelimesi
degildir:

```python
import numpy as np

matrix = np.array([
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
])
```

Bu rectangular array'in shape'i:

```text
(3, 5)
```

NumPy'da satirlar ve sutunlar ayni ifadede slice edilebilir:

```python
submatrix = matrix[0:2, 1:4]
```

Virgulun sol tarafi satirlari secer:

```python
0:2
```

Secilen satirlar:

```text
0 ve 1
```

Virgulun sag tarafi sutunlari secer:

```python
1:4
```

Secilen sutunlar:

```text
1, 2 ve 3
```

Sonuc:

```text
[[11 12 13]
 [21 22 23]]
```

Yeni shape:

```text
(2, 3)
```

Matematiksel olarak bu islem, belirli satir ve sutunlarin kesisiminden olusan
bir alt matris secimidir.

## 11. Python List ve NumPy Karsilastirmasi

NumPy:

```python
submatrix = matrix[row_slice, column_slice]
```

Ornek:

```python
submatrix = matrix[0:2, 1:4]
```

Saf Python listesi:

```python
submatrix = [
    row[column_start:column_stop]
    for row in matrix[row_start:row_stop]
]
```

Ornek:

```python
submatrix = [row[1:4] for row in matrix[0:2]]
```

Saf Python listesinde su kullanim desteklenmez:

```python
matrix[0:2, 1:4]
# TypeError
```

## Kisa Ozet

```text
sequence[start:stop]      -> Belirli bir araligi secer.
sequence[start:stop:step] -> Adim miktariyla birlikte secim yapar.
sequence[::-1]            -> Sequence'i ters cevirir.
family[start:end]         -> ex01'de yalnizca satirlari secer.
matrix[rows, columns]     -> NumPy'da satir ve sutunlari birlikte secer.
```

`ex01` icin temel islem yalnizca:

```python
result = family[start:end]
```

oldugu icin satir sayisi degisebilir, fakat rectangular input'un sutun sayisi
degismez.
