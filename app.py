import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# ======================
# LOAD DATA & MODEL
# ======================
df = pd.read_csv("clean_car_data.csv")
model = joblib.load("model.pkl")

brands = sorted(df["Brand"].unique())
fuels = sorted(df["Fuel_Type"].unique())
trans_opts = sorted(df["Transmission"].unique())

# ======================
# UI
# ======================
st.set_page_config(page_title="Prediksi Harga Mobil", layout="centered")
st.title("🚗 Prediksi Harga Mobil")

# ======================
# INPUT (2 COLUMN LAYOUT)
# ======================
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Brand", brands)
    fuel = st.selectbox("Fuel Type", fuels)
    year = st.number_input("Model_Year", 1990, 2026, 2015)
    engine = st.number_input("Engine_Size", 0.5, 6.0, 2.0)

with col2:
    trans = st.selectbox("Transmission", trans_opts)
    mileage = st.number_input("Mileage", 0, 300000, 50000)
    doors = st.selectbox("Doors", [2, 3, 4, 5])
    owner = st.selectbox("Owner_Count", [1, 2, 3, 4])
    hp = st.number_input("Horsepower", 40, 600, 120)

# ======================
# PREDIKSI
# ======================
if st.button("Prediksi"):

    input_df = pd.DataFrame([{
        "Brand": brand,
        "Model_Year": year,
        "Engine_Size": engine,
        "Fuel_Type": fuel,
        "Transmission": trans,
        "Mileage": mileage,
        "Doors": doors,
        "Owner_Count": owner,
        "Horsepower": hp
    }])

    pred = model.predict(input_df)[0]

    st.success(f"💰 Perkiraan Harga: {pred:,.2f}")

    # ======================
    # INSIGHT
    # ======================
    if mileage > 100000:
        st.warning("⚠️ Mileage tinggi → harga cenderung turun")

    if engine > 3.0:
        st.info("🚀 Engine besar → harga cenderung lebih tinggi")

    if year < 2015:
        st.warning("📉 Mobil relatif lama → kemungkinan depresiasi")

# ======================
# VISUALISASI
# ======================
st.subheader("📊 Distribusi Harga")

fig, ax = plt.subplots()
sns.histplot(df["Price"], kde=True, ax=ax)
st.pyplot(fig)