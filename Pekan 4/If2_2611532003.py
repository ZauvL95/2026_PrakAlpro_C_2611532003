# Buat file dengan nama If2_NIM.py
# Buat program untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini mengggunakan fungsi input()

ipk_2003 = float(input("Input IPK Anda: "))

if ipk_2003 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK "+str(ipk_2003))
else:
    print("Anda Tidak Lulus")

print("Program Selesai")