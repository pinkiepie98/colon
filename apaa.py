import streamlit as st
import random

with st.popover("Menu"):
    menu = st.radio("Pilih Halaman", ["Home", "Kalkulator Total Plate Count", "Tentang Kami"])

# Tambahkan background image & style
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/73/e6/3f/73e63f3961ed68e42e4628c8155ecd38.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 0px;
        border-radius: 10px;
        margin-top: 5%;
    }
    .title {
        color: Black;
        text-align: center;
    }
    h3 {
        color: Black;
    }
   .custom-text {
    color: Black;
    font-size: 16px;
    font-family: 'Calibri', 'Segoe UI', sans-serif;
}
    </style>
""", unsafe_allow_html=True)


# Halaman: Home
if menu == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🧫 Welcome To Calculator TPC 🦠</h1>', unsafe_allow_html=True)
    st.write("Website ini membantu menghitung **Total Plate Count (TPC)** atau jumlah koloni bakteri per mL sampel cair. Gunakan menu di atas untuk mulai.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Fakta-fakta seru gabungan
fakta_seru = [
    "🧫 Bakteri bisa bereproduksi dalam hitungan menit!",
    "🔬 TPC digunakan untuk mengukur keamanan pangan.",
    "🦠 Beberapa bakteri bisa bertahan di lingkungan ekstrem.",
    "💡 Pasteurisasi membantu menurunkan jumlah mikroba berbahaya.",
    "🍽️ Mencuci tangan yang benar bisa mencegah penyebaran bakteri berbahaya.",
    "📊 TPC adalah metode penting dalam pengujian kualitas makanan.",
    "🥛 Produk susu sering diuji menggunakan TPC sebelum dipasarkan.",
    "🧼 Higienitas alat laboratorium sangat mempengaruhi hasil TPC.",
    "🌡️ Suhu inkubasi yang ideal untuk TPC adalah 35-37°C.",
    "🔎 Jumlah koloni ideal dihitung dari cawan dengan 30-300 koloni."
]

# Pilih satu fakta secara acak
fakta_pilihan = random.choice(fakta_seru)

# Halaman: Kalkulator Total Plate Count
elif menu == "Kalkulator Total Plate Count":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🔢 Kalkulator Total Plate Count</h1>', unsafe_allow_html=True)

    st.write("Masukkan data pengamatan laboratorium:")

    st.subheader("🔬 Data Pengenceran 1")
    koloni_1a = st.number_input("Jumlah koloni cawan 1 - Simplo:", min_value=0, step=1, key="koloni_1a")
    koloni_1b = st.number_input("Jumlah koloni cawan 1 - Duplo:", min_value=0, step=1, key="koloni_1b")
    pengenceran_1 = st.number_input("Faktor pengenceran cawan 1 (misal 10⁻³ → isi 1000):", min_value=1, step=1, key="pengenceran_1")

    st.subheader("🔬 Data Pengenceran 2")
    koloni_2a = st.number_input("Jumlah koloni cawan 2 - Simplo:", min_value=0, step=1, key="koloni_2a")
    koloni_2b = st.number_input("Jumlah koloni cawan 2 - Duplo:", min_value=0, step=1, key="koloni_2b")
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
        st.info("Bakteri udah dihitung, sekarang waktunya kamu santai dulu! ☕🦠")
        
    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Tentang Kami
elif menu == "Tentang Kami":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">👨‍🔬 Tentang Kami</h1>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Kami dari kelompok 6 kelas 1E2 Penjaminan Mutu Industri Pangan membuat website ini untuk menghitung Total Plate Count (TPC) secara cepat dan akurat. Kami sangat terbuka terhadap masukan, kritik, maupun saran demi peningkatan dan pengembangan web ini ke depannya. Jangan ragu untuk menghubungi kami!</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">💻 Dibuat menggunakan Python & Streamlit.</p>', unsafe_allow_html=True)

    # Menambahkan gambar dengan HTML agar bisa diatur gaya
    st.markdown('''
        <div style="text-align: center;">
            <img src="https://i.pinimg.com/736x/2e/49/ba/2e49baed7b89068c1c1747e623b5e916.jpg" alt="This Is Us!!" style="width: 60%; border-radius: 15px; margin-top: 20px;">
            <p class="custom-text"><strong>This Is Us!!</strong></p>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
