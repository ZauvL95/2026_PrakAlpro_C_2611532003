# Buat file dengan nama If_elif_else1_NIM.py
# Buat program untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini mengggunakan fungsi input()

umur_2003 = int(input("Input umur anda: "))
sim_2003 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_2003 >= 17 and sim_2003 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_2003 >= 17 and sim_2003 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2003 < 17 and sim_2003 == "y":
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur bawa motor")

print("Program Selesai")