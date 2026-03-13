print("=== Posisi Pemain Sepak Bola ===")

nomor = int(input("Masukkan nomor punggung: "))

# genap
if nomor % 2 == 0:
    print("Posisi: Target Attacker")

# genap 50–100
if nomor % 2 == 0 and 50 <= nomor <= 100:
    print("Posisi: Calon Captain")

# ganjil
if nomor % 2 != 0:
    print("Posisi: Defender")

# ganjil > 90
if nomor % 2 != 0 and nomor > 90:
    print("Posisi: Playmaker")

# ganjil kelipatan 3 dan 5
if nomor % 2 != 0 and nomor % 3 == 0 and nomor % 5 == 0:
    print("Posisi: Keeper")