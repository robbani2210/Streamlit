import streamlit as st
from generator.data_generator import generate_data
from utils.filter_global import filter_global
import pandas as pd

st.set_page_config(page_title="Grafik dengan Filter", layout="wide")
filter_global()
st.title("📊 Grafik dengan Filter Waktu")

if "data_listrik" not in st.session_state:
    st.warning("⚠️ Data belum dibuat.")
else:
    df = st.session_state["data_listrik"]

    # Ambil pilihan dari session_state
    pilihan = st.session_state["range_waktu"]

    # Normalisasi huruf biar konsisten
    if pilihan.lower() == "7 hari":
        filtered_df = df[df["timestamp"] >= df["timestamp"].max() - pd.Timedelta(days=7)]
    elif pilihan.lower() == "3 hari":
        filtered_df = df[df["timestamp"] >= df["timestamp"].max() - pd.Timedelta(days=3)]
    else:  # "1 Hari"
        filtered_df = df[df["timestamp"] >= df["timestamp"].max() - pd.Timedelta(days=1)]

    # Pilih jenis data
    jenis_data = st.selectbox("Pilih jenis data:", ["Arus", "Volt"])

    if jenis_data == "Arus":
        kolom = ["arus_lokasi1", "arus_lokasi2"]
        judul = "Grafik Arus Listrik"
    else:
        kolom = ["volt_lokasi1", "volt_lokasi2"]
        judul = "Grafik Tegangan Listrik"

    st.subheader(f"{judul} - {pilihan}")
    st.area_chart(filtered_df.set_index("timestamp")[kolom])
