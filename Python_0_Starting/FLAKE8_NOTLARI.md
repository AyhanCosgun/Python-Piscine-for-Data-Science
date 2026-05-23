# Flake8 Kuralları Notları

Bu notlar Python Piscine subject'indeki şu kuralı anlamak için hazırlandı:

```text
Your code must follow the norm
pip install flake8
alias norminette=flake8
```

Flake8, tek başına yeni bir Python standardı değildir. Birkaç farklı kontrol aracını
tek komut altında çalıştıran bir lint aracıdır.

Varsayılan Flake8 temel olarak şunları kullanır:

- `pycodestyle`: PEP 8 stil kurallarını kontrol eder.
- `pyflakes`: kullanılmayan import, tanımsız değişken gibi mantıksal problemleri yakalar.
- `mccabe`: fonksiyonların karmaşıklığını kontrol edebilir.

## Nasıl Çalıştırılır?

Kurulum:

```bash
python3 -m pip install flake8
```

Tek dosya kontrolü:

```bash
flake8 whatis.py
```

Klasör kontrolü:

```bash
flake8 .
```

Subject'teki `norminette` alias'i:

```bash
alias norminette=flake8
```

Bundan sonra şunu yazabilirsin:

```bash
norminette whatis.py
```

Çıktı yoksa genellikle problem yok demektir. Flake8 hata bulursa dosya adı, satır,
sütun ve hata kodu gösterir.

Örnek:

```text
whatis.py:4:1: E302 expected 2 blank lines, found 1
```

Bu şu anlama gelir:

- Dosya: `whatis.py`
- Satır: `4`
- Sütun: `1`
- Hata kodu: `E302`
- Açıklama: function/class tanımından önce 2 boş satır bekleniyor

## Hata Kodları Ne Anlama Gelir?

Flake8 hata kodları genellikle harf + sayı formatındadır.

```text
E...   pycodestyle error
W...   pycodestyle warning
F...   pyflakes error
C90... mccabe complexity
```

## Sık Görülen E Kodları

`E` kodları genellikle PEP 8 stil sorunlarıdır.

### E302

Function veya class tanımından önce iki boş satır olmalı.

Kötü:

```python
import sys
def main():
    pass
```

İyi:

```python
import sys


def main():
    pass
```

### E305

Function veya class tanımından sonra gelen top-level koddan önce iki boş satır
olmalı.

Kötü:

```python
def main():
    pass
if __name__ == "__main__":
    main()
```

İyi:

```python
def main():
    pass


if __name__ == "__main__":
    main()
```

### E501

Satır çok uzun.

Kötü:

```python
print("This is a very very very very very very very very very very very long line")
```

Daha iyi:

```python
print(
    "This is a very very very very very very "
    "very very very very very long line"
)
```

Flake8'in varsayılan satır uzunluğu genellikle 79 karakterdir.

### E225

Operatör çevresinde boşluk eksik.

Kötü:

```python
x=42
```

İyi:

```python
x = 42
```

### E231

Virgülden sonra boşluk eksik.

Kötü:

```python
numbers = [1,2,3]
```

İyi:

```python
numbers = [1, 2, 3]
```

### E261

Inline comment öncesinde en az iki boşluk olmalı.

Kötü:

```python
x = 42 # answer
```

İyi:

```python
x = 42  # answer
```

### E303

Çok fazla boş satır var.

Kötü:

```python
def main():



    pass
```

İyi:

```python
def main():
    pass
```

## Sık Görülen W Kodları

`W` kodları stil uyarılarıdır.

### W291

Satır sonunda gereksiz boşluk var.

Kötü:

```python
import sys 
```

İyi:

```python
import sys
```

### W292

Dosya sonunda newline yok.

Kötü:

```text
Son satırdan sonra dosya direkt bitiyor.
```

İyi:

```text
Son satırdan sonra newline var.
```

### W293

Boş satırda whitespace var.

Bu, boş görünen satırda aslında space veya tab bulunmasıdır.

## Sık Görülen F Kodları

`F` kodları `pyflakes` tarafındandır. Bunlar stil probleminden çok gerçek hata
riski taşır.

### F401

Import edilmiş ama kullanılmamış.

Kötü:

```python
import sys


def main():
    print("hello")
```

İyi:

```python
def main():
    print("hello")
```

### F821

Tanımsız isim kullanılmış.

Kötü:

```python
print(number)
```

Eğer `number` daha önce tanımlanmadıysa Flake8 bunu yakalar.

İyi:

```python
number = 42
print(number)
```

### F841

Yerel değişken atanmış ama kullanılmamış.

Kötü:

```python
def main():
    number = 42
    print("hello")
```

İyi:

```python
def main():
    number = 42
    print(number)
```

## C90 / McCabe Karmaşıklığı

`mccabe`, fonksiyonun çok fazla dallanıp dallanmadığını kontrol eder.

Örneğin çok fazla `if`, `elif`, `for`, `while`, `try` kullanımı fonksiyonu karmaşık
hale getirebilir.

Flake8 normalde `--max-complexity` verilmeden bu kontrolü sıkı kullanmayabilir.

Örnek:

```bash
flake8 --max-complexity 10 .
```

Bu, karmaşıklığı 10'dan fazla olan fonksiyonları raporlar.

## Piscine İçin Pratik Kurallar

Küçük egzersizlerde şu alışkanlıklar çoğu Flake8 problemini engeller:

1. Importlardan sonra iki boş satır bırak.
2. Top-level fonksiyonlar arasında iki boş satır bırak.
3. Operatörlerin etrafına boşluk koy.
4. Virgülden sonra boşluk koy.
5. Satır sonlarında gereksiz boşluk bırakma.
6. Kullanmadığın importları sil.
7. Kullanmadığın değişkenleri bırakma.
8. Çok uzun satırları böl.
9. Dosyanın sonunda newline olsun.
10. Ex05 ve sonrası için `main()` ve `if __name__ == "__main__":` yapısını kullan.

## Örnek Flake8 Uyumlu whatis.py

```python
import sys


def main(args):
    """Check whether the provided integer argument is even or odd."""
    if len(args) == 1:
        return

    if len(args) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        number = int(args[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main(sys.argv)
```

## Önemli Not

Flake8 sadece kod stilini ve bazı basit hataları yakalar. Programın doğru sonucu
verdiğini garanti etmez.

Bu yüzden iki ayrı kontrol yapmak gerekir:

```bash
flake8 whatis.py
python3 whatis.py 14
python3 whatis.py Hi!
python3 whatis.py 13 5
```

Flake8 temiz olsa bile program yanlış çalışabilir. Program doğru çalışsa bile Flake8
hatası alabilir. Teslimden önce ikisini de kontrol etmek gerekir.
