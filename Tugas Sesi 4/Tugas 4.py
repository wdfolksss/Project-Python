#operator aritmatika
print("======Operator Aritmatika=======")
apel_awal = 12
teman = 4
tambahan_apel = 8

apel_per_teman = apel_awal / teman
total_apel = apel_awal + tambahan_apel

print("Total apel awal Budi:", apel_awal)
print("Jumlah teman:", teman)
print("Apel yang diterima setiap teman:", apel_per_teman)
print("Tambahan apel yang didapat Budi:", tambahan_apel)
print("Total apel Budi sekarang:", total_apel)
print("\n")

#operator perbandingan
print("=======Operator Perbandingan=======")
siti = 160
andi = 165
print("Apakah siti lebih tinggi dari andi?", siti > andi)
print("Apakah andi lebih tinggi dari siti?", andi > siti)
if andi > siti:
    print("andi lebih tinggi dari siti")
else:
    print("siti lebih tinggi dari andi")
print("\n")


#operator logika
print("=========Operator Logika==========")
cuaca_cerah = True
PR_udah_selesai = True
budi_bisa_bermain = cuaca_cerah and PR_udah_selesai
print("Apakah Budi bisa bermain?", budi_bisa_bermain)
print("\n")


# operator bitwise
print("======== Operator Bitwise ========")
a = 6
b = 3

print("Angka a =", a, "dalam biner =", bin(a))
print("Angka b =", b, "dalam biner =", bin(b))
print("Hasil AND:", a & b, "adalah", bin(a & b))
print("Hasil OR :", a | b, "adalah", bin(a | b))
print("Hasil XOR:", a ^ b, "adalah", bin(a ^ b))
print("\n")


#operator penugasan
print("========Operator Penugasan=======")
saldo_pulsa = 50000
print("Saldo awal:", saldo_pulsa)

saldo_pulsa += 20000
print("Setelah isi ulang 20000:", saldo_pulsa)

saldo_pulsa -= 30000
print("Setelah membeli paket internet 30000:", saldo_pulsa)
print("Sisa saldo pulsa:", saldo_pulsa)
print("\n")


# operator keanggotaan
print("======== Operator Keanggotaan ========")
daftar_peserta = ["Andi", "Budi", "Citra", "Dewi"]
print("Apakah Eka terdaftar sebagai peserta?")
print("Hasil:", "Eka" in daftar_peserta)

kalimat = "Saya suka belajar Python"
print("Apakah kata 'Python' ada dalam kalimat?")
print("Hasil:", "Python" in kalimat)
print("\n")


# operator identitas
print("======== Operator Identitas ========")
x = 10
y = 10
print(" hasil dari x is y:", x is y)
print("hasil dari x == y:", x == y)

x = ["apel", "jeruk"]
y = ["apel", "jeruk"]
print("hasil dari x is y:", x is y)
print("hasil dari x == y:", x == y)
print("\n")


#operator Ternary
print("========Operator Ternary=======")
angka = 100
hasil = "lebih besar dari 100" if angka > 100 else "tidak lebih besar dari 100"
print("hasil:", hasil)

nilai = 80
hasil = "lulus" if nilai > 70 else "tidak lulus"
print("hasil: ", hasil)