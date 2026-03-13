#Program Beasiswa
print("===========Program Beasiswa==============")

nilai_rapor = int(input("Masukkan nilai rapor: "))
penghasilan = int(input("Masukkan Penghasilan Orang tua: "))

if nilai_rapor >= 90 and penghasilan < 5000000:
    hasil = "Beasiswa Penuh"
    print("Selamat Anda mendapatkan beasiswa penuh")
elif nilai_rapor >= 85 and penghasilan < 8000000:
    hasil = "Beasiswa Penuh 50%"
    print("Selamat Anda mendapatkan beasiswa 50%")
else:
    hasil = "Tidak dapat Beasiswa"
    print("Mohon maaf Anda tidak mendapatkan beasiswa")

print ("Hasil seleksi: ", hasil)

    