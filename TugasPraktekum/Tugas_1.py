print("====== Sistem Perhitungan Nilai Mahasiswa ======")
# ================= INPUT NILAI =================
nilai_tugas = int(input("Masukkan nilai tugas : "))
nilai_uts = int(input("Masukkan nilai UTS   : "))
nilai_uas = int(input("Masukkan nilai UAS   : "))

bobot_tugas = 30/100
bobot_uts = 30/100
bobot_uas = 40/100

nilai_akhir = (nilai_tugas * bobot_tugas) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)

print("Nilai akhir kamu adalah :", nilai_akhir)
print("----------------------------------------------------")

# ================= OPERATOR PENUGASAN ==================
satuan_tugas = nilai_tugas
satuan_uts = nilai_uts
satuan_uas = nilai_uas

satuan_tugas *= bobot_tugas
satuan_uts *= bobot_uts
satuan_uas *= bobot_uas

print("Nilai kontribusi Tugas :", satuan_tugas)
print("Nilai kontribusi UTS   :", satuan_uts)
print("Nilai kontribusi UAS   :", satuan_uas)

print("----------------------------------------------------")

# ================= OPERATOR PERBANDINGAN =================
if nilai_akhir >= 75:
    print("Status : LULUS")
else:
    print("Status : TIDAK LULUS")

print("----------------------------------------------------")

# ================= OPERATOR LOGIKA =================
if (nilai_akhir >= 75) and (nilai_uas >= 70):
    print("Status tambahan : LULUS SEMPURNA")

print("----------------------------------------------------")

# ================= OPERATOR IDENTITAS =================
nilai_asli = nilai_akhir
nilai_backup = nilai_asli

print("Nilai asli   :", nilai_asli, ", id:", hex(id(nilai_asli)))
print("Nilai backup :", nilai_backup, ", id:", hex(id(nilai_backup)))
print("Apakah nilai_asli is nilai_backup :", nilai_asli is nilai_backup)

print("----------------------------------------------------")

# ================= OPERATOR KEANGGOTAAN =================
peserta_ujian = ["andi", "budi", "citra", "dina"]
nama_mahasiswa = input("Masukkan nama Anda : ").lower()
if nama_mahasiswa in peserta_ujian:
    print("Nama anda ada di daftar peserta ujian")
else:
    print("Nama anda tidak ada di daftar peserta")

print("----------------------------------------------------")

# ================= OPERATOR BITWISE =================
a = 5
b = 3

print("======== AND ========")
c = a & b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== OR ========")
c = a | b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== XOR ========")
c = a ^ b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== Shift Kiri ========")
c = a << b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))

print("\n======== Shift Kanan ========")
c = a >> b
print("nilai a =", a, ", biner :", format(a, "08b"))
print("nilai b =", b, ", biner :", format(b, "08b"))
print("Hasil   =", c, ", biner :", format(c, "08b"))