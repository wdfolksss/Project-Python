#variabel name, age, address, province, scorepython
name = "Warda"
age = 19
address = "Sukabumi"
province = "Jawa Barat"
ScorePython = 90
print("Name:", name, "Tipe data: ", type(name))
print("Age:", age, "Tipe Data: ", type(age))
print("Address:", address, "Tipe Data: ", type(address))
print("Province:", province, "Tipe Data: ", type(province))
print("ScorePython:", ScorePython, "Tipe Data: ", type(ScorePython))

print("==============================================================") 

#Casting 
# 1. Mengubah tipe data variabel Age menjadi string, float, dan boolean
print("A. Mengubah data integer ke string, float, dan boolean")
Age_str = str(age)
Age_float = float(age)
Age_bool = bool(age)

print("data :", Age_str,"-", type(Age_str))
print("data :", Age_float,"-", type(Age_float))
print("data :", Age_bool,"-", type(Age_bool))

print("=============================================================")    

# 2. mengubah tipe data variabel menjadi string, integer, dan boolean
# karena string tidak bisa diubah menjadi integer, maka akan terjadi error jika kita mencoba untuk mengubahnya menjadi integer.
# str to int, float, bool
print("B. Mengubah data String ke int, float, dan boolean")
data = "12"
data_int = int(data)
data_float = float(data)
data_bool = bool(data)

print("data :",data_int,"-", type(data_int))
print("data :",data_float,"-", type(data_float))
print("data :",data_bool,"-", type(data_bool))

print("=============================================================")

# mengubah float ke int, string, dan boolean
print("C.Mengubah float ke int, string, dan boolean")
ScorePython_int = int(ScorePython)
ScorePython_str = str(ScorePython)
ScorePython_bool = bool(ScorePython)

print("data :",ScorePython_int,"-", type(ScorePython_int))
print("data :",ScorePython_str,"-", type(ScorePython_str))
print("data :",ScorePython_bool,"-", type(ScorePython_bool))

print("=============================================================")

# mengubah boolean ke int, string, dan float 
print("D. Mengubah boolean ke int, string, dan float")  
data_bool = True
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data :",data_int,"-", type(data_int))
print("data :",data_str,"-", type(data_str))
print("data :",data_float,"-", type(data_float))