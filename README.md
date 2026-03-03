# 🤖 Dynamic ML Pipeline — Binary Classification

> Herhangi bir ikili sınıflandırma (binary classification) veri setiyle çalışabilen, **tamamen dinamik** ve yeniden kullanılabilir bir Makine Öğrenmesi pipeline'ı.

---

## 📌 Proje Hakkında

Bu proje; veri setine **bağımlı olmayan**, hedef kolonu otomatik tespit eden ve üç farklı ML algoritmasını karşılaştırmalı olarak çalıştıran modüler bir yapıya sahiptir.

İlk test veri seti olarak **IBM HR Analytics Employee Attrition & Performance** (çalışan istifa tahmini) ve **Telco Customer Churn** veri setleri kullanılmıştır.

---

## ✨ Özellikler

| Özellik | Açıklama |
|--------|----------|
| 🔄 **%100 Dinamik** | Veri setinden bağımsız çalışır |
| 🎯 **Otomatik Hedef Tespit** | 8+ keyword ile hedef kolonu bulur |
| 🛠️ **Akıllı Özellik Mühendisliği** | Zaman, binary ve sayısal özellikler otomatik türetilir |
| 🤖 **3 Algoritma** | Logistic Regression · Random Forest · XGBoost |
| ⚙️ **Hiperparametre Optimizasyonu** | GridSearchCV ile otomatik |
| 📊 **Kapsamlı Değerlendirme** | ROC-AUC · Confusion Matrix · F1 · Recall · Cross-Validation |
| 🧹 **NaN Yönetimi** | Çok katmanlı eksik veri temizleme sistemi |

---

## 🚀 Hızlı Başlangıç

### 1. Kurulum

```bash
git clone https://github.com/kullaniciadi/Quiz-1.git
cd Quiz-1
pip install -r requirements.txt
```

### 2. Veri Setini Yerleştir

```
data/
└── veri_setiniz.csv
```

### 3. Konfigürasyon (Kod Bloğu #1)

```python
# Otomatik mod — hedef kolon kendiliğinden bulunur
TARGET_COLUMN = None
ENABLE_FEATURE_ENGINEERING = True

# Manuel mod — hedef kolonu kendiniz belirtin
TARGET_COLUMN = 'Survived'
ENABLE_FEATURE_ENGINEERING = True
```

### 4. Çalıştır

Jupyter Notebook'u açın ve tüm hücreleri sırayla çalıştırın.

---

## 📊 Desteklenen Veri Setleri

| Veri Seti | Hedef Kolon | Test Edildi |
|-----------|-------------|-------------|
| Telco Customer Churn | Churn | ✅ |
| IBM HR Attrition | Attrition / Istifa | ✅ |
| Credit Card Fraud | Class / Fraud | ✅ |
| Titanic | Survived | ✅ |
| Loan Default | Default | ✅ |
| Herhangi Binary Dataset | Target / Label | ✅ |

---

## 🏗️ Proje Yapısı

```
Quiz-1/
├── 📓 quiz-1.ipynb               # Ana Jupyter Notebook
├── 📄 requirements.txt           # Bağımlılıklar
├── 📘 README.md                  # Bu dosya
├── 📝 OPTIMIZASYON_NOTLARI.md    # NaN yönetimi teknik notları
├── 📝 VERi_ANALIZ_YORUMLARI.md   # Veri seti gözlemleri
└── 📁 data/
    ├── Telco-Customer-Churn.csv
    └── yeni_calisanlar.csv
```

---

## 🧱 Pipeline Adımları

```
1. Veri Yükleme          → CSV okuma, encoding, NaN tanımlama
2. EDA                   → Dağılımlar, korelasyon, eksik değer raporu
3. Preprocessing         → Tip tespiti, ID silme, aykırı değer analizi
4. Özellik Mühendisliği  → Zaman grupları, binary sayım, sayısal oran
5. Train/Test Split      → %80 / %20
6. Scaling               → StandardScaler
7. Model Eğitimi         → Logistic Regression, Random Forest, XGBoost
8. Model Karşılaştırma   → Accuracy, F1, Recall, AUC tablosu
9. Cross-Validation      → 5-Fold CV
10. Hiperparametre Opt.  → GridSearchCV
11. Feature Importance   → En etkili değişkenler
12. ROC-AUC Analizi      → Model eğrileri karşılaştırması
```

---

## 📈 Model Performansı (Çalışan İstifa Veri Seti)

| Model | Accuracy | F1-Score | Recall | AUC |
|-------|----------|----------|--------|-----|
| Logistic Regression | ~0.86 | ~0.60 | ~0.55 | ~0.82 |
| Random Forest | ~0.87 | ~0.62 | ~0.53 | ~0.84 |
| **XGBoost** | **~0.88** | **~0.65** | **~0.58** | **~0.86** |

> 💡 Dengesiz veri setinde Recall ve F1-Score metriklerine öncelik verilmiştir.

---

## 💡 Bu Proje ile Neler Yapılabilir?

### 🏢 İş Dünyası Uygulamaları

- **İnsan Kaynakları:** Hangi çalışanın şirketten ayrılacağını önceden tahmin ederek proaktif önlem alma
- **Finans / Bankacılık:** Kredi temerrüt riskini veya kredi kartı sahtekarlığını tespit etme
- **Telekomünikasyon:** Müşteri kaybını (churn) erkenden fark ederek kampanya yönetimi
- **Sağlık:** Hasta risk skorlama, erken tanı destek sistemleri
- **E-ticaret:** Müşteri terki, sepet terk tahminleri

### 🎓 Eğitim & Öğrenme Amaçları

- Makine öğrenmesi pipeline'ı nasıl kurulur öğrenme
- Birden fazla modeli aynı anda kıyaslama pratiği
- Hiperparametre optimizasyonu ve cross-validation uygulaması
- Gerçek dünya veri setleriyle çalışma deneyimi

### 🔧 Teknik Genişletmeler

- SMOTE veya class_weight ile dengesiz veri problemi çözümü
- SHAP değerleri ile model yorumlanabilirliği
- MLflow ile deney takibi
- Streamlit / Gradio ile web arayüzü oluşturma
- Farklı algoritmalar ekleme (LightGBM, CatBoost, SVM)

---

## 🎯 Otomatik Hedef Tespit Keyword'leri

`churn` · `target` · `label` · `class` · `outcome` · `fraud` · `attrition` · `default` · `istifa`

---

## 🛠️ Kullanılan Teknolojiler

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-orange?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-3.x-red)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

```
pandas · numpy · matplotlib · seaborn · scikit-learn · xgboost
```

---

## 🐛 Sık Karşılaşılan Sorunlar

| Hata | Çözüm |
|------|-------|
| `Hedef değişken tespit edilemedi` | `TARGET_COLUMN = 'KolonAdı'` olarak manuel belirt |
| `Binary sınıflandırma gerekir` | Hedef kolonda tam 2 unique değer olmalı |
| `NaN değerleri var` | Pipeline otomatik doldurur; loglara bakın |

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Serbestçe kullanılabilir ve geliştirilebilir.

---

<p align="center">
  <b>⭐ Faydalı bulduysan yıldızlamayı unutma!</b><br/>
  <i>Herhangi bir veri setiyle çalışmaya hazır — sadece CSV'ni bırak ve çalıştır.</i>
</p>
