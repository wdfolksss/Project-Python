print("===========Aplikasi Streaming Film==============")

umur = int(input("Masukkan umur: "))
kategori = input("Masukkan Kategori Film (Dewasa/Remaja/Semua Umur): ")

if kategori == "dewasa":
    if umur >= 18:
        print("Boleh Menonton")
    else:
        print("Tidak Boleh Menonton")

elif kategori == "remaja":
    if umur >= 13:
        print("Boleh Menonton film Remaja")
    else:
        print("Tidak Boleh Menonton")

elif kategori == "Semua Umur":
    print("Boleh Menonton")

else:
    print("Kategori film tidak terdaftar")
