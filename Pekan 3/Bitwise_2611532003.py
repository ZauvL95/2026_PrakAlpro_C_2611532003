# Buat file dengan nama Bitwise_NIM.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("===============================")
print("3. OPERATOR BITWISE")
print("===============================")

angka1_2003 = int(input("Input angka bitwise 1: "))
angka2_2003 = int(input("Input angka bitwise 2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("Angka 1", angka1_2003, "| biner =", bin(angka1_2003))
print("Angka 2", angka2_2003, "| biner =", bin(angka2_2003))

# Bitwise AND
hasil_2003 = angka1_2003 & angka2_2003
print("\nBitwise AND (&)")
print(angka1_2003, "&", angka2_2003, "=", hasil_2003)
print("Biner hasil =", bin(hasil_2003))
print("Biner hasil (8 bit) =", format(hasil_2003, "08b"))

# Bitwise OR
hasil_2003 = angka1_2003 | angka2_2003
print("\nBitwise OR (|)")
print(angka1_2003, "|", angka2_2003, "=", hasil_2003)
print("Biner hasil =", bin(hasil_2003))
print("Biner hasil (8 bit) =", format(hasil_2003, "08b"))

# Bitwise XOR
hasil_2003 = angka1_2003 ^ angka2_2003
print("\nBitwise XOR (^)")
print(angka1_2003, "^", angka2_2003, "=", hasil_2003)
print("Biner hasil =", bin(hasil_2003))
print("Biner hasil (8 bit) =", format(hasil_2003, "08b"))

# Bitwise NOT
hasil_2003 = ~angka1_2003
print("\nBitwise NOT (-)")
print("~", angka1_2003, "=", hasil_2003)
print("Biner hasil =", bin(hasil_2003))
print("Biner hasil (8 bit) =", format(hasil_2003, "08b"))

# Bitwise geser kiri
jumlah_geser_2003 = int(input("\nMasukkan jumlah pergeseran bit:"))

hasil_2003 = angka1_2003 << jumlah_geser_2003
print("\nBitwise geser kiri(<<)")
print(angka1_2003, "<<", jumlah_geser_2003,"=", hasil_2003)
print("Biner hasil =", bin(hasil_2003))
print("Biner hasil (8 bit) =", format(hasil_2003, "08b"))

# Bitwise geser kanan
hasil_2003 = angka1_2003 >> jumlah_geser_2003
print("\nBitwise geser kanan(>>)")
print(angka1_2003, ">>", jumlah_geser_2003, "=",hasil_2003)
print("Biner hasil =", bin(hasil_2003))
print("Biner hasil (8 bit) =", format(hasil_2003, "08b"))