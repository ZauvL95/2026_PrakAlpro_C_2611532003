# Buat file dengan nama logika_NIM.py
# Nama variable ditambah 4 digit angka terakhir contoh:a1_1234
# Program ini mengggunakan fungsi input()
# Program operator logika dalam python

# Masukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2003 = input("Input nilai boolean 1 (true/false)").strip().lower() == "true"
a2_2003 = input("Input nilai boolean 2 (true/false)").strip().lower() == "true"

print("\nA1 =",a1_2003)
print("A2", a2_2003)

# Konjungsi: bernilai True jika keduanya True
hasil_2003 = a1_2003 and a2_2003
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_2003)

# Disjungsi: bernilai True jika salah satunya True
hasil_2003 = a1_2003 or a2_2003
print("\nKonjungsi (OR)")
print("A1 or A2 =", hasil_2003)

# Negasi A1: membalik nilai A1
hasil_2003 = not a1_2003
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_2003)

# Negasi A2: membalik nilai A1
hasil_2003 = not a2_2003
print("\nNegasi A12 (NOT)")
print("not A2 =", hasil_2003)

# XOR: Bernilai True jika kedua nilai berbeda
hasil_2003 = a1_2003 != a2_2003
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_2003)