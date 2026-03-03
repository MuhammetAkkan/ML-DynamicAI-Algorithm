# 🧹 NaN Optimizasyon Notları

Bu dokümanda pipeline'ın eksik veri (NaN) yönetimi için uyguladığı çok katmanlı temizleme stratejisi açıklanmaktadır.

---

## 🔄 NaN Temizleme Akışı

```
CSV Okuma (na_values genişletilmiş)
        ↓
📋 İlk NaN Raporu (yüzdelik oranlar)
        ↓
🔢 Sayısal Dönüşüm Hataları → medyan / 0
        ↓
🎯 Hedef Değişken → mod (sınıf dengesi korunur)
        ↓
🏷️  Kategorik Kolonlar → mod / 'Unknown'
        ↓
✅ Final Kontrol → Kalan tüm NaN'lar temizlenir
        ↓
🔀 X-y Ayrımı → Son güvenlik kontrolü
        ↓
🤖 Model Eğitimi (NaN = 0 garantisi)
```

---

## ⚙️ Uygulanan Optimizasyonlar

### 1. Gelişmiş CSV Okuma

```python
df = pd.read_csv("data/yeni_calisanlar.csv",
                 sep=';',
                 encoding='utf-8',
                 na_values=['', ' ', 'NA', 'N/A', 'nan', 'NaN', 'null'],
                 keep_default_na=True,
                 skipinitialspace=True)
```

| Parametre | Amaç |
|-----------|------|
| `sep=';'` | Noktalı virgül ayracını destekler |
| `encoding='utf-8'` | Türkçe karakter sorunlarını çözer |
| `na_values=[...]` | Boş string, whitespace, 'NA' vb. otomatik NaN'a çevrilir |
| `skipinitialspace=True` | Baştaki boşluklardan kaynaklanan hataları önler |

---

### 2. Kontrol Noktaları

| Aşama | Strateji |
|-------|----------|
| Veri yükleme sonrası | Tüm kolonlar taranır, yüzdelik NaN raporu üretilir |
| Sayısal dönüşüm | Dönüşüm kaynaklı NaN → **medyan** (ya da 0) |
| Hedef değişken | NaN → **mod** (sınıf dengesini korur) |
| Kategorik kolonlar | One-Hot öncesi → **mod** / `'Unknown'` |
| Final kontrol | Kalan her NaN sayısal ise medyan, kategorik ise mod ile doldurulur |
| X-y ayrımı | Model eğitimi öncesi son güvenlik katmanı |

---

### 3. Türkçe Veri Seti Desteği

- `TARGET_COLUMN = 'Istifa'` olarak ayarlandığında otomatik tanınır
- `'Evet'` → `1`, `'Hayır'` → `0` dönüşümü otomatik yapılır
- Otomatik hedef tespit listesine `'evet'` ve `'istifa'` keyword'leri eklenmiştir

---

## 📋 NaN Doldurma Stratejileri Özeti

| Kolon Tipi | Strateji | Neden? |
|------------|----------|--------|
| Sayısal | Medyan | Aykırı değerlere duyarsız |
| Kategorik | Mod | En sık görülen değeri korur |
| Hedef değişken | Mod | Sınıf dengesini bozmaz |
| Tüm değerler NaN | 0 / 'Unknown' | Son çare |

---

## ✅ Güvenceler

- ⛔ Hiçbir satır silinmez → Veri bütünlüğü korunur
- ✅ Model eğitimine giren veride NaN = 0 garantisi
- ✅ Her aşamada detaylı loglama
- ✅ Aykırı değerler silinmez (model kendi öğrenir)
