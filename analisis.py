import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import plotly.express as px


def tampilkan_analisis():
    df = pd.read_excel('dataset_bee_cycle.xlsx', parse_dates=['order_date'])

    tab1, tab2 = st.tabs(["Page 1", "Page 2"])

    with tab1:
        # Jumlah penjualan di setiap negara
        st.markdown("### Eropa, si kecil yang indah. Menjadi wilayah dengan penjualan barang terbanyak")
        df["tahun_order"] = df["order_date"].dt.year
        
        df["profit"] = df["totalprice_rupiah"] - df["totalcost_rupiah"]
        df_grouped = df.groupby("territory_groups").agg({
            "quantity": "sum",
            "profit": "sum"
            }).reset_index()


        # Bar chart
        fig = px.bar(
            df_grouped,
            x="territory_groups",
            y="quantity",
            color="territory_groups",
            hover_data=["profit"],
            title="Total Penjualan per Wilayah",
            text="quantity"
        )

        # Format dan posisinya
        fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')

        fig.update_layout(
        title_text="Total Penjualan per Wilayah",
        title_x=0.5)

        st.plotly_chart(fig)
        
        # profit
        st.markdown("<h6 style='text-align: center;'>Detail Profit per Wilayah</h3>", unsafe_allow_html=True)
        df_grouped["profit"] =  df_grouped["profit"].apply(lambda x: f"Rp{x:,.0f}".replace(",", "."))
        
        st.dataframe(df_grouped[["territory_groups", "profit"]])

        st.write("""
                Walaupun tidak memiliki cakupan ruang seluas wilayah di Amerika Utara dan Pasifik, Eropa mampu menyaingi dan menduduki posisi pertama dengan total penjualan barang terbanyak. 
                Pernah menjadi wilayah dengan penjualan barang yang paling sedikit, namun perlahan ikut bersaing bermain di 2 peringkat teratas dan di 2020-2021 konsisten berada di urutan pertama. 
                Bukan hanya unggul di kuantitas, Eropa juga meraup total keuntungan terbanyak.
                """)

        # Tren penjualan
        # Agregasi penjualan per tahun dan kategori
        
        df_grouped = df.groupby(["tahun_order", "category", "territory_groups", "gender"])["quantity"].sum().reset_index()

        df_grouped = df_grouped[df_grouped['territory_groups'].isin(["Europe"])]

        # Urutkan tahun
        df_grouped = df_grouped.sort_values("tahun_order")

        # Ambil daftar tahun unik
        tahun_unik = df_grouped["tahun_order"].unique()

        st.markdown("### Permintaan sepeda tidak pernah absen di setiap tahun")

        tahun_terpilih = st.multiselect(
        "Pilih Tahun",
        options=sorted(df_grouped["tahun_order"].unique()),
        default=sorted(df_grouped["tahun_order"].unique())  # default semua tahun aktif
        )

        if tahun_terpilih:
            df_filtered = df_grouped[df_grouped["tahun_order"].isin(tahun_terpilih)]
        else:
            df_filtered = df_grouped.copy()  # kalau gak pilih apapun, tampilkan semua

        # Area kosong buat animasi
        grafik_area = st.empty()

        with grafik_area:
            plt.figure(figsize=(10, 5))
            sns.lineplot(
                data=df_filtered,
                x="tahun_order",
                y="quantity",
                hue="category",
                marker="o"
            )
            plt.xlabel("Tahun")
            plt.ylabel("Jumlah Penjualan")
            plt.title("Tren Penjualan Keseluruhan")
            plt.tight_layout()
            st.pyplot(plt)

        if st.button("▶️Lihat Pergerakan Tren Kategori Produk"):
            for tahun in tahun_unik:
                df_t = df_grouped[df_grouped["tahun_order"] <= tahun]

                # Update grafik di tempat yang sama
                with grafik_area:
                    plt.figure(figsize=(10, 5))
                    sns.lineplot(
                        data=df_t,
                        x="tahun_order",
                        y="quantity",
                        hue="category",
                        marker="o"
                    )
                    plt.title(f"Tren Penjualan s.d. Tahun {tahun}")
                    plt.xlabel("Tahun")
                    plt.ylabel("Jumlah Penjualan")
                    plt.tight_layout()
                    st.pyplot(plt)
                    time.sleep(0.5)
        
        st.write("""
                Produk yang berhasil terjual di wilayah bagian Eropa adalah kategori aksesoris, sepeda, dan pakaian. 
                Melihat dari perspektif tren pada rentang waktunya, kategori sepeda selalu hadir sejak 2016 dan terus meningkat di 3 tahun berikutnya hingga menurun perlahan di 2020.
                """)
        
        # metrik
        st.markdown("### Sepeda, Produk dengan keuntungan terbanyak")
        
        tahun_terpilih = st.select_slider(
        "Pilih Tahun",
        options=sorted(df["tahun_order"].unique()),
        value=max(df["tahun_order"])  # default ke tahun terbaru
        )

        df_filtered = df[df["tahun_order"] == tahun_terpilih]

        penjualan_per_kategori = df_filtered.groupby("category")["profit"].sum().reset_index()

        cols = st.columns(len(penjualan_per_kategori))

        for i, row in penjualan_per_kategori.iterrows():
            with cols[i]:
                st.metric(
                    label=row["category"],
                    value=f"Rp{row['profit']:,.0f}".replace(",", ".")
                )


    with tab2:
        # gender
        st.markdown("### Mari berkenalan dengan pelanggan sepeda kami")

        df_europe = df[df['territory_groups'] == 'Europe']

        gender_counts = df_europe["gender"].value_counts(normalize=True).reset_index()
        gender_counts.columns = ["gender", "percentage"]
        gender_counts["percentage"] = gender_counts["percentage"] * 100

        # pie chart
        st.markdown("<h6 style='text-align: center;'>Tabel Presentase Gender</h4>", unsafe_allow_html=True)
        fig = px.pie(
            gender_counts,
            names="gender",
            values="percentage",
            hole=0.4  # tambahkan lubang untuk tampilan donut chart
            )
        fig.update_traces(textinfo='percent+label')

        st.plotly_chart(fig)
        gender_counts["percentage"] = gender_counts["percentage"].apply(lambda x: f"{x:.2f}%")

        st.write("""
                    Pelanggan yang membeli sepeda mayoritas adalah wanita, namun jumlahnya tidak jauh berbeda dengan pria dan keduanya hampir seimbang. Sebagian besar pelanggan telah menyandang status menikah dan konsisten lebih tinggi jumlahnya di sepanjang tahun dibandingkan yang berstatus single. 
                    Pembelian didominasi oleh pelanggan dengan grup usia 21-40 dan 41-60 tahun. 
                    Usia termuda yaitu grup usia <=20 tahun dan tertua yaitu grup usia di atas 60 tahun tidak rutin dijumpai di setiap tahun.
                    """)
        
        st.markdown("### Sepeda apa saja yang mereka beli?")

        # Tren penjualan
        # Agregasi penjualan per tahun dan kategori
        df_sub = df_europe.groupby(["tahun_order", "sub_category", "category"])["quantity"].sum().reset_index()

        df_sub = df_sub[df_sub['category'] == 'Bikes']

        # Urutkan tahun
        df_sub = df_sub.sort_values("tahun_order")

        # Ambil daftar tahun unik
        tahun_unik = df_sub["tahun_order"].unique()

        # Area kosong buat animasi
        grafik_area = st.empty()

        with grafik_area:
            plt.figure(figsize=(10, 5))
            sns.lineplot(
                data=df_sub,
                x="tahun_order",
                y="quantity",
                hue="sub_category",
                marker="o"
            )
            plt.xlabel("Tahun")
            plt.ylabel("Jumlah Penjualan")
            plt.title("Tren Penjualan Keseluruhan")
            plt.tight_layout()
            st.pyplot(plt)

        if st.button("▶️Lihat Pergerakan Tren Produk Sepeda"):
            for tahun in tahun_unik:
                df_t = df_sub[df_sub["tahun_order"] <= tahun]

                # Update grafik di tempat yang sama
                with grafik_area:
                    plt.figure(figsize=(10, 5))
                    sns.lineplot(
                        data=df_t,
                        x="tahun_order",
                        y="quantity",
                        hue="sub_category",
                        marker="o"
                    )
                    plt.title(f"Tren Penjualan s.d. Tahun {tahun}")
                    plt.xlabel("Tahun")
                    plt.ylabel("Jumlah Penjualan")
                    plt.tight_layout()
                    st.pyplot(plt)
                    time.sleep(0.5)
        
        st.write("""
                Toko menyediakan berbagai pilihan sepeda dengan kebutuhan yang beragam. 
                Sepeda yang dibeli oleh pelanggan di wilayah Eropa di antaranya adalah Mountain Bikes, Road Bikes, dan Touring Bikes yang diasumsikan debut di tahun 2018 karena seluruh wilayah penjualan kompak menunjukkan tidak adanya tercatat penjualan. 
                Pada 4 tahun awal (2016-2019), penjualan Road Bikes dan Mountain Bikes menunjukkan peningkatan yang stabil, namun di tahun berikutnya pelan-pelan menurun. 
                """)
        






    








