import streamlit as st
from utils.filter_global import filter_global
from generator.data_generator import generate_data

st.set_page_config(page_title="Simulasi Data", page_icon="📊")
filter_global()

# Cek apakah sudah ada data di session_state
if "data_listrik" not in st.session_state:
    st.session_state["data_listrik"] = generate_data()

st.title("🏠 Home - Generate Data Listrik")

# with st.sidebar:   # pakai sidebar sebagai "navbar"
#     pilihan = st.radio(
#         "Pilih rentang waktu:",
#         ("7 hari", "3 hari", "1 hari"),
#         horizontal=False
#     )
#     st.session_state["range_waktu"] = pilihan

# Pakai data dari state
df = st.session_state["data_listrik"]



st.subheader("Data Preview")
st.write(df.head())

st.subheader("Grafik Arus")
st.line_chart(df.set_index("timestamp")[["arus_lokasi1", "arus_lokasi2"]])

st.subheader("Grafik Tegangan")
st.line_chart(df.set_index("timestamp")[["volt_lokasi1", "volt_lokasi2"]])