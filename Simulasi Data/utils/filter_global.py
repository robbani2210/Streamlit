import streamlit as st

def filter_global():
    opsi_waktu = ["7 Hari", "3 Hari", "1 Hari"]

    if "range_waktu" not in st.session_state:
        st.session_state["range_waktu"] = opsi_waktu[0]  # default

    # Simpan widget di sidebar (navbar)
    st.sidebar.subheader("⏱ Pilih Rentang Waktu")

    st.session_state["range_waktu"] = st.sidebar.radio(
        "Filter Waktu",
        opsi_waktu,
        index=opsi_waktu.index(st.session_state["range_waktu"])
    )
    st.sidebar.markdown("---")
