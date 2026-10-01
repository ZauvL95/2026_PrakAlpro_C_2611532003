# Buat file dengan nama Nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2003 = int(input("Masukkan nilai batas: "))
for i_2003 in range(batas_2003 + 1):
    for j_2003 in range(batas_2003 + 1):
        print(i_2003 + j_2003, end="")
    print() # Pindah ke baris berikutnya
