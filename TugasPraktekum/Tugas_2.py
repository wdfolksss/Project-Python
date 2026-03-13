# Program Sistem Analisis Penjualan Toko Online
nama_pelanggan = input("Masukkan nama pelanggan: ")
jumlah_barang = int(input("Masukkan jumlah barang: "))
harga_barang = float(input("Masukkan harga barang: "))
member = input("Apakah pelanggan member? (ya/tidak): ")
kode_diskon = input("Masukkan kode diskon: ")

total = 0
diskon = 0
biaya_pengiriman = 20000
kategori = ""
diskon_tambahan = 0

# OPERATOR ARITMATIKA
total = jumlah_barang * harga_barang

# diskon jika beli > 10 barang
if jumlah_barang > 10:
    diskon = total * 0.05

# OPERATOR PENUGASAN
total -= diskon
total += biaya_pengiriman

# OPERATOR PERBANDINGAN
if total >= 1000000:
    kategori = "Pembelian Besar"
elif total >= 500000:
    kategori = "Pembelian Sedang"
else:
    kategori = "Pembelian Kecil"

# OPERATOR LOGIKA
if member == "ya" and total > 500000:
    diskon_tambahan = total * 0.1
    total -= diskon_tambahan

# OPERATOR KEANGGOTAAN
kode_valid = ["HEMAT10", "PROMO20", "SALE30"]

if kode_diskon in kode_valid:
    total -= 500000
    status_diskon = "Kode diskon valid"
else:
    status_diskon = "Kode diskon tidak valid"

# OPERATOR IDENTITAS
data_pelanggan = nama_pelanggan
data_cache = data_pelanggan

if data_pelanggan is data_cache:
    cek_data = "Data pelanggan sama di memori"
else:
    cek_data = "Data pelanggan berbeda"

# OPERATOR BITWISE
status = 6
izin = 3

bit_and = status & izin
bit_or = status | izin
bit_xor = status ^ izin
shift_kiri = status << 1
shift_kanan = status >> 1

# OUTPUT
print("\n===== HASIL ANALISIS PENJUALAN =====")
print("Nama Pelanggan:", nama_pelanggan)
print("Total Belanja:", total)
print("Kategori Pembelian:", kategori)
print("Status Diskon:", status_diskon)
print("Cek Data:", cek_data)

print("\nOperasi Bitwise:")
print("AND:", bit_and)
print("OR:", bit_or)
print("XOR:", bit_xor)
print("Shift Kiri:", shift_kiri)
print("Shift Kanan:", shift_kanan)