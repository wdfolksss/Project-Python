target = int(input("Masukkan target uang Rp: "))

total_tabungan = 0
hari = 0

while total_tabungan < target:
    tabungan = int(input(f"Masukkan jumlah tabungan hari ke- {hari+1}: "))
    
    total_tabungan += tabungan
    hari += 1

    print("Total Sementara: Rp", total_tabungan)

    if total_tabungan < target:
        sisa = target - total_tabungan
        print("Sisa yang harus ditabung: Rp", sisa)

print("\n === Target Tercapai ===")
print("Total Tabungan: Rp", total_tabungan)
print("Jumlah Hari yang dibutuhkan: ", hari)
