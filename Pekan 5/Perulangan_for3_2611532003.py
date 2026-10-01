# Buat file dengan nama Perulangan_for1_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2003 = int(input("Masukkan jumlah perulangan: "))

jumlah_2003 = 0
for i_2003 in range(1, ulang_2003 + 1):
    print(i_2003, end=" ")
    jumlah_2003 = jumlah_2003 + i_2003

    if i_2003 < ulang_2003:
        print(" + ", end="")
    else:
        print(" = ", end="")

print()
print("Jumlah =", jumlah_2003)