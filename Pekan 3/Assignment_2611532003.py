# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_2003 = int(input("Input angka 1: "))
angka2_2003 = int(input("Input angka 2: "))

print("\nNilai awal angka 1 =",angka1_2003)
print("Nilai awal angka 2 =",angka2_2003)

# Assigment biasa
hasil_2003 = angka1_2003
print("\nAssigment biasa (=)")
print("Hasil =",hasil_2003)

# Assigment penambahan
hasil_2003 = angka1_2003
hasil_2003 += angka2_2003
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_2003)

# Assigment pengurangan
hasil_2003 = angka1_2003
hasil_2003 -= angka2_2003 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_2003)

# Assigment perkalian
hasil_2003 = angka1_2003
hasil_2003 *= angka2_2003
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_2003)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_2003 != 0:
    hasil_2003 = angka1_2003
    hasil_2003 /= angka2_2003
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_2003)
    # Operator tambahan
    hasil_2003 = angka1_2003
    hasil_2003 //= angka2_2003
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_2003)
    hasil_2003 = angka1_2003 
    hasil_2003 %= angka2_2003
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_2003)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_2003 = angka1_2003
hasil_2003 **= angka2_2003
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_2003)