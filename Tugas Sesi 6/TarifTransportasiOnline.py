print("===========Tarif Transportasi Online==============")

jarak = int(input("Masukkan Jarak Perjalanan per km: "))

if jarak <= 5:
    harga = 5000
    print("Harga: Rp", harga)
elif 6 <= jarak <= 10:
    harga = 4000
    print("Harga: Rp", harga)
elif jarak > 10:
    harga = 3000
    print("Harga: Rp", harga)
else:
    harga = 0
    print("Tidak Valid")

total = harga * jarak 
print("Total tarif perjalanan: Rp", total)
