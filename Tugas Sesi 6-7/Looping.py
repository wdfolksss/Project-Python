while True:
    print("\n1. fanta - Rp.11000")
    print("2. sprite - Rp.12000")
    print("3. nipis_madu - Rp.15000")
    print("4. pucuk - Rp.13000")

    pilihan = input("Pilihan Minuman (1-4): ")

    if pilihan == "1":
        minuman = "fanta"
        harga = 11000
    elif pilihan == "2":
        minuman = "sprite"
        harga = 12000
    elif pilihan == "3":
        minuman = "nipis_madu"
        harga = 15000
    elif pilihan == "4":
        minuman = "pucuk"
        harga = 13000
    else:
        print("Pilihan Minuman tidak valid!")
        continue  

    print(f"\nKamu memilih {minuman} dengan harga Rp{harga}")

    total = 0
    jumlah_input = 0

    while total < harga:
        uang = int(input("Masukkan uang: Rp"))
        total += uang
        jumlah_input += 1
        print(f"Total uang yang dimasukkan: Rp{total}")

    kembalian = total - harga
    
    print("\n== Struk Belanja ==")
    print("Minuman:", minuman)
    print("Jumlah input:", jumlah_input)
    print("Total Bayar: Rp", total)
    print("Kembalian: Rp", kembalian)

    print("\nTerima kasih telah berbelanja!")

    ulang = input("Apakah Anda ingin membeli lagi? (y/n): ")
    if ulang.lower() != "y":
        print("Terimakasih telah menggunakan vending machine kami!")
        break