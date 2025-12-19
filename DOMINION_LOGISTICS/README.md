# 📦 DOMINION: LOGISTICS & SUPPLY CHAIN (SD/MM/PP)

![Logistics Banner](../_ASSETS/module_logistics.png)

Lojistik dominionu, "Malzemeden Paraya" (Material to Cash) ve "İhtiyaçtan Satın Almaya" (Procure to Pay) süreçlerini kapsar.

## 📁 Alt Başlıklar ve Süreçler

### 🛒 SAP MM (Materials Management)
Malzeme ve stok yönetimi, satın alma süreçleri.

#### 1. Satın Alma (Purchasing)
*   **Satın Alma Talebi (BANF - ME51N):** Dahili ihtiyaç bildirimi.
*   **Teklif Talebi (RFQ - ME41):** Tedarikçilerden fiyat toplama.
*   **Satın Alma Siparişi (Purchase Order - ME21N):** Resmi sipariş belgesi.

#### 2. Stok Yönetimi (Inventory Management)
*   **Mal Girişi (GR - MIGO):** Tedarikçiden gelen malın depoya girişi.
*   **Mal Çıkışı (GI - MIGO):** Üretim veya satış için depodan mal çıkışı.
*   **Stok Transferi:** Depolar arası stok hareketi.

### 🚚 SAP SD (Sales & Distribution)
Satış, teslimat ve faturalama süreçleri.

#### 1. Satış Süreci (Order to Cash)
*   **Müşteri Siparişi (VA01):** Siparişin sisteme girişi.
*   **Nakliye/Teslimat (VL01N):** Ürünün hazırlanması ve depodan sevki.
*   **Faturalama (VF01):** Muhasebeleşme ve fatura kesimi.

### 🏭 SAP PP (Production Planning)
Üretim planlama ve kontrol.

*   **MRP (Material Requirements Planning):** Malzeme ihtiyaç planlaması (MD01).
*   **Üretim Siparişi (CO01):** Üretim emrinin oluşturulması ve teyidi.
*   **BOM (Bill of Materials - CS01):** Ürün reçetesi yönetimi.

## 🛠️ Kritik Lojistik İşlem Kodları
*   **MM03:** Malzeme Master Verisi Görüntüleme.
*   **MMBE:** Stok Özeti (Stock Overview).
*   **VA03:** Satış Siparişi Görüntüleme.
*   **MD04:** İhtiyaç/Stok Listesi.

---
[🏠 Ana Sayfaya Dön](../README.md)
