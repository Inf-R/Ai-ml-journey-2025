# DAY 3: GENTLE INTRODUCTION TO PANDAS
# Pandas = Python + Data Analysis = Powerful tool untuk olah data

print("=== DAY 3: KENALAN DENGAN PANDAS ===")
print("Pandas itu seperti Excel tapi dengan kekuatan Python!")
print("-" * 50)

# STEP 0: Import Pandas (seperti memanggil tools)
import pandas as pd  # 'pd' adalah nickname untuk pandas

print("✅ Pandas berhasil diimport!")
print("Pandas = Powerful Data Analysis Library")

# STEP 1: Dari Python Biasa ke Pandas
print("\n📍 STEP 1: Bandingkan Python Biasa vs Pandas")

# Cara lama (Python biasa) - ribet!
mahasiswa_python = [
    {"nama": "Ali", "umur": 20, "nilai": 85},
    {"nama": "Budi", "umur": 21, "nilai": 90},
    {"nama": "Cici", "umur": 19, "nilai": 78}
]

print("Data dengan Python biasa:")
for mhs in mahasiswa_python:
    print(f"{mhs['nama']}: {mhs['nilai']}")

# Cara baru (Pandas) - mudah!
df = pd.DataFrame(mahasiswa_python)  # DataFrame = tabel data
print("\nData dengan Pandas:")
print(df)

print(f"\nBentuk data: {df.shape}")  # (baris, kolom)
print("Lebih rapi kan? 😊")

# STEP 2: Pandas DataFrame = Excel Sheet yang Powerful
print("\n📍 STEP 2: DataFrame = Seperti Excel Tapi Lebih Pintar")

# Membuat data lebih besar
data_mahasiswa = {
    'nama': ['Ali', 'Budi', 'Cici', 'Dodi', 'Eka', 'Fani'],
    'umur': [20, 21, 19, 22, 20, 21],
    'nilai_math': [85, 90, 78, 92, 88, 76],
    'nilai_python': [92, 85, 88, 95, 90, 82],
    'jurusan': ['TI', 'SI', 'TI', 'SI', 'TI', 'SI']
}

df = pd.DataFrame(data_mahasiswa)
print("Dataset lengkap:")
print(df)

# Informasi basic tentang data
print(f"\nJumlah mahasiswa: {len(df)} orang")
print(f"Jumlah kolom: {len(df.columns)}")
print(f"Nama kolom: {list(df.columns)}")

# STEP 3: Melihat Data (seperti mengintip Excel)
print("\n📍 STEP 3: Cara Melihat Data")

print("5 data teratas:")
print(df.head())  # Seperti lihat sheet Excel dari atas

print("\n5 data terbawah:")
print(df.tail())  # Seperti scroll ke bawah Excel

print("\nInfo lengkap dataset:")
print(df.info())  # Seperti properties file Excel

# STEP 4: Mengakses Data (seperti pilih kolom/baris di Excel)
print("\n📍 STEP 4: Mengakses Data Tertentu")

# Pilih satu kolom (seperti pilih kolom A di Excel)
print("Hanya nama mahasiswa:")
print(df['nama'])

# Pilih beberapa kolom
print("\nNama dan nilai Python:")
print(df[['nama', 'nilai_python']])

# Pilih baris tertentu (seperti pilih row 2 di Excel)
print("\nMahasiswa pertama:")
print(df.iloc[0])  # iloc = integer location (baris ke-0)

# STEP 5: Filter Data (seperti filter di Excel)
print("\n📍 STEP 5: Filter Data")

# Cari mahasiswa dengan nilai math > 85
mahasiswa_pintar = df[df['nilai_math'] > 85]
print("Mahasiswa dengan nilai Math > 85:")
print(mahasiswa_pintar[['nama', 'nilai_math']])

# Filter berdasarkan jurusan
mahasiswa_ti = df[df['jurusan'] == 'TI']
print("\nMahasiswa jurusan TI:")
print(mahasiswa_ti[['nama', 'jurusan']])

# Filter kombinasi
pintar_ti = df[(df['nilai_math'] > 85) & (df['jurusan'] == 'TI')]
print("\nMahasiswa TI yang pintar Math:")
print(pintar_ti[['nama', 'nilai_math', 'jurusan']])

# STEP 6: Statistik Dasar (seperti SUM, AVERAGE di Excel)
print("\n📍 STEP 6: Statistik Otomatis")

print("Statistik nilai Math:")
print(f"Rata-rata: {df['nilai_math'].mean():.1f}")
print(f"Tertinggi: {df['nilai_math'].max()}")
print(f"Terendah: {df['nilai_math'].min()}")
print(f"Total: {df['nilai_math'].sum()}")

# Statistik semua kolom angka sekaligus
print("\nStatistik lengkap:")
print(df.describe())

# STEP 7: Grouping (seperti Pivot Table di Excel)
print("\n📍 STEP 7: Grouping Data")

# Rata-rata nilai per jurusan
print("Rata-rata nilai per jurusan:")
hasil_group = df.groupby('jurusan')[['nilai_math', 'nilai_python']].mean()
print(hasil_group)

# Hitung berapa mahasiswa per jurusan
print("\nJumlah mahasiswa per jurusan:")
print(df['jurusan'].value_counts())

# STEP 8: Menambah Kolom Baru (seperti formula di Excel)
print("\n📍 STEP 8: Membuat Kolom Baru")

# Hitung rata-rata dari 2 nilai
df['rata_rata'] = (df['nilai_math'] + df['nilai_python']) / 2

# Buat kategori berdasarkan nilai
df['kategori'] = df['rata_rata'].apply(lambda x: 'Excellent' if x >= 90 
                                      else 'Good' if x >= 80 
                                      else 'Average')

print("Data dengan kolom baru:")
print(df[['nama', 'nilai_math', 'nilai_python', 'rata_rata', 'kategori']])

# STEP 9: Sort Data (seperti sort di Excel)
print("\n📍 STEP 9: Mengurutkan Data")

# Sort berdasarkan rata-rata (tertinggi ke terendah)
df_sorted = df.sort_values('rata_rata', ascending=False)
print("Ranking mahasiswa berdasarkan rata-rata:")
print(df_sorted[['nama', 'rata_rata', 'kategori']])