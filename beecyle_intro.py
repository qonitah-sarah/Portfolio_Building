import streamlit as st

def tampilkan_intro():  
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron&display=swap');

    .logo-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 60px;
        text-align: center;
        font-weight: 700;
        color: #222;
        letter-spacing: 2px;
    }
    </style>

    <div class="logo-text">bee-cycle</div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <marquee behavior="scroll" direction="left" scrollamount="10" style="font-size:20px; color:teal;">
            🚴‍♀️ Selamat datang di BeeCycle! 🚴‍♂️
        </marquee>
        """,
        unsafe_allow_html=True)

    # st.markdown("### Selamat Datang di Bee-Cycle!")
    st.write("""
            Bee-Cycle merupakan sebuah e-commerce yang fokus menjual produk sepeda beserta perlengkapannya. 
            Toko telah berdiri di 3 kelompok wilayah, yaitu Eropa, Amerika Utara, dan Pasifik. 
            Data terdiri atas riwayat pembelian pelanggan yang rampung dilakukan di tahun 2016-2020 dan baru terdaftar hingga bulan Juli di 2021. 
            Setiap pembelian disertai dengan masing-masing data pembeli secara detail.
             """)
    
    st.markdown("### Kategori Produk Apa Saja yang Ditawarkan?")
    st.header("Bikes")
    st.image("https://www.racv.com.au/content/dam/racv-assets/images/images/motor/cars-bikes-transport/1600x900/bicycles-scooters-ebikes-1600x900.jpg", caption="Sumber: racv.com.au")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Accessories")
        st.image("https://www.vidavida.co.uk/cdn/shop/products/bike-water-bottle-holder-brown-0031_900x.jpg?v=1666024851", caption="Sumber: vidavida.co.uk")

    with col2:
        st.header("Clothing")
        st.image("https://media.rapha.cc/rapha-cc/image/upload/ar_1:1,c_fill,f_auto,q_auto,w_480,dpr_2.0/archive/amplience-image/H2_PDP_Assets76", caption="Sumber: media.rapha.cc")

        
