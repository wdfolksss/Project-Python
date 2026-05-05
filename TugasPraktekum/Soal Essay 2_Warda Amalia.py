nama = ""
ayam = 0
telur = 0   

nama = input("Nama Kandang :")
ayam = int(input("Jumlah ayam : "))

for hari in range(1,8):
    telur_hari_ini = int(input(f"Jumlah telur hari ke-{hari} : "))
    telur = telur + telur_hari_ini

rata = ayam / telur

if rata >= 0.8 :
    kategori = "Produktif tinggi"
elif rata >= 0.5 and rata < 0.79 :
    kategori = "Produktif sedang"
else :
    kategori = "Produktif Rendah"

print(f"Nama Kandang: {nama}")
print(f"Jumlah ayam: {ayam}")
print(f"Jumlah telur: {telur}")
print(f"Rata-rata telur per ayam: {rata:.2f}")
print(f"Kategori: {kategori}")