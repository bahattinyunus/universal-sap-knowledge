# 🆘 SAP Sorun Giderme Rehberi (Troubleshooting)

Bu bölüm, SAP sisteminde en sık karşılaşılan hataların anlamlarını ve çözüm yollarını içerir.

---

## 🛠️ 1. ABAP Çalışma Zamanı Hataları (Dumps)

| Hata Kodu (ID) | Anlamı | Muhtemel Çözüm |
| :--- | :--- | :--- |
| **COMPUTE_INT_ZERODIVIDE** | Sıfıra bölme hatası. | Kodda bölen değerin sıfır olup olmadığını kontrol edin. |
| **TSV_TNEW_PAGE_ALLOC_FAILED** | Bellek (Memory) hatası. | Sorgunun çıktısını filtreleyin veya sistemi genişletin. |
| **MESSAGE_TYPE_X** | Kritik uygulama hatası. | `ST22` üzerinden dump detayına bakarak kısa dökümdeki açıklamayı okuyun. |
| **TIME_OUT** | İşlem süresi aşıldı. | Programı arkaplanda (`Background Job`) çalıştırın. |
| **COLLECT_OVERFLOW** | Hash tablosu limit aşımı. | `COLLECT` komutu yerine `APPEND` ve `SORT` kombinasyonunu deneyin. |

---

## 🔑 2. Yetki ve Kullanıcı Hataları

| Hata Mesajı | Sebep | Çözüm |
| :--- | :--- | :--- |
| **Authorization check failed** | Eksik yetki nesnesi. | `SU53` kodunu çalıştırın ve eksik nesneyi Basis ekibine bildirin. |
| **User locked due to failed logins** | Yanlış şifre denemesi. | `SU01` üzerinden yöneticinizden kilidi kaldırmasını isteyin. |
| **Client is locked** | Bakım veya güncelleme modu. | Basis ekibinin çalışmayı bitirmesini bekleyin. |

---

## 📦 3. Entegrasyon ve Veri Hataları

| Sorun | T-Code | Çözüm Adımları |
| :--- | :--- | :--- |
| **IDoc Hataları (Status 51)** | `WE02` / `WE05` | Hatalı segment verisini bulun ve `BD87` ile yeniden işleyin. |
| **BAPI Dönüş Mesajları** | `SE37` | BAPI'nin `RETURN` tablosundaki `E` (Error) tipi mesajları analiz edin. |
| **Update Terminated** | `SM13` | Veritabanı güncelleme hatasını bulun ve sebebini (`ABAP Dump` gibi) inceleyin. |

---

## 🌐 4. Teknik Bağlantı Hataları

| Hata | Sebep | Çözüm |
| :--- | :--- | :--- |
| **RFC Failure** | Bağlantı kesik. | `SM59` ile RFC bağlantısını test edin (`Connection Test`). |
| **ICM_HTTP_CONNECTION_FAILED** | Web servisi kapalı. | `SMICM` üzerinden servis durumunu kontrol edin. |
| **GATAWAY_ERROR** | Hub bağlantısı kopuk. | `SMGW` üzerinden gateway durumunu inceleyin. |

---

## 💡 Genel İpuçları
1.  **Hata Mesajına Tıklayın:** Ekranın altındaki kırmızı mesaj kutusuna çift tıklayarak detaylı açıklamayı ve uzun teknik metni okuyun.
2.  **S-Notes:** Hata kodunu [SAP Support Portal](https://support.sap.com/) üzerinden OSS Notu (Note) olarak aratın. En kesin çözümler buradadır.
3.  **Hata Ayıklama (Debug):** `/h` yazarak debugger modunu açın ve kodun nerede patladığını adım adım izleyin.

---
[🏠 Ana Sayfaya Dön](../README.md)
