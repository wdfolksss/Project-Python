print("===========Diskon Toko==============")

total_belanja = float(input("Masukkan total belanja:"))

if total_belanja >= 500000:
    diskon = 0.2
    print("Selamat kamu mendapatkan diskon 20%")
elif total_belanja >= 250000:
    diskon = 0.1
    print("Selamat kamu mendapatkan diskon 10%")
else:
    diskon = 0
    print("Maast, Tidak ada Diskon")

potongan = total_belanja * diskon
harga_akhir = total_belanja - potongan

print("Harga Akhir: Rp ", int(harga_akhir))
