import streamlit as st

# Ini bagian heading aplikasi Streamlit
st.title("Kuliah Praktikum Big Data")
st.write("# Pendahuluan")
st.write("Contoh aplikasi `streamlit` untuk proyek kelompok mata kuliah Praktikum Big Data.")
st.write("## Petunjuk Proyek Kelompok")
str_petunjuk = '''
- Proyek Kelompok dibuat menggunakan `streamlit`.
- Harus menggunakan dataset yang diambil dari sumber data seperti Kaggle, BPS, dan sebagainya.
- Harus ada visualisasi dalam bentuk grafis.
- Visualiasi harus bisa dianalisis secara dinamis menggunakan variabel dari elemen-elemen `streamlit`.
- Ada analisis sederhana terhadap visualisasi grafis tersebut.
- Ada simpulan terhadap analisis.
'''
st.write(str_petunjuk)

st.write("# Contoh-contoh elemen `streamlit`")

st.write("## Button")
btn_contoh = st.button("Coba klik saya")
st.write(f"Tombol sudah diklik: {btn_contoh}")

# Pilihan
st.write('## Checkbox')
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(f"Ya: {pilih1} Tidak: {pilih2}.")

st.write("## Toggle")
saklar = st.toggle("Activate")
st.write(f"{saklar}")

st.write("## Radiobox")
makanan = st.radio('Apa makanan kesukaanmu?', ['Bakso', 'Nasi goreng', 'Mie ayam', 'Yang lain'] )
st.write(f"Makanan kesukaanmu adalah: {makanan}.")

st.write("## Selection Box")
minuman = st.selectbox('Pilih minuman yang akan dipesan',
            ['Es teh', 'Kopi', 'Jus'] )

st.write(minuman)

st.write("## Multiple Selection")
bayar = st.multiselect('Bayar pakai:',
                      ['Tunai', 'Ovo', 'GoPay'])
st.write(bayar)

st.write("## Slider")
volume = st.select_slider("Volume suara", list(range(1,11)))
st.write(f"Volume: {volume}")

st.write("## Metric")
# Kinerja unit
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)
st.metric("Saham", 100, 20)

st.write("## `streamlit` widgets")
st.write("Untuk contoh-contoh widget yang lain, bisa dilihat di [`streamlit` widgets](https://docs.streamlit.io/develop/api-reference/widgets).")

