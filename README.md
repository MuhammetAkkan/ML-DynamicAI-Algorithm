# Dinamik Makine Öğrenmesi Projesi

## 📋 Proje Açıklaması

Bu proje, **herhangi bir binary classification veri setiyle** çalışabilen tamamen dinamik bir makine öğrenmesi pipeline'ıdır.

## ✨ Özellikler

- ✅ **%100 Dinamik:** Veri setine bağımlılık yok
- ✅ **Otomatik Hedef Tespit:** 8 farklı keyword ile hedef kolon bulma
- ✅ **Akıllı Özellik Mühendisliği:** Zaman, binary ve sayısal özellikler otomatik
- ✅ **3 Farklı Model:** Logistic Regression, Random Forest, XGBoost
- ✅ **Hiperparametre Optimizasyonu:** GridSearchCV
- ✅ **Cross-Validation:** 5-Fold CV
- ✅ **ROC-AUC Analizi:** Model performans karşılaştırma

## 🔧 Konfigürasyon

Kod Bloğu #1'de sadece 2 parametre ayarlayın:

```python
# Hedef kolon (None = otomatik tespit)
TARGET_COLUMN = None  # Örnek: 'Churn', 'Fraud', 'Survived'

# Özellik Mühendisliği (True = akıllı tespit, False = atla)
ENABLE_FEATURE_ENGINEERING = True
```

## 🚀 Kullanım

### 1. Veri Setini Yerleştir
```bash
data/Telco-Customer-Churn.csv  # veya herhangi bir CSV
```

### 2. Konfigürasyon Ayarla

**Otomatik Mod:**
```python
TARGET_COLUMN = None              # Hedef kolon otomatik bulunur
ENABLE_FEATURE_ENGINEERING = True # Özellikler otomatik türetilir
```

**Manuel Mod:**
```python
TARGET_COLUMN = 'Survived'        # Hedef kolon manuel belirt
ENABLE_FEATURE_ENGINEERING = True # Özellikler otomatik türetilir
```

**Minimal Mod:**
```python
TARGET_COLUMN = 'Target'          # Hedef kolon manuel belirt
ENABLE_FEATURE_ENGINEERING = False # Sadece temel preprocessing
```

### 3. Kodu Çalıştır
Jupyter Notebook'ta tüm hücreleri çalıştır.

## 📊 Desteklenen Veri Setleri

| Veri Seti | Hedef Kolon | Değerler | Test Edildi |
|-----------|-------------|----------|-------------|
| Telco Customer Churn | Churn | Yes/No | ✅ |
| Credit Card Fraud | Class/Fraud | 0/1 | ✅ |
| Employee Attrition | Attrition | Yes/No | ✅ |
| Loan Default | Default | True/False | ✅ |
| Titanic | Survived | 0/1 | ✅ |
| Generic ML Dataset | Target/Label | Any binary | ✅ |

## 🎯 Hedef Kolon Tespiti

### Otomatik Tespit (TARGET_COLUMN = None)

Kod şu keyword'leri arar:
- `churn` (örn: Churn, Customer_Churn)
- `target` (örn: Target, Target_Label)
- `label` (örn: Label, Class_Label)
- `class` (örn: Class, Classification)
- `outcome` (örn: Outcome, Final_Outcome)
- `fraud` (örn: Fraud, Is_Fraud)
- `attrition` (örn: Attrition, Employee_Attrition)
- `default` (örn: Default, Loan_Default)

### Manuel Tespit (TARGET_COLUMN = 'ColumnName')

Direkt olarak kolon adını belirtin.

## 🔨 Özellik Mühendisliği

### 1. Zaman Bazlı Özellik (NEW_TimeGroup)

**Tespit:** `tenure`, `duration`, `age`, `days`, `months`, `years`, `time`

**Çıktı:** Quartile bazlı gruplar
- Q1_Dusuk (0-25%)
- Q2_Orta_Alt (25-50%)
- Q3_Orta_Ust (50-75%)
- Q4_Yuksek (75-100%)

### 2. Binary Özellik Sayısı (NEW_ActiveFeatureCount)

**Tespit:** Yes/No, True/False, 1/0 değerli kolonlar

**Çıktı:** Aktif özelliklerin toplamı

### 3. Sayısal Özellik Oranı (NEW_Ratio_1_2)

**Tespit:** İlk iki sayısal kolon

**Çıktı:** Birinci kolonun ikinciye oranı

## 📦 Gereksinimler

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
pandas
numpy
seaborn
matplotlib
scikit-learn
xgboost
```

## 📁 Proje Yapısı

```
Quiz-1/
├── quiz-1.ipynb              # Ana notebook
├── data/
│   └── Telco-Customer-Churn.csv
├── control/
│   ├── makine-ogranmesi-sinav-uyarisi.json
│   └── sinavUyarilari.json
├── requirements.txt
└── README.md
```

## 🎓 Kod Blokları

1. **Kod Bloğu #1:** Kütüphaneler + Konfigürasyon
2. **Kod Bloğu #2:** EDA (Keşifçi Veri Analizi)
3. **Kod Bloğu #3:** Preprocessing + Özellik Mühendisliği
4. **Kod Bloğu #4:** Train/Test Split + Scaling
5. **Kod Bloğu #5-7:** Model Eğitimi (3 algoritma)
6. **Kod Bloğu #8:** Model Karşılaştırma
7. **Kod Bloğu #9:** Cross-Validation
8. **Kod Bloğu #10:** Hiperparametre Optimizasyonu
9. **Kod Bloğu #11:** Feature Importance
10. **Kod Bloğu #12:** ROC-AUC Analizi

## 📈 Model Performansı (Telco Dataset)

| Model | Accuracy | F1-Score | Recall |
|-------|----------|----------|--------|
| Logistic Regression | 0.80 | 0.58 | 0.54 |
| Random Forest | 0.79 | 0.59 | 0.51 |
| XGBoost | 0.80 | 0.60 | 0.54 |

## 🎯 Özellikler

### Veri Ön İşleme
- ✅ Otomatik tip tespiti
- ✅ ID kolon silme
- ✅ Eksik değer yönetimi
- ✅ Aykırı değer analizi (IQR)
- ✅ One-Hot Encoding
- ✅ Standard Scaling

### Model Değerlendirme
- ✅ Confusion Matrix
- ✅ Classification Report
- ✅ ROC Curve
- ✅ Feature Importance
- ✅ Cross-Validation Scores

### Özel Özellikler
- ✅ Kolon numaralama sistemi
- ✅ Dinamik hedef tespit
- ✅ Akıllı özellik türetme
- ✅ Hata yönetimi

## 🔍 Test Senaryoları

### Senaryo 1: Yeni Veri Seti (Otomatik)
```python
# 1. CSV'yi data/ klasörüne at
# 2. Kod Bloğu #1'i güncelle:
df = pd.read_csv("data/YeniDataSet.csv")
TARGET_COLUMN = None
ENABLE_FEATURE_ENGINEERING = True

# 3. Tüm hücreleri çalıştır
```

### Senaryo 2: Hedef Kolon Bulunamıyor
```python
# Manuel belirt:
TARGET_COLUMN = 'OzelHedefKolonum'
```

### Senaryo 3: Özellik Mühendisliği İstemiyorum
```python
ENABLE_FEATURE_ENGINEERING = False
```

## 🐛 Hata Giderme

### "Hedef değişken tespit edilemedi"
```python
# Çözüm: Manuel hedef kolon belirt
TARGET_COLUMN = 'HedefKolonAdı'
```

### "Binary sınıflandırma gerekir"
```python
# Hedef kolonunuzda tam olarak 2 unique değer olmalı
print(df['HedefKolon'].unique())  # Kontrol et
```

## 📚 Öğrenilen Konular

- Dinamik kod yazımı
- Veri seti bağımsız sistemler
- Otomatik özellik tespiti
- Binary classification
- Model karşılaştırma
- Hiperparametre optimizasyonu
- Cross-validation
- ROC-AUC analizi

## 👨‍💻 Geliştirici

Makine Öğrenmesi Sınavı Çalışması

## 📄 Lisans

Bu proje eğitim amaçlıdır.

---

**🎉 Artık herhangi bir veri setiyle çalışabilirsiniz!**

=======
# ML-Multi-Algo-Resignation-Core
Veri setlerini dinamik olarak okuyarak Logistic Regression, Random Forest ve XGBoost algoritmalarıyla analiz eder ve sonuçları karşılaştırmalı olarak listeler. Kolon yapısı otomatik algılanır; veri setinde ilgili alanın bulunamadığı durumlarda tek seferlik manuel yapılandırma desteği sunar
>>>>>>> d1da86ac138315deea0f13d8d2870fc2bcb0ad0b
