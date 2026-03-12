print("=== Seleksi Calon Programmer ===")

nilai_coding = int(input("Masukkan nilai coding: "))
nilai_interview = input("Masukkan nilai interview (A/B/C/dll):")

if nilai_coding > 80:
    status_coding = "LOLOS"
elif 60 <= nilai_coding <= 80:
    status_coding = "DIPERTIMBANGKAN"
else:
    status_coding = "GAGAL"

if nilai_interview == "A" or nilai_interview == "B":
    status_interview = "LOLOS"
else:
    status_interview = "GAGAL"

if (status_coding == "LOLOS" or status_coding == "DIPERTIMBANGKAN") and status_interview == "LOLOS":
    print("Selamat Kamu Berhasil Menjadi Calon Programmer")
else:
    print("Maaf Kamu Belum Berhasil")