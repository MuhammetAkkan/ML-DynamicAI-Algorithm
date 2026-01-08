# KOD BLOĞU #1: Kütüphaneleri İçe Aktarma ve Veriyi Yükleme
import pandas as pd
import numpy as np
import seaborn as sns    # Güzel grafikler çizmek için
import matplotlib.pyplot as plt  # Grafik çizmek için
import missingno as msn


# CSV dosyasından müşteri verilerini okuyoruz
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# İlk 5 satırı inceliyoruz, veriyi tanımak için
df.head()

# KOD BLOĞU #2: Veriyi İnceleme ve Keşfetme

# Veri boyutu bilgisi
print("--- Veri Seti İncelemesi Start---")
print("Veri Boyutu:", df.shape)  # Örnek: (A, B) = A satır, B sütun(kolon) var

# Veri tiplerini inceleme
print("\nVeri Tipleri:")
df.info()  # Her sütunun tipini ve eksik veri olup olmadığını gösterir

# Sayısal verilerin istatistikleri (ortalama, min, max vb.)
print("\nİstatistiksel Özet:")
print(df.describe())  # Sayısal sütunlar için özet istatistikler

# Hedef değişken (Churn) dağılımını grafik olarak gösteriyoruz
# burada hedef "Churn" dır.
plt.figure(figsize=(6,4)) # grafik boyutu
sns.countplot(x='Churn', data=df)  # Bar grafiği: Kaç kişi Yes, kaç kişi No
plt.title("Churn Dağılımı")
plt.show()

# Churn oranlarını sayı olarak yazdırıyoruz
print(df['Churn'].value_counts())  # Örnek: No: 5174, Yes: 1869
print("--- Veri Seti İncelemesi End---\n")
