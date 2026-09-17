# Buat file dengan nama Lainnnya_NIM.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program Operator keanggotaan dan identitas

print("===============================")
print("1. OPERATOR KEANGGOTAAN")
print("===============================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2003 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2003 = [int(angka_2003.strip()) for angka_2003 in input_data_2003.split(",")]

nilai_dicari_2003 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2003 = nilai_dicari_2003 in data_2003
print("\nOperator keanggotaan IN")
print(nilai_dicari_2003, "in", data_2003, "=", hasil_2003)

#Operator not in
hasil_2003 = nilai_dicari_2003 not in data_2003
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2003, "not in", data_2003, "=", hasil_2003)


print("\n===============================")
print("2. OPERATOR IDENTIAS")
print("===============================")

# objek1 menggunakan list dari input perngguna
object1_2003 = data_2003

# objek2 merujuk pada objek yang sama dengan objek1
object2_2003 = object1_2003

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_2003 = data_2003.copy()

print("object1 =",object1_2003)
print("object2 =",object2_2003)
print("object3 =",object3_2003)

# Operator is
hasil_2003 = object1_2003 is object2_2003
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_2003)

# Operator is not
hasil_2003 = object1_2003 is not object3_2003
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =",hasil_2003)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_2003 is object3_2003)
print("objek1 == objek3 =",object1_2003 == object3_2003)