#Diskon Restoran
print("===========Diskon Restoran==============")

umur = int(input("Masukkan umur: "))
harga = int(input("Masukkan harga: "))

if 0 <= umur <= 12:
    diskon = 0.5
    print("Selamat yaa! Anda mendapatkan diskon anak-anak 50%")
elif umur >= 60:
    diskon = 0.3
    print(" Selamat yaa! Anda dapat diskon lansia 30%")
else: 
    diskon = 0 
    print("Maaf, tidak ada diskon untuk kategori enih")

potongan = harga * diskon
total = harga - potongan

print(f"Harga setelah diskon: Rp {int(total)}")