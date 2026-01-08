# 📊 Veri Seti Hakkında Basit Yorumlar

## Genel Bakış
- **Toplam Kayıt:** 1471 çalışan
- **Toplam Özellik:** 21 kolon
- **Hedef Değişken:** Istifa (Evet/Hayır)

---

## 🔍 Basit Gözlemler

### 1. Departmanlar
- **En yaygın:** Araştırma ve Geliştirme (çok fazla)
- **Diğerleri:** Satış, İnsan Kaynakları
- **Yorum:** Şirket teknoloji/AR-GE ağırlıklı görünüyor

### 2. Yaş Dağılımı
- **Gençler:** 21-30 yaş arası çok var
- **Orta yaş:** 30-45 arası yoğun
- **Yaşlılar:** 50+ az
- **Yorum:** Genç bir çalışan profili var

### 3. Maaş (Aylık Gelir)
- **Düşük:** 1000-3000 TL arası çok fazla
- **Orta:** 4000-10000 TL arası
- **Yüksek:** 15000+ TL çok az
- **Yorum:** Genel olarak düşük-orta gelirli çalışanlar

### 4. Fazla Mesai
- **Evet yapanlar:** Oldukça fazla
- **Hayır diyenler:** Daha az
- **Yorum:** Fazla mesai şirkette yaygın

### 5. İstifa Durumu (Hedef)
- **Hayır (Kalan):** Çoğunluk
- **Evet (Ayrılan):** Azınlık
- **Yorum:** Normal bir işten ayrılma oranı (dengesiz veri)

### 6. Eğitim Alanları
- **En yaygın:** Yaşam Bilimleri
- **Diğerleri:** Tıp, Pazarlama, Teknik Derece
- **Yorum:** Biyoteknoloji/sağlık şirketi olabilir

### 7. Medeni Durum
- **Bekar:** Çok fazla
- **Evli:** Orta düzeyde
- **Boşanmış:** Az
- **Yorum:** Genç ve bekar çalışan çoğunlukta

### 8. İş Seyahati
- **Nadiren Seyahat:** En yaygın
- **Sık Seyahat:** Orta
- **Seyahat Etmiyor:** Az
- **Yorum:** Çoğu çalışan ara sıra seyahat ediyor

### 9. Şirketteki Yıl
- **Yeni (0-2 yıl):** Çok fazla
- **Tecrübeli (5+ yıl):** Orta
- **Eski (10+ yıl):** Az
- **Yorum:** Yüksek personel devri olabilir

### 10. Evden Uzaklık
- **Yakın (1-5 km):** Çok
- **Orta (5-15 km):** Orta
- **Uzak (15+ km):** Az
- **Yorum:** Çalışanlar genelde yakında oturuyor

---

## ⚠️ Dikkat Edilmesi Gerekenler

### İstifa Tahmininde Önemli Olabilecek Özellikler:
1. **Fazla Mesai** → Evet yapanlar daha çok istifa edebilir
2. **İş Memnuniyeti** → Düşük olanlar risk altında
3. **Maaş Artış Yüzdesi** → Düşük artış alanlar gidebilir
4. **Son Terfi Süresi** → Uzun süre terfi almayanlar riskli
5. **İş-Yaşam Dengesi** → Kötü olduğunda istifa riski artar
6. **Toplam Çalışma Yılı** → Çok tecrübeli olanlar başka fırsatlara açık
7. **Şirketteki Yıl** → 0-1 yıl olanlar hemen gidebilir
8. **Evden Uzaklık** → Çok uzakta olanlar yorulup gidebilir

---

## 📈 Model İçin Beklentiler

### Dengesiz Veri
- İstifa eden az, kalan çok
- Model "Hayır" demeye meyilli olabilir
- F1-score ve recall metriklerine bakmak önemli

### Kategorik Özellikler Çok
- One-hot encoding sonrası kolon sayısı artacak
- Departman, Eğitim Alanı, Medeni Durum → Binary kolonlara dönüşecek

### Korelasyonlar
- İş memnuniyeti + Ortam memnuniyeti → Birbiriyle ilişkili olabilir
- Toplam çalışma yılı + Yaş → Pozitif korelasyon beklenir
- Şirketteki yıl + Mevcut müdürle yıl → İlişkili olabilir

---

## ✅ Sonuç

Bu veri seti **çalışan istifa tahmini** için uygundur.
- Yeterli kayıt var (1471 satır)
- Hedef değişken açık (Istifa)
- Özellikler anlamlı ve gerçekçi
- Makine öğrenmesi modeli başarılı sonuç verebilir

**Beklenen Model Başarısı:** %75-85 accuracy
**Kritik Metrik:** Recall (istifa edecekleri yakalama oranı)

