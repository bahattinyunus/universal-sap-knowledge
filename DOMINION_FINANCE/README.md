# 💰 DOMINION: FINANCE & CONTROLLING (FI/CO)

![Finance Banner](../_ASSETS/module_finance.png)

SAP FI/CO modülleri, kurumsal finansal yönetimin kalbidir. Bu bölümde modüllerin alt detaylarına ve kritik süreçlere odaklanıyoruz.

## 📁 Alt Başlıklar ve Süreçler

### 🏦 SAP FI (Financial Accounting)
Finansal muhasebe, dış raporlama ve yasal yükümlülükler için kullanılır.

#### 1. Genel Muhasebe (FI-GL)
*   **Ana Hesap Planı (Chart of Accounts):** Hesap kodlarının organizasyonu.
*   **Paralel Defter (Parallel Ledger):** IFRS ve VUK gibi farklı raporlama standartlarının aynı anda takibi.
*   **Yevmiye Kayıtları (FB01, FB50):** Günlük finansal işlemlerin sisteme girişi.

#### 2. Satıcılar Muhasebesi (FI-AP)
*   **Tedarikçi Master Verisi (FK01/BP):** Satıcı kartlarının yönetimi.
*   **Fatura Girişi (MIRO/FB60):** Satın alma faturalarının işlenmesi.
*   **Ödeme Programı (F110):** Otomatik toplu ödeme süreçleri.

#### 3. Müşteriler Muhasebesi (FI-AR)
*   **Müşteri Master Verisi (FD01/BP):** Müşteri kartları ve kredi limitleri.
*   **Tahsilat Yönetimi:** Gelen ödemelerin (banka ekstreleri) eşleştirilmesi.

#### 4. Duran Varlıklar Muhasebesi (FI-AA)
*   **Varlık Oluşturma (AS01):** Şirket demirbaşlarının kaydı.
*   **Amortisman Çalıştırma (AFAB):** Aylık değer kayıplarının hesaplanması.

### 📊 SAP CO (Controlling)
Yönetim muhasebesi, iç raporlama ve karar destek mekanizmaları içindir.

*   **Maliyet Merkezi (Cost Center) Muhasebesi:** Elektrik, personel gibi genel giderlerin departman bazlı takibi.
*   **İç Siparişler (Internal Orders):** Pazarlama kampanyası gibi geçici projelerin maliyet takibi.
*   **Karlılık Analizi (CO-PA):** Hangi segmentten (ürün, müşteri, bölge) ne kadar kar edildiğinin analizi.

## 🛠️ Kritik FI/CO İşlem Kodları
*   **FAGLB03:** Ana Hesap Bakiyesi Görüntüleme.
*   **FBL1N:** Satıcı Münferit Kalemleri Listesi.
*   **FBL5N:** Müşteri Münferit Kalemleri Listesi.
*   **FS00:** Ana Hesap Bakımı.

---
[🏠 Ana Sayfaya Dön](../README.md)
