# 📊 Veri Seti Analiz Yorumları

> **Veri Seti:** IBM HR Analytics — Çalışan İstifa Tahmini  
> **Kayıt Sayısı:** 1.471 çalışan · **Özellik Sayısı:** 21 kolon · **Hedef:** `Istifa` (Evet / Hayır)

---

## 🔍 Keşifsel Veri Analizi (EDA) Gözlemleri

### 1. Departman Dağılımı
- **Baskın departman:** Araştırma & Geliştirme
- Satış ve İnsan Kaynakları departmanları daha küçük
- 📌 Şirket profili teknoloji / AR-GE ağırlıklı görünüyor

### 2. Yaş Dağılımı
- 21–30 yaş aralığında yoğunlaşma var
- 50+ yaş grubu oldukça az
- 📌 **Genç ve dinamik** bir çalışan profili

### 3. Aylık Gelir
- Büyük çoğunluk düşük-orta gelir bandında (1.000–5.000 arası)
- Yüksek gelir grubu (15.000+) çok az
- 📌 Maaş dağılımı sağa çarpık — potansiyel istifa tetikleyicisi

### 4. Fazla Mesai
- Çalışanların önemli bir kısmı fazla mesai yapıyor
- 📌 Fazla mesai → tükenmişlik → istifa zinciri model tarafından öğrenilebilir

### 5. Hedef Değişken (İstifa Dengesi)
- **Hayır (Kalan):** ~%84
- **Evet (Ayrılan):** ~%16
- 📌 **Dengesiz sınıf** → Recall ve F1-Score odaklı değerlendirme gerektirir

### 6. Eğitim Alanı
- En yaygın: Yaşam Bilimleri, ardından Tıp ve Pazarlama
- 📌 Biyoteknoloji / sağlık sektörü profiliyle örtüşüyor

### 7. Medeni Durum
- Bekar çalışanlar çoğunlukta
- 📌 Bekar + genç kombinasyonu → daha yüksek hareket kabiliyeti

### 8. İş Seyahati
- "Nadiren seyahat" en yaygın kategori
- Sık seyahat edenler azınlıkta ama istifa oranı yüksek olabilir

### 9. Şirketteki Yıl
- 0–2 yıllık çalışanlar baskın grup
- 📌 Yeni işe girenlerde yüksek işten ayrılma eğilimi — **erken uyarı sistemi** kurulabilir

### 10. Evden Uzaklık
- Çalışanların büyük çoğunluğu 1–10 km mesafede
- Uzak mesafeli çalışanlar küçük grup ama yorgunluk riski yüksek

---

## ⚠️ İstifa Tahmininde Kritik Özellikler

| Özellik | Beklenen Etki |
|---------|--------------|
| **Fazla Mesai** | ↑ Evet → ↑ İstifa riski |
| **İş Memnuniyeti** | ↓ Düşük skor → ↑ Risk |
| **Maaş Artış Yüzdesi** | ↓ Düşük artış → ↑ Risk |
| **Son Terfi Süresi** | ↑ Uzun süre → ↑ Risk |
| **İş-Yaşam Dengesi** | ↓ Kötü denge → ↑ Risk |
| **Şirketteki Yıl** | 0–1 yıl → Yüksek risk |
| **Evden Uzaklık** | ↑ Uzak → ↑ Yorgunluk |
| **Toplam Çalışma Yılı** | Çok tecrübeli → dışarıdan teklif alabilir |

---

## 📈 Modelleme Notları

### Dengesiz Veri Problemi
- Hedef sınıf oranı ~84/16 → Model "Hayır" demeye meyilli olabilir
- **Çözüm:** `class_weight='balanced'` veya SMOTE uygulaması önerilir
- Metrik önceliği: `Recall` > `F1-Score` > `Accuracy`

### Kategorik Özellikler
- One-Hot Encoding sonrası kolon sayısı artacak
- `Departman`, `Eğitim Alanı`, `Medeni Durum` → Binary kolonlara dönüşür

### Beklenen Korelasyonlar
- `Toplam Çalışma Yılı` ↔ `Yaş` → Pozitif
- `İş Memnuniyeti` ↔ `Ortam Memnuniyeti` → İlişkili olabilir
- `Şirketteki Yıl` ↔ `Mevcut Müdürle Yıl` → Paralel gidebilir

---

## 💼 İş Değeri

Bu analiz sonucunda şirket yönetimine sunulabilecek çıktılar:

- 🔴 **Yüksek Risk Listesi:** Model tahminlerine göre istifa edebilecek çalışanlar
- 📊 **Departman Bazlı Risk Raporu:** Hangi bölümde istifa riski daha yüksek
- 🛠️ **Aksiyon Önerileri:** Fazla mesai düzenlemesi, maaş revizyonu, terfi planlaması
