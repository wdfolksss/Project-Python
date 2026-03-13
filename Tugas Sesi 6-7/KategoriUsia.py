#Menentuka kategori usia
print("===========Kategori Usia==============")

umur = int(input("Masukkan umur Anda: "))

if 0 <= umur <= 12:
    print("Kategori: Anak-anak")
if 13 <= umur <= 17:
    print("Kategori: Remaja")
if 18 <= umur <= 59:
    print("Kategori: Dewasa")
if umur >= 60:
    print("Kategori: Lansia")


