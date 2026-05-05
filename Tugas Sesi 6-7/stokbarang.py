# Sistem Manajemen Toko Sederhana

barang = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Transaksi")
    print("4. Update Stok")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    # 1. Tambah Barang
    if pilihan == "1":
        nama = input("Nama barang: ")
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))

        barang.append({
            "nama": nama,
            "harga": harga,
            "stok": stok
        })
        print("Barang berhasil ditambahkan!")

    # 2. Lihat Barang
    elif pilihan == "2":
        if not barang:
            print("Belum ada barang.")
        else:
            print("\nDaftar Barang:")
            for i, b in enumerate(barang):
                print(f"{i}. {b['nama']} | Harga: {b['harga']} | Stok: {b['stok']}")

    # 3. Transaksi
    elif pilihan == "3":
        nama_cari = input("Masukkan nama barang: ")
        jumlah = int(input("Jumlah beli: "))

        ditemukan = False

        for b in barang:
            if b["nama"].lower() == nama_cari.lower():
                ditemukan = True
                if b["stok"] >= jumlah:
                    b["stok"] -= jumlah
                    print("Transaksi berhasil!")
                else:
                    print("Stok tidak cukup!")
                break

        if not ditemukan:
            print("Barang tidak ditemukan!")

    # 4. Update Stok
    elif pilihan == "4":
        nama_cari = input("Masukkan nama barang: ")
        tambah = int(input("Tambah stok: "))

        ditemukan = False

        for b in barang:
            if b["nama"].lower() == nama_cari.lower():
                b["stok"] += tambah
                ditemukan = True
                print("Stok berhasil diperbarui!")
                break

        if not ditemukan:
            print("Barang tidak ditemukan!")

    # 5. Keluar
    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")