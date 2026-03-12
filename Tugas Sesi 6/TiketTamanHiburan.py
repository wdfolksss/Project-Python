#menentukan tiket taman hiburan
print("=====Tiket Taman Hiburan=====")

tiket1 = int(input("Masukkan umur Anda: "))
if 0 <= tiket1 <= 12:
    harga1 = 10000
    print("Harga: Rp", harga1)
elif 13 <= tiket1 <= 17:
    harga1 = 15000
    print("Harga: Rp", harga1)
elif 18 <= tiket1 <= 59:
    harga1 = 25000
    print("Harga: Rp", harga1)
elif tiket1 >= 60:
    harga1 = 0
    print("Harga: Rp", harga1)
else:
    print("Bukan Manusia")
    print("Harga: Rp", harga1)

tiket2 = int(input("Masukkan umur Anda: "))
if 0 <= tiket2 <= 12:
    harga2 = 10000
    print("Harga: Rp", harga2)
elif 13 <= tiket2 <= 17:
    harga2 = 15000
    print("Harga: Rp", harga2)
elif 18 <= tiket2 <= 59:
    harga2 = 25000
    print("Harga: Rp", harga2)
elif tiket2 >= 60:
    harga2 = 0
    print("Harga: Rp", harga2)
else:
    print("Bukan Manusia")
    print("Harga: Rp", harga2)

tiket3 = int(input("Masukkan umur Anda: "))
if 0 <= tiket3 <= 12:
    harga3 = 10000
    print("Harga: Rp", harga3)
elif 13 <= tiket3 <= 17:
    harga3 = 15000
    print("Harga: Rp", harga3)
elif 18 <= tiket3 <= 59:
    harga3 = 25000
    print("Harga: Rp", harga3)
elif tiket3 >= 60:
    harga3 = 0
    print("Harga: Rp", harga3)
else:
    print("Bukan Manusia")    
    print("Harga: Rp", harga3)

print("\nHasil:")
total = harga1 + harga2 + harga3
print("Total harga tiket: Rp", total)
