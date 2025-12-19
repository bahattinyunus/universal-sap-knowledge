# 📋 Standart Operasyon Prosedürleri (SOP)

Bu bölüm, SAP sisteminde sıkça karşılaşılan senaryolar için adım adım uygulama rehberlerini içerir.

---

## 🏗️ 1. Yeni Bir Malzeme Kartı Oluşturma (Procure-to-Pay Başlangıcı)
1.  **T-Code:** `MM01`
2.  **Sektör:** Endüstri türünü seçin (örn: Makine Mühendisliği).
3.  **Malzeme Türü:** ROH (Hammadde), HALB (Yarı Mamul) veya FERT (Mamul).
4.  **Görünümler:** Temel Veri 1, Satın Alma, Genel Fabrika Verileri ve Muhasebe 1.
5.  **Organizasyon Seviyeleri:** Üretim Yeri (Plant) ve Depo Yeri (Storage Location) bilgisini girin.
6.  **Kaydet:** Malzeme numarası sistem tarafından üretilecektir.

---

## 🛒 2. Satın Alma Siparişi ve Mal Kabulü
1.  **Sipariş Oluşturma:** `ME21N` ile tedarikçiyi ve malzemeyi seçip siparişi kaydedin.
2.  **Mal Kabulü:** `MIGO` işlem kodunu kullanın. İşlem türü: "Mal Kabulü", Referans: "Satın Alma Siparişi".
3.  **Kontrol:** "Kalem Tamam" (Item OK) check-box'ını işaretleyin ve "Kaydet"e basın.
4.  **Sonuç:** Stok bakiyesi (`MMBE`) güncellenecek ve muhasebe kaydı otomatik oluşacaktır.

---

## 📊 3. Ay Sonu Kapanış İşlemleri (Finans)
1.  **Girişlerin Kontrolü:** Tüm faturaların (`MIRO`/`VF01`) işlendiğinden emin olun.
2.  **Duran Varlıklar:** `AFAB` ile aylık amortismanı çalıştırın.
3.  **Maliyet Dağıtımı:** `KSV5` üzerinden masraf yerleri arası dağıtım yapın.
4.  **Dönem Kapatma:** `MMPV` (Lojistik) ve `OB52` (Finans) kodları ile ilgili ayı kapatıp yeni ayı açın.

---

## 🐞 4. ABAP Hata (Dump) Analizi
1.  **Log Görüntüleme:** `ST22` işlem koduna gidin.
2.  **Hata Seçimi:** İlgili tarih ve saatteki hataya çift tıklayın.
3.  **Analiz:** "Error analysis" ve "How to correct" bölümlerini okuyarak hatanın sebebini (örn: Zero Divide, Timeout) belirleyin.

---
[🏠 Ana Sayfaya Dön](../README.md)
