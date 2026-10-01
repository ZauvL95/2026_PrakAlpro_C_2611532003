# Buat file dengan nama Nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variable ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2003 = int(input("Masukkan tinggi pola (bilangan genap)"))

if tinggi_2003 % 2 !=0:
    print("Tinggi harus bilangan genap")
else:
    a_2003 = tinggi_2003
    c_2003 = a_2003
    lebar_2003 = (2 * tinggi_2003) - 2

    for i_2003 in range(1, tinggi_2003 + 1):
        b_2003 = c_2003 + 1

        for j_2003 in range(1, lebar_2003 + 1):

            # Baris atas dan bawah
            if i_2003 == 1 or i_2003 == tinggi_2003:
                if j_2003 == 1 or j_2003 == lebar_2003:
                    print("#", end="")
                else:
                    print("=", end="")

            #Baris isi
            else:
                if j_2003 == 1 or j_2003 == lebar_2003:
                    print("|", end="")
                else:
                    if j_2003 == c_2003:
                        print("<", end="")
                    elif j_2003 == b_2003:
                        print(">", end="")
                    elif j_2003 == (lebar_2003 - c_2003):
                        print("<", end="")
                    elif j_2003 == (lebar_2003 - c_2003 + 1):
                        print(">", end="")
                    elif j_2003 > b_2003 and j_2003 < (lebar_2003 - c_2003):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli java
        a_2003 -= 2

        if a_2003 <= 0:
            c_2003 = (-a_2003) + 2
        else:
            c_2003 = a_2003