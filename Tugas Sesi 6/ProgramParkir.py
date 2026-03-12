print("===========Program Parkir==============")

jenis_kendaraan = input("Masukkan Jenis Kendaraan (Mobil/Motor): ") .lower()
lama_parkir = int(input("Lama parkir (jam): "))

if jenis_kendaraan == "mobil":
    tarif = 5000
    print("Harga tarif per jam:", tarif)
elif jenis_kendaraan == "motor":
    tarif = 2000
    print("Harga tarif per jam:", tarif)
else: 
    tarif = 0
    print("kendaraan tidak dikenal")

total = tarif * lama_parkir

if lama_parkir > 5:
    total = total + 10000
    print("Terkena biaya tambahan Rp. 10.000 karna lebh dari 5 jam")

print("Total biaya parkir: Rp", total)


