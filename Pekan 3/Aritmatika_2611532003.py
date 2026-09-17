# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam python
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan di konversi menjadi tipe data integer

angka1_2003 = int(input("Input angka 1: "))
angka2_2003 = int(input("Input angka 2: "))

#Penjumlahan
hasil_2003 = angka1_2003 + angka2_2003
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2003)

#Pengurangan
hasil_2003 = angka1_2003 - angka2_2003
print("\nOperator Pengurangan")
print("Hasil =", hasil_2003)

#Perkalian
hasil_2003 = angka1_2003 * angka2_2003
print("\nOperator Perkalian")
print("Hasil =", hasil_2003)

#Pembagian
if angka2_2003 != 0:
    hasil_2003 = angka1_2003 / angka2_2003
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2003)

    hasil_2003 = angka1_2003 // angka2_2003
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2003)

    hasil_2003 = angka1_2003 % angka2_2003
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2003)
else:
    print("Angka kedua tidak boleh bernilai 0")

#Pangkat
hasil_2003 = angka1_2003 ** angka2_2003
print("\nOperator Pangkat")
print("Hasil =", hasil_2003)