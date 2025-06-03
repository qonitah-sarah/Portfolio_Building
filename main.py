import streamlit as st

st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")

st.title("Portfolio")
# st.header("Data Science Enthusiast")

st.sidebar.title("Halo Selamat Datang!")
page = st.sidebar.radio("Pilih Halaman",
                        ["Tentang Saya", "Tentang Dataset", "Analisis"])

if page == 'Tentang Saya':
    import tentang
    tentang.tampilkan_tentang_saya()
elif page == 'Tentang Dataset':
    import beecyle_intro
    beecyle_intro.tampilkan_intro()
else:
    import analisis
    analisis.tampilkan_analisis()