import streamlit as st

# Sidebar menu
menu = st.sidebar.radio("Pilih Menu", ["Home", "Kalkulator Total Plate Count", "Tentang Kami"])

# Tambahkan background image & style
st.markdown(f"""
    <style>
    body {{
        background-image: url("https://i.pinimg.com/736x/9d/4a/8e/9d4a8e3c2a9f2560f5febd654b189910.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
    }}
    .main {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        margin-top: 10%;
    }}
    .title {{
        color: #4CAF50;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Halaman: Home
if menu == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🧫 Selamat Datang di Aplikasi TPC</h1>', unsafe_allow_html=True)
    st.write("Aplikasi ini membantu menghitung **Total Plate Count (TPC)** atau jumlah koloni bakteri per mL sampel cair. Gunakan menu di sebelah kiri untuk mulai.")
    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Kalkulator Total Plate Count
elif menu == "Kalkulator Total Plate Count":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🔢 Kalkulator Total Plate Count</h1>', unsafe_allow_html=True)

    st.write("Masukkan data pengamatan laboratorium:")

    st.subheader("🔬 Data Pengenceran 1")
    koloni_1a = st.number_input("Jumlah koloni cawan 1 - Duplo A:", min_value=0, step=1, key="koloni_1a")
    koloni_1b = st.number_input("Jumlah koloni cawan 1 - Duplo B:", min_value=0, step=1, key="koloni_1b")
    pengenceran_1 = st.number_input("Faktor pengenceran cawan 1 (misal 10⁻³ → isi 1000):", min_value=1, step=1, key="pengenceran_1")

    st.subheader("🔬 Data Pengenceran 2")
    koloni_2a = st.number_input("Jumlah koloni cawan 2 - Duplo A:", min_value=0, step=1, key="koloni_2a")
    koloni_2b = st.number_input("Jumlah koloni cawan 2 - Duplo B:", min_value=0, step=1, key="koloni_2b")
    pengenceran_2 = st.number_input("Faktor pengenceran cawan 2 (misal 10⁻³ → isi 1000):", min_value=1, step=1, key="pengenceran_2")

    if st.button("Hitung TPC"):
        rata_1 = (koloni_1a + koloni_1b) / 2
        rata_2 = (koloni_2a + koloni_2b) / 2

        tpc1 = rata_1 / pengenceran_1
        tpc2 = rata_2 / pengenceran_2

        rata_rata_tpc = (tpc1 + tpc2) / 2

        st.write(f"📍 Rata-rata koloni cawan 1: {rata_1:.2f}")
        st.write(f"📍 Rata-rata koloni cawan 2: {rata_2:.2f}")
        st.write(f"✅ TPC dari cawan 1: **{tpc1:.4f} CFU/mL**")
        st.write(f"✅ TPC dari cawan 2: **{tpc2:.4f} CFU/mL**")
        st.success(f"🔢 Rata-rata Total Plate Count (TPC): **{rata_rata_tpc:.4f} CFU/mL**")

    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Tentang Kami
elif menu == "Tentang Kami":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">👨‍🔬 Tentang Kami</h1>', unsafe_allow_html=True)
    st.write("""
        Aplikasi ini dibuat untuk menghitung Total Plate Count (TPC) secara cepat dan akurat.
        \n💻 Dibuat menggunakan Python & Streamlit.
        \n📧 Kontak: lab@example.com
    """)
    st.image("LPK.jpg", caption="KELOMPOK 6", width=150)
    st.markdown('</div>', unsafe_allow_html=True)

