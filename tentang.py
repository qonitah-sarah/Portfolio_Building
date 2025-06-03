import streamlit as st

def tampilkan_tentang_saya():
    st.markdown("### Tentang Saya")
    st.write("""
             Halo, perkenalkan nama saya Qonitah Sarah! 
             
             Memiliki latar belakang pendidikan sarjana di bidang Arsitektur yang menaruh minat pada decision-making berbasis data.
             Untuk berkenalan lebih jauh, selengkapnya bisa mengunjungi profil [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/qonitahsarah) 
             dan tulisan saya di [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@qonitah_sarah).
             Semoga sebelum berpisah, ada oleh-oleh kebaikan yang bisa dibawa pulang.
             """, unsafe_allow_html=True)

    name = st.text_input("Sebelum menjelajah lebih jauh kita saling kenal dulu yuk, siapa nama kamu?")
    if name:
        st.markdown(f"Halo **{name}**! Salam kenal ya! 👋")

