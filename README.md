# TEKNOFEST

## HAVACILIK, UZAY VE TEKNOLOJİ FESTİVALİ

## İNSANLIK YARARINA TEKNOLOJİLER YARIŞMASI

## TAKIM ADI

## Ordu Gençlik Merkezi

## PROJE ADI

## MAVERA


## İçindekiler

- 1. Proje Özeti
- 2. Proje Fikri
   - 2.1 Yerlilik ve Özgünlük Tarafı
      - 2.2 Hedef Kitle
- 3. Kullanılacak Yöntem
- 4. Proje Takvimi
- 5. Kaynakça


## 1. Proje Özeti

```
Gençlik Merkezine gelen üyelerin maske, ateş, HES kodu bilgilerinin kontrol
edilmesi, daha sonra bu verilerin gençlik merkezi tarafından oluşturulmuş bot
Telegram hesabına mesaj olarak atılması ve bir veri tabanında depolanması
amaçlanmıştır. Bunun amacı ise Covid- 19 virüsünün bulaşmasını engelleyecek
maske, ateş gibi etmenlerin kontrolünü sağlamakla birlikte kişinin pozitif çıkması
durumunda filyasyon ekiplerine bilgilerinin paylaşılmasıdır. Aynı zamanda
gençlik merkezinde kimler ile temaslı olup olmadığı bilgilerini tespit edip hızlı bir
müdahale olanağı sağlamaktır.
```
## 2 .Proje Fikri

```
Projenin fikir aşaması gençlik merkezinin bir sorunu ile ortaya çıkmıştır. Ordu
Gençlik Merkezine gelen gençlik merkezi üyeleri ve diğer misafirlerin pandemi
süresinde yaşadığı sorunların başında Covid- 19 semptomlarını taşıyıp taşımadığını
bilmemesi, gençlik merkezine gelen üyelerin pandemi koşulları kapsamında
gençlik merkezimin imkanlarından yararlandırmaktı. Ancak bu koşulları
sağlayabilmemiz için üyelerin ateşlerinin ölçülmesi, maske takıp takmadığının
kontrol edilmesi ve hayat eve sığar programından (HES) durumunun kontrol
edilmesi gerekmekteydi. Bu durumun insan olmadan çözümüne yoğunlaşarak
pandemi süresince ve sonrasında da Ordu Gençlik Merkezinde ve diğer devlet
kurumlarında kullanılmak üzere bir yazılım geliştirmek amaçlanmıştır. Gençlik
merkezinin kapısından giren her kişi için “ateşinin ölçülmesi, HES kodunun
kontrol edilmesi, maske takıp takmadığını kontrol ederek bu verileri gençlik
merkezine ait bir bot Telegram hesabına ve gençlik merkezine ait bir veri tabanına
depolanması amaçlanmıştır. Bunun yanında gerekli şartları sağlamayan kişilerin
tasarladığımız turnike sistemi sayesinde girişine izin verilmeyecektir. Böylelikle
hem pandemi süresince hem de pandemi bittikten sonra gençlik merkezimizde
kontrollü bir giriş-çıkış ve aynı zamanda güvenli bir ortam sağlanması
hedeflenmektedir.
```
### 2.1 Yerlilik ve Özgünlük Tarafı

```
Takım olarak üretebileceğimiz tüm parçaları tasarlayıp üretim aşaması
takımımız tarafından yapılacaktır. Projenin diğer projelerden farklı olarak
gerçek zamanlı tespit mantalitesi ile geliştirilmiş olup veri tabanında
depolama sağlayarak olası Covid- 19 durumlarında hızlı müdahale
sağlamaktadır.
```

#### 2.2 Hedef Kitle

```
Gençlik merkezleri, okullar, kamu kuruluşları ve toplu şekilde çalışılan
bütün kuruluşlarda projemizin kullanılması hedeflenmektedir.
```
## 3. Kullanılacak Yöntem

```
Proje ana kapsamında görüntü işleme ve derin öğrenme teknikleri olan YOLO
kullanılarak bir maske tespit yazılımı gerçekleştirilmesi hedeflenmektedir. Gerçek
zamanlı nesne tanıma ve hız gibi kavramları göz önünde tutarak nesne tanıma
yöntemleri içerisinden R-CNN ve benzeri algoritmalar ilk başta verilen görüntülerdeki
nesnelerin olabileceği muhtemel yerleri bulur. YOLO algoritması ise daha öncesinden
bir yer tahmini yapmaz, tüm görüntüyü bir kere evrişimsel sinir ağına verirsiniz ve size
çıktı olarak nesnelerin bulunduğu yeri, nesnenin sınıfını verir. Projenin bir diğer amacı
olan ateş ölçme aşamasında ise düşük maliyet ile en etkili çözüm yolu aranmıştır. Bu
sebepten dolayı Kızıl Ötesi Termometre kullanılması, sensor verisini işlemek için ise
Atmega 328P-U entegresi kullanılması düşünülmektedir. Mekanik tasarım solidworks
program tarafından tasarlanıp maliyet ve özgünlük kavramları dikkate alınarak plexi
madde kullanılması amaçlanmaktadır.
```
## 4. Proje Takvimi

## 5. Kaynakça

```
 K. Zhao, J. Kang, J. Jung and G. Sohn, "Building Extraction from Satellite
Images Using Mask R-CNN with Building Boundary Regularization," in CVPR,
2018.
```
```
 J. Dai, K. He and J. Sun, "Instance-Aware Semantic Segmentation via Multi-
task Network Cascades," in CVPR,2016.
```
```
 K. He, X. Zhang, S. Ren and J. Sun, "Deep Residual Learning for Image
Recognition," in CVPR 2016.
```
```
 T. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan and S. Belongie, "Feature
Pyramid Networks for Object Detection," in CVPR 2017.
```

