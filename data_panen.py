# ============================================
# PROGRAM ANALISIS DATA PANEN
# Dibuat untuk pemula, langkah demi langkah
# ============================================

# Data panen disimpan dalam dictionary
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("=" * 50)
print("SOAL 1: TAMPILKAN SELURUH DATA PANEN")
print("=" * 50)

# Tampilkan semua data
for kode_lokasi in data_panen:
    print(f"\nKode Lokasi: {kode_lokasi}")
    print(f"Nama Lokasi: {data_panen[kode_lokasi]['nama_lokasi']}")
    print("Hasil Panen:")
    
    # Ambil data hasil panen
    hasil = data_panen[kode_lokasi]['hasil_panen']
    
    print(f"  - Padi: {hasil['padi']} kg")
    print(f"  - Jagung: {hasil['jagung']} kg")
    print(f"  - Kedelai: {hasil['kedelai']} kg")

print("\n" + "=" * 50)
print("SOAL 2: JUMLAH PANEN JAGUNG DARI LOKASI2")
print("=" * 50)

# Ambil data jagung dari lokasi2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
nama_lokasi2 = data_panen['lokasi2']['nama_lokasi']
print(f"Jumlah panen jagung di {nama_lokasi2}: {jagung_lokasi2} kg")

print("\n" + "=" * 50)
print("SOAL 3: NAMA LOKASI DARI LOKASI3")
print("=" * 50)

# Ambil nama lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi3: {nama_lokasi3}")

print("\n" + "=" * 50)
print("SOAL 4 & 5: VARIABEL TERPISAH UNTUK PADI DAN KEDELAI")
print("=" * 50)

# Buat list untuk menyimpan data
list_padi = []
list_kedelai = []
list_nama_lokasi = []

# Kumpulkan data dari semua lokasi
for kode_lokasi in data_panen:
    nama = data_panen[kode_lokasi]['nama_lokasi']
    padi = data_panen[kode_lokasi]['hasil_panen']['padi']
    kedelai = data_panen[kode_lokasi]['hasil_panen']['kedelai']
    
    list_nama_lokasi.append(nama)
    list_padi.append(padi)
    list_kedelai.append(kedelai)

# Tampilkan data padi
print("\nData Panen Padi Setiap Lokasi:")
for i in range(len(list_nama_lokasi)):
    print(f"  {list_nama_lokasi[i]}: {list_padi[i]} kg")

# Tampilkan data kedelai
print("\nData Panen Kedelai Setiap Lokasi:")
for i in range(len(list_nama_lokasi)):
    print(f"  {list_nama_lokasi[i]}: {list_kedelai[i]} kg")

# Buat dictionary untuk memudahkan akses
data_padi = {}
data_kedelai = {}

for kode_lokasi in data_panen:
    nama = data_panen[kode_lokasi]['nama_lokasi']
    data_padi[nama] = data_panen[kode_lokasi]['hasil_panen']['padi']
    data_kedelai[nama] = data_panen[kode_lokasi]['hasil_panen']['kedelai']

print("\nData Padi (dalam dictionary):")
print(data_padi)

print("\nData Kedelai (dalam dictionary):")
print(data_kedelai)

print("\n" + "=" * 50)
print("SOAL 6: PERCABANGAN KONDISI PANEN")
print("=" * 50)

print("\nStatus Kondisi Panen Setiap Lokasi:")
print("-" * 40)

# Cek kondisi setiap lokasi
for kode_lokasi in data_panen:
    nama = data_panen[kode_lokasi]['nama_lokasi']
    padi = data_panen[kode_lokasi]['hasil_panen']['padi']
    jagung = data_panen[kode_lokasi]['hasil_panen']['jagung']
    
    print(f"\nLokasi: {nama}")
    print(f"  Padi: {padi} kg, Jagung: {jagung} kg")
    
    # Percabangan if-else
    if padi > 1300 or jagung > 800:
        print("  STATUS: Perlu perhatian khusus!")
    else:
        print("  STATUS: Kondisi baik")

print("\n" + "=" * 50)
print("RINGKASAN")
print("=" * 50)

# Hitung total panen
total_padi = 0
total_jagung = 0
total_kedelai = 0

for kode_lokasi in data_panen:
    hasil = data_panen[kode_lokasi]['hasil_panen']
    total_padi += hasil['padi']
    total_jagung += hasil['jagung']
    total_kedelai += hasil['kedelai']

print(f"Total Panen Padi: {total_padi} kg")
print(f"Total Panen Jagung: {total_jagung} kg")
print(f"Total Panen Kedelai: {total_kedelai} kg")

print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)