# Python Piscine - Python 2 DataTable Proje Bağlamı

Bu belge, depo kökündeki `Python_2_Datatable.pdf` subjectinin ayrıntılı
özetidir. Başka bir sohbet oturumunda bu dosya yüklenerek projenin amacı,
zorunlu kuralları, alıştırmaları ve değerlendirme riskleri hızla yeniden
bağlama alınabilir.

## 1. Kaynak ve kapsam

- Kaynak dosya: `Python_2_Datatable.pdf`
- Subject başlığı: `Training Piscine Python for datascience - 2 / DataTable`
- Subject sürümü: `1.00`
- PDF tarihi: 24 Mart 2023
- PDF uzunluğu: 10 sayfa
- Bu bağlam belgesinin oluşturulma tarihi: 13 Haziran 2026
- Projenin ana konusu: CSV veri kümelerini yüklemek, dönüştürmek, seçmek ve
  Matplotlib/Seaborn benzeri araçlarla görselleştirmek.
- Veri kaynağı: Gapminder.org tarafından sağlanan, CC-BY lisanslı eğitim
  materyalleri.

PDF nihai otoritedir. Bu belgede:

- **Zorunlu** denilen maddeler subjectte açıkça yazan kurallardır.
- **Örnekten çıkarım** denilen maddeler PDF'deki ekran görüntülerinden
  gözlemlenen davranışlardır; birebir biçim zorunluluğu değildir.
- **Öneri** denilen maddeler güvenli ve değerlendirici dostu uygulama
  tavsiyeleridir; subjectin doğrudan şartı değildir.

## 2. Projenin kısa özeti

Proje dört alıştırmadan oluşur:

1. `ex00`: Genel amaçlı ve hataya dayanıklı CSV yükleme fonksiyonu.
2. `ex01`: Kampüs ülkesinin yıllara göre yaşam beklentisi çizgi grafiği.
3. `ex02`: Kampüs ülkesi ile seçilen başka bir ülkenin 1800-2050 nüfus
   karşılaştırması.
4. `ex03`: 1900 yılında ülkelerin kişi başı gelir/GDP değerleri ile yaşam
   beklentileri arasındaki ilişkinin saçılım grafiği.

## 3. Depo durumu

13 Haziran 2026 tarihindeki inceleme anında depo kökünde şunlar bulunuyordu:

```text
Python_2_datatable/
├── Python_2_Datatable.pdf
├── ex00/
├── ex01/
├── ex02/
└── ex03/
```

Alıştırma dizinleri boştu ve CSV veri dosyaları henüz depoda yoktu.

## 4. Tüm alıştırmalar için zorunlu genel kurallar

### 4.1 Çalışma ve teslim ortamı

- Çalışma cluster bilgisayarında, doğrudan veya gerekli yazılımları kurulmuş
  bir sanal makinede yapılmalıdır.
- Değerlendirmeden önce gereken tüm yazılımlar kurulmuş olmalıdır.
- Yalnızca atanmış Git deposunda bulunan çalışma değerlendirilir.
- Deepthought değerlendirmesinde bir bölüm hata verirse değerlendirme durur.
- Savunma/değerlendirme, değerlendirilen grubun bilgisayarında yapılır.
- Dizin ve dosya isimleri subjectte yazdığı biçimde olmalıdır.

### 4.2 Python ve import kuralları

- Python sürümü zorunlu olarak `3.10` olmalıdır.
- Importlar açık olmalıdır. Örnek: `import numpy as np`.
- Wildcard import yasaktır. Örnek: `from pandas import *`.
- Wildcard import kullanmak ilgili alıştırmadan `0` alınmasına yol açar.
- Subject, alıştırmada özel olarak yasaklanmamış built-in fonksiyonların
  kullanılmasına izin verir.
- Global değişken kullanılmamalıdır.

### 4.3 Program yapısı

- Global scope içinde çalışan uygulama kodu bulunmamalıdır; işler fonksiyonlar
  içinde yapılmalıdır.
- Her çalıştırılabilir program bir `main()` fonksiyonuna sahip olmalıdır.
- Her program şu giriş kalıbını kullanmalıdır:

```python
def main():
    """Run the program."""
    # Tests and error handling.


if __name__ == "__main__":
    main()
```

- Tüm fonksiyonların docstring'i, yani `__doc__` içeriği olmalıdır.
- Kod `flake8` normuna uymalıdır.
- Subjectin önerdiği kurulum/kısayol:

```bash
pip install flake8
alias norminette=flake8
```

### 4.4 Hata yönetimi

- Yakalanmamış herhangi bir exception alıştırmayı geçersiz kılar.
- Bu kural, özellikle hata üretmesi istenen test senaryolarında da geçerlidir.
- Program beklenmedik biçimde sonlanmamalıdır.
- Hatalı dosya yolu, hatalı biçim, okunamayan veri, bulunamayan ülke/sütun gibi
  makul hata durumları uygulama seviyesinde ele alınmalıdır.
- Subject, `ex00` için hata halinde açıkça `None` döndürülmesini ister.

### 4.5 Test yaklaşımı

- Test dosyaları zorunlu teslim değildir ve notlandırılmaz.
- Subject yine de savunmada kullanılmak üzere yerel testler hazırlanmasını
  kuvvetle önerir.
- Teslim dışı testler, geçerli veri kadar bozuk yol ve bozuk veri durumlarını
  da kapsamalıdır.

## 5. Teslim matrisi

| Alıştırma | Dizin | Teslim edilecek dosyalar | Temel veri |
|---|---|---|---|
| 00 | `ex00/` | `load_csv.py` | Çağıranın verdiği CSV |
| 01 | `ex01/` | `load_csv.py`, `aff_life.py` | `life_expectancy_years.csv` |
| 02 | `ex02/` | `load_csv.py`, `aff_pop.py` | `population_total.csv` |
| 03 | `ex03/` | `load_csv.py`, `projection_life.py` | Gelir/GDP CSV'si ve yaşam beklentisi CSV'si |

Her alıştırma kendi dizininde bir `load_csv.py` ister. Önceki alıştırmanın
çözümünü sonraki dizine kopyalamak veya aynı davranışı koruyarak yeniden
kullanmak gerekir.

## 6. Exercise 00 - Load my Dataset

### 6.1 Zorunlu teslim

- Dizin: `ex00/`
- Dosya: `load_csv.py`
- İzin verilen araçlar: `pandas` veya veri kümesi manipülasyonu yapan başka
  bir kütüphane.

### 6.2 İstenen API

Subjectteki kavramsal imza:

```python
def load(path: str) -> Dataset:
    """Load and return a dataset."""
```

`Dataset` yer tutucudur. Kullanılan kütüphaneye göre gerçek dönüş tipi
uyarlanmalıdır. Pandas seçilirse güvenli tip ifadesi pratikte
`pd.DataFrame | None` olabilir.

### 6.3 Zorunlu davranış

- Fonksiyon dosya yolunu `str` olarak alır.
- Veri kümesini yükler.
- Yüklenen veri kümesinin boyutlarını terminale yazar.
- Veri kümesini döndürür.
- Hatalı yol, hatalı dosya biçimi vb. hata durumlarını yakalar.
- Hata durumunda `None` döndürür.
- Exception çağırana kaçmamalıdır.

Subjectin örnek başarılı mesajı:

```text
Loading dataset of dimensions (195, 302)
```

Ardından tester, dönen DataFrame'i `print()` ile gösterir. Subject veri
kümesinin terminaldeki tablo biçiminin birebir aynı olmasını istemez ve
"Dataset'i istediğiniz formatta gösterebilirsiniz" der.

### 6.4 Subjectteki örnek tester

```python
from load_csv import load

print(load("life_expectancy_years.csv"))
```

### 6.5 Güvenli uygulama önerileri

- `pandas.read_csv(path)` kullan.
- Başarılı okumadan sonra `dataset.shape` değerini yazdır.
- En azından dosya sistemi, parser ve veri biçimi kaynaklı beklenen
  exception'ları yakala.
- Kullanıcıya kısa ve anlaşılır hata mesajı ver; traceback sızdırma.
- Fonksiyon içinde yalnızca yükleme sorumluluğunu tut.
- `main()` içinde başarılı ve başarısız örnek çağrılar test edilebilir.

### 6.6 Değerlendirme kontrolü

- Geçerli CSV, DataFrame döndürüyor mu?
- Mesajda doğru `(satır, sütun)` boyutu var mı?
- Olmayan yol `None` döndürüyor mu?
- Geçersiz/okunamayan dosya exception fırlatmadan `None` döndürüyor mu?
- `load.__doc__` dolu mu?
- Dosya doğrudan çalıştırıldığında yakalanmamış exception oluşuyor mu?

## 7. Exercise 01 - Draw my Country

### 7.1 Zorunlu teslim

- Dizin: `ex01/`
- Dosyalar: `load_csv.py`, `aff_life.py`
- İzin verilen araçlar: `matplotlib`, `seaborn` veya başka bir veri
  görselleştirme kütüphanesi.

### 7.2 Zorunlu davranış

- Önceki alıştırmadaki `load()` fonksiyonu çağrılmalıdır.
- `life_expectancy_years.csv` yüklenmelidir.
- Kampüsün bulunduğu ülkeye ait yaşam beklentisi bilgisi gösterilmelidir.
- Grafik bir başlığa sahip olmalıdır.
- X ve Y eksenlerinin açıklayıcı etiketleri olmalıdır.

Subject Fransa kampüsünü örnek verir. Türkiye'deki bir 42 kampüsü için doğal
ülke seçimi `Turkey` olur; ancak gerçek CSV'deki ülke anahtarı kontrol
edilmeden sabit varsayım yapılmamalıdır.

### 7.3 PDF örneğinden gözlemler

Örnek Fransa grafiği:

- Bir çizgi grafiğidir.
- Başlık: `France Life expectancy Projections`
- X ekseni: `Year`
- Y ekseni: `Life expectancy`
- Veri yaklaşık 1800-2100 aralığını kapsar.
- Tek ülke serisi bulunduğu için örnekte ayrı bir seri legend'i görünmez.

Başlık metninin, renklerin, figür boyutunun ve tick aralıklarının birebir
kopyalanması subjectte zorunlu değildir.

### 7.4 Beklenen veri dönüşümü

- `country` sütunundan kampüs ülkesi satırı seçilir.
- İlk sütun ülke ismidir; kalan sütun adları yıllardır.
- Yıl sütun adları çizim için sayısal X değerlerine dönüştürülür.
- Seçilen satırdaki yaşam beklentileri sayısal Y değerlerine dönüştürülür.
- Grafik `plt.show()` benzeri bir çağrıyla gösterilir.

### 7.5 Hata durumları

- CSV yüklenemezse çizime devam edilmemeli.
- `country` sütunu yoksa hata kullanıcıya kontrollü biçimde bildirilmelidir.
- Kampüs ülkesi bulunamazsa yakalanmamış `KeyError`/`IndexError`
  oluşmamalıdır.
- Yıl veya değer dönüşümü başarısızsa exception dışarı kaçmamalıdır.

### 7.6 Değerlendirme kontrolü

- `aff_life.py`, `load_csv.load()` kullanıyor mu?
- Doğru dosya adı yükleniyor mu?
- Doğru ülke seçiliyor mu?
- Yıllar kronolojik ve sayısal eksende mi?
- Başlık, X etiketi ve Y etiketi var mı?
- Programda `main()` ve main guard var mı?
- Tüm fonksiyonlar docstring içeriyor mu?

## 8. Exercise 02 - Compare my Country

### 8.1 Zorunlu teslim

- Dizin: `ex02/`
- Dosyalar: `load_csv.py`, `aff_pop.py`
- İzin verilen araçlar: `matplotlib`, `seaborn` veya başka bir veri
  görselleştirme kütüphanesi.

### 8.2 Zorunlu davranış

- `load()` fonksiyonu ilk alıştırmadan kullanılmalıdır.
- `population_total.csv` yüklenmelidir.
- Kampüs ülkesinin nüfusu, seçilen başka bir ülkeyle karşılaştırılmalıdır.
- Yalnızca `1800` ile `2050` arasındaki yıllar gösterilmelidir.
- Grafik başlığı bulunmalıdır.
- X ve Y eksenleri etiketlenmelidir.
- Her iki çizginin hangi ülkeye ait olduğunu gösteren legend bulunmalıdır.

Aralığın değerlendirmede en güvenli yorumu iki sınırın da dahil olmasıdır:
`1800 <= year <= 2050`.

### 8.3 PDF örneğinden gözlemler

Örnek karşılaştırma Fransa ve Belçika arasındadır:

- Başlık: `Population Projections`
- X ekseni: `Year`
- Y ekseni: `Population`
- İki farklı renkte çizgi vardır.
- Legend'de `Belgium` ve `France` görünür.
- Y ekseni değerleri `20M`, `40M`, `60M` gibi okunabilir kısaltmalarla
  gösterilir.

`M` biçimlendirmesi örnekte vardır; subject metni bunu açıkça zorunlu kılmaz.
Yine de okunabilirlik ve yaygın 42 değerlendirme beklentisi açısından
uygulanması önerilir.

### 8.4 Beklenen veri dönüşümü

- İki ülkenin satırları `country` sütunundan seçilir.
- Sütun adlarından yalnızca 1800-2050 yılları alınır.
- `population_total.csv` değerleri `20M`, `1.5B`, `800k` gibi metinler
  içerebileceğinden sayıya dönüştürme gerekebilir.
- Her ülke aynı X yıl dizisi üzerinde ayrı çizgi olarak çizilir.
- Her çizgiye `label=<ülke>` verilerek legend üretilir.

### 8.5 Nüfus değerlerini ayrıştırma önerisi

Veri kümesinin gerçek içeriği kontrol edilmelidir. Kısaltma varsa:

- `k` -> `1_000`
- `M` -> `1_000_000`
- `B` -> `1_000_000_000`

Dönüşüm fonksiyonu:

- Docstring içermeli.
- Sayısal girdiyi zaten sayısalsa kabul edebilmeli.
- String girdiyi temizleyip suffix'e göre çarpabilmeli.
- Beklenmeyen veya eksik değeri kontrollü ele almalı.

### 8.6 Değerlendirme kontrolü

- `aff_pop.py`, `load_csv.load()` kullanıyor mu?
- `population_total.csv` doğru adla açılıyor mu?
- Kampüs ülkesi ve ikinci ülke gerçekten bulunuyor mu?
- Grafik 1800 öncesi veya 2050 sonrası veri içeriyor mu?
- İki çizgi, iki ülke etiketi ve legend var mı?
- Y değerleri doğru ölçeğe çevrilmiş mi?
- Başlık ve iki eksen etiketi var mı?
- Hata durumları exception kaçırmadan ele alınıyor mu?

## 9. Exercise 03 - Draw my Year

### 9.1 Zorunlu teslim

- Dizin: `ex03/`
- Dosyalar: `load_csv.py`, `projection_life.py`
- İzin verilen araçlar: `matplotlib`, `seaborn` veya başka bir veri
  görselleştirme kütüphanesi ve `ex00` veri yükleme kütüphanesi.

### 9.2 Zorunlu veri dosyaları

Tam dosya adları:

```text
income_per_person_gdppercapita_ppp_inflation_adjusted.csv
life_expectancy_years.csv
```

Uzun gelir dosyası adı harf harfine korunmalıdır.

### 9.3 Zorunlu davranış

- İki dosya da `load()` ile yüklenmelidir.
- Yalnızca `1900` yılı kullanılmalıdır.
- Her ülke için 1900 yaşam beklentisi ile 1900 gelir/GDP değeri
  ilişkilendirilmelidir.
- Sonuç bir grafik üzerinde gösterilmelidir.
- Grafik başlığı bulunmalıdır.
- X ve Y eksenleri etiketlenmelidir.
- Subject metni ayrıca "her grafik için legend" ister.
- Program, yaşam süresi ile gayrisafi yurtiçi hasıla arasında korelasyon olup
  olmadığını görsel olarak inceletir.

### 9.4 PDF örneğinden gözlemler

Örnek:

- Bir scatter/saçılım grafiğidir.
- Her nokta bir ülkeyi temsil eder.
- Başlık: `1900`
- X ekseni: `Gross domestic product`
- Y ekseni: `Life Expectancy`
- X ekseni logaritmiktir; görünen ana işaretler yaklaşık `300`, `1k`, `10k`.
- Y ekseni yaklaşık 20-55 aralığındadır.
- Noktalar genel olarak sağa gidildikçe yükselir.
- Örnekte görünür bir seri legend'i yoktur.

Subjectin "legend for each graph" ifadesi ile kendi örneği arasında belirsizlik
vardır. Değerlendirme açısından başlık ve eksen etiketleri kesinlikle
bulunmalı; tek scatter serisine anlamlı bir `label` verip legend eklemek
subject metnine daha sıkı uyum sağlar.

### 9.5 Beklenen veri birleştirme mantığı

- Her iki DataFrame'de `country` ve `1900` sütunları seçilir.
- `1900` sütunları anlamlı adlarla yeniden adlandırılır; örneğin `income` ve
  `life_expectancy`.
- İki tablo `country` üzerinden inner join/merge ile birleştirilir.
- Eksik veya sayıya çevrilemeyen değerler çizimden önce elenir.
- Gelir değerlerindeki `k`, `M`, `B` gibi suffix'ler varsa sayıya çevrilir.
- Kalan her ülke için `(income, life_expectancy)` noktası çizilir.
- X ekseni için log ölçek kullanmak PDF örneğine uygundur:
  `plt.xscale("log")`.

İki tablonun satır sıralarının aynı olduğu varsayılıp doğrudan iki Series'i
eşleştirmek risklidir. Ülke adına göre merge etmek doğru ve dayanıklı
yaklaşımdır.

### 9.6 Korelasyonun yorumu

PDF örneğine göre 1900 yılında kişi başı gelir/GDP yükseldikçe yaşam beklentisi
genel olarak yükselir. Bu, pozitif bir korelasyon görünümüdür. Ancak:

- Saçılım belirgindir.
- Korelasyon nedensellik anlamına gelmez.
- Tek yıl ve ülkeler arası gözlem, tek başına nedensel sonuç üretmez.

### 9.7 Değerlendirme kontrolü

- İki dosya da tam doğru adla `load()` üzerinden açılıyor mu?
- Yalnızca 1900 sütunu kullanılıyor mu?
- Ülkeler isim üzerinden doğru eşleştiriliyor mu?
- Eksik ve geçersiz değerler temizleniyor mu?
- Grafik gerçekten scatter mı?
- Başlıkta 1900 açık mı?
- X ve Y eksen etiketleri anlamlı mı?
- X ekseni örneğe uygun log ölçekte mi?
- Subject metnine uyum için legend değerlendirilmiş mi?
- Program yakalanmamış exception üretmeden kapanıyor mu?

## 10. Önerilen kod organizasyonu

Subject dosya isimlerini sınırlar; aşağıdaki organizasyon bu sınırlar içinde
uygundur:

```text
ex00/
└── load_csv.py

ex01/
├── load_csv.py
└── aff_life.py

ex02/
├── load_csv.py
└── aff_pop.py

ex03/
├── load_csv.py
└── projection_life.py
```

Önerilen sorumluluklar:

- `load_csv.py`
  - `load(path)`: CSV'yi yükler, boyutu yazar, DataFrame veya `None` döndürür.
  - `main()`: Yalnızca yerel test/smoke test işlevi görür.
- `aff_life.py`
  - Veri seçme ve yaşam beklentisi çizme fonksiyonları.
  - `main()`: Yükleme, doğrulama ve çizim akışını yönetir.
- `aff_pop.py`
  - Gerekirse nüfus metnini sayıya çeviren yardımcı fonksiyon.
  - Ülke karşılaştırma çizim fonksiyonu.
  - `main()`: Yükleme, doğrulama ve çizim akışını yönetir.
- `projection_life.py`
  - Gerekirse gelir değerini sayıya çeviren yardımcı fonksiyon.
  - 1900 tablolarını merge eden fonksiyon.
  - Scatter grafiğini çizen fonksiyon.
  - `main()`: İki yükleme, doğrulama, birleştirme ve çizim akışını yönetir.

Subject "global variable yok" dediği için ülke adı, dosya adı ve yıl gibi
değerleri modül seviyesinde değişken olarak tutmak yerine `main()` içinde veya
fonksiyon parametresi olarak taşımak en katı uyum yaklaşımıdır.

## 11. Önerilen geliştirme sırası

1. `ex00/load_csv.py` tamamlanır.
2. Geçerli CSV, olmayan dosya ve bozuk CSV ile `load()` test edilir.
3. Aynı `load_csv.py` sonraki alıştırma dizinlerine aktarılır.
4. Gerçek CSV sütun adları ve değer biçimleri terminalden incelenir.
5. `ex01` için tek ülke seçimi ve çizgi grafiği yapılır.
6. `ex02` için nüfus parser'ı ve 1800-2050 filtresi yapılır.
7. `ex03` için ülke bazlı merge, veri temizliği ve log ölçekli scatter yapılır.
8. Her dosya `flake8` ile kontrol edilir.
9. Her çalıştırılabilir dosya Python 3.10 ile doğrudan çalıştırılır.
10. Hata senaryolarında traceback/uncaught exception olmadığı doğrulanır.

## 12. Subjectin zorunlu kılmadığı ayrıntılar

Aşağıdakiler PDF örneğine benzetilebilir fakat açık zorunluluk değildir:

- Çizgi renklerinin birebir aynı olması.
- Figür boyutunun birebir aynı olması.
- Başlık cümlesinin örnekle harf harfine aynı olması.
- Tick aralıklarının birebir aynı olması.
- Grid kullanımı.
- Belirli Matplotlib stili.
- DataFrame'in terminalde belirli bir görünümde yazdırılması.

Zorunlu olan veri seçiminin doğruluğu, istenen yıl/ülke kapsamı, başlık,
eksen açıklamaları, gerekli legend ve hatasız çalışmadır.

## 13. Başka oturum için hızlı yükleme talimatı

Yeni bir sohbette bu dosyayı yükledikten sonra şu istem kullanılabilir:

```text
PYTHON_2_DATATABLE_CONTEXT_TR.md dosyasını proje bağlamı olarak oku.
Python_2_Datatable.pdf nihai otorite olsun. Önce mevcut ex00-ex03
dosyalarını incele, sonra subject kurallarına, Python 3.10'a, flake8'e,
main guard/docstring şartlarına ve yakalanmamış exception yasağına göre
çalışmaya devam et. Belgede "öneri" olarak işaretlenen maddeleri zorunlu
subject kuralı gibi değerlendirme.
```

## 14. Uygulama başlamadan çözülmesi gereken açık noktalar

- Kampüs ülkesi kesin olarak hangisi? Türkiye ise CSV anahtarı `Turkey` mi?
- `ex02` karşılaştırma için hangi ikinci ülke seçilecek?
- CSV dosyaları nerede tutulacak ve değerlendirme anında çalışma dizini ne
  olacak?
- Gerçek CSV değerleri düz sayı mı, yoksa `k/M/B` suffix'li string mi?
- Değerlendirici ex03'te tek scatter serisi için görünür legend bekliyor mu?

Bu noktalar subjectin temel çözümünü engellemez; gerçek veri dosyaları ve kampüs
bilgisi görüldüğünde doğrulanmalıdır.
