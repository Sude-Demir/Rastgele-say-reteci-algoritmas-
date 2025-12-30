CPLM (Collatz Parity Logic Machine) - Rastgele Sayı Üretici (RSÜ)
Bu proje, Collatz Teorisi tabanlı, yüksek istatistiksel kaliteye sahip ve kriptografik düzeyde rastgelelik hedefleyen özgün bir Rastgele Dizi Üretme (RSÜ) algoritmasıdır.
CPLM, çift motorlu yapısı ve gelişmiş filtreleme teknikleriyle 0 ve 1 dağılım dengesini mükemmel bir şekilde sağlar.

🚀 Öne Çıkan Özellikler
Collatz Teoremi Tabanlı Entropi: Kaotik sayı dizileri üretmek için matematiksel Collatz iterasyonlarını kullanır.

Dual-Motor Mimarisi: İki bağımsız Collatz motoru (Motor A ve Motor B) paralel çalışarak karmaşıklığı artırır.

Cross-Link Etkileşimi: Motorlar arası veri transferi (XOR geçişleri) ile "state" (durum) uzayı sürekli güncellenir.

Von Neumann Deskewing: Üretilen bitler, istatistiksel taraflılığı (bias) yok etmek için Von Neumann filtrelemesinden geçirilerek %50/%50 (0/1) dengesine yaklaştırılır.

İstatistiksel Test Desteği: NIST standartlarına benzer Ki-Kare, Runs ve Seri testlerini içerir.

🛠 Çalışma Mantığı

Başlangıç (Seeding): Algoritma, yüksek güvenliğe sahip secrets kütüphanesi ile 1024-bitlik iki farklı başlangıç durumu üretir.

İterasyon: Motorlar Collatz kuralına ($3n+1$) göre dönerken, her 8 adımda bir birbirlerine veri aktarımı (cross-link) yaparlar.

Bit Çıkarımı: Motorların o anki durumlarının pariteleri (tek/çift) XOR işlemine sokularak ham bit dizisi elde edilir.

Filtreleme: 00 ve 11 çiftleri atılır, 01 -> 0 ve 10 -> 1 olarak kabul edilerek istatistiksel denge sağlanır.

📊 İstatistiksel Başarı Raporu
Yapılan testlerde algoritma aşağıdaki sonuçları başarıyla geçmektedir:

✅ Ki-Kare (Frekans) Testi: 0 ve 1 sayılarının eşitliği doğrulanmıştır.

✅ Runs (Dizi) Testi: Bit değişim frekansı rastgelelik sınırları içerisindedir.

✅ Seri Test: İkili bit kombinasyonlarının (00, 01, 10, 11) dağılımı homojendir.
