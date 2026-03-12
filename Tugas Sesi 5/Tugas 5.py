# Biodata sederhana menggunakan input dan format
nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
prodi = input("Masukkan prodi: ")

print("\nOutput:")
print("Nama: {}".format(nama))
print("Umur: {}".format(umur))
print("Prodi: {}".format(prodi))
print("\n")


# Kalimat
text = "UNIVERSITAS NUSA PUTRA SUKABUMI"
kata = text.split()

# a. putra nusa
print("a.", kata[2].lower(), kata[1].lower())

# b. NIVERSITAS NSA PTRA SKABMI
print("b.", kata[0][1:], kata[1][0] + kata[1][2:], kata[2][0] + kata[2][2:], kata[3][0] + kata[3][2:])

# c. SUKABUMI PUTRA NUSA UNIVERSITAS
print("c.", kata[3], kata[2], kata[1], kata[0])

# d. UNPS
print("d.", kata[0][0] + kata[1][0] + kata[2][0] + kata[3][0])

# e. TAS SAPU BUMI
print("e.", kata[0][-3:], kata[1][-1] + kata[2][:2], kata[3][4:])