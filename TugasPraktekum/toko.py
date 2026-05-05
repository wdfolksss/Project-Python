total = 0

jumlah_data = int(input("Masukkan jumlah barang: "))

i = 1
while i <= jumlah_data:
    print(f"\nBarang ke-{i}")
    
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))

    subtotal = harga * jumlah
    total += subtotal

    print(f"Subtotal {nama}: Rp{subtotal}")
    print("-" * 30)

    i += 1

# Hitung diskon
diskon = 0
if total >= 100000:
    diskon = total * 0.1  # 10%

# Hitung cashback
cashback = 0
if total >= 100000:
    cashback = 20000

total_bayar = total - diskon - cashback

# Output
print("\n=== STRUK BELANJA ===")
print(f"Total Belanja : Rp{total}")
print(f"Diskon        : Rp{int(diskon)}")
print(f"Cashback      : Rp{cashback}")
print(f"Total Bayar   : Rp{int(total_bayar)}")