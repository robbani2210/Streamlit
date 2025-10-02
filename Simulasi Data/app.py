import streamlit as st

# === Definisi halaman ===
pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon="🏠"), 
    st.Page("pages/grafik_line.py", title="Grafik Line", icon="📈"),
    st.Page("pages/grafik_area.py", title="Grafik Area", icon="📊"),
])

# # === Filter waktu global (selalu ada di setiap halaman) ===
# opsi_waktu = ["7 Hari", "3 Hari", "1 Hari"]

# if "range_waktu" not in st.session_state:
#     st.session_state["range_waktu"] = opsi_waktu[0]  # default "7 Hari"

# # pastikan value valid
# if st.session_state["range_waktu"] not in opsi_waktu:
#     st.session_state["range_waktu"] = opsi_waktu[0]

# st.markdown("---")

# st.subheader("⏱ Pilih Rentang Waktu")

# st.session_state["range_waktu"] = st.radio(
#     "Filter Waktu",
#     opsi_waktu,
#     horizontal=True,
#     index=opsi_waktu.index(st.session_state["range_waktu"])
# )
# st.markdown("---")

# === Jalankan halaman yang dipilih ===
pg.run()
