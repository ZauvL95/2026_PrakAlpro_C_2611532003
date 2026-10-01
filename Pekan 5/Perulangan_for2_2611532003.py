# Buat file dengan nama Perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2003 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2003-1)
for i_2003 in range(ulang_2003):
    print(i_2003, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2003)
for i_2003 in range(1, ulang_2003+1):
    print(i_2003, end=" ")