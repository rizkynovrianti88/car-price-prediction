# 🚗 Car Price Prediction App

## 📌 Deskripsi
Aplikasi Machine Learning untuk memprediksi harga mobil berdasarkan spesifikasi kendaraan.

## 🧠 Teknologi
- Python
- Pandas
- Scikit-learn
- Streamlit

## 🔍 Fitur
- Input data kendaraan
- Prediksi harga otomatis
- Insight sederhana
- Visualisasi data


## ⚙️ Cara Menjalankan
```bash
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```
<img width="241" height="326" alt="image" src="https://github.com/user-attachments/assets/f03d82b6-15dd-4a60-bfa4-4da8d0e2dcd9" />

## 📊 Model Performance

Model yang digunakan: **Random Forest Regressor**

- 📉 RMSE: 2453.55  
- 📈 R² Score: 0.92450  

## 📌 Interpretasi:
- Model mampu menjelaskan **±92.45% variasi harga mobil**
- Nilai R² tinggi → model sangat baik dalam menangkap pola data
- RMSE ~2.45K menunjukkan rata-rata error prediksi relatif kecil
- Model sudah cukup akurat untuk estimasi harga kendaraan
  
## 📈 Insight
- 🚗 Mileage tinggi → harga cenderung turun
- ⚙️ Engine besar → harga cenderung lebih tinggi
- 📅 Tahun kendaraan mempengaruhi depresiasi

## 📦 Struktur Project
# car-price-prediction/

-   app.py
-   train_model.py
-   Clean_car_data.csv
-   model.pkl
-   requirements.txt
-   README.md

## 💡 Pengembangan Selanjutnya
- Hyperparameter tuning (GridSearch / RandomSearch)
- Tambah model lain (XGBoost, Linear Regression)
- Deploy dengan UI yang lebih advanced

# 👤 Author

Rizky Novrianti
- 📊 Data Enthusiast | Mathematics Background
- 🔗 https://github.com/rizkynovrianti88
