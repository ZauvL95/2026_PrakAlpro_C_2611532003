print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_2003 = int(input("Masukkan ukuran skala jam pasir (N): "))

if n_2003 <= 0:
    print("Ukuran N harus berupa bilangan bulat positif.")
else:
    lebar_2003 = 4 * n_2003 + 7

    for posisi_2003 in range(1, lebar_2003 + 1):
        if posisi_2003 == 1 or posisi_2003 == lebar_2003:
            print("#", end="")
        else:
            print("=", end="")
    print()

    for baris_2003 in range(n_2003, 0, -1):
        print("|", end="")

        print(" ", end="")

        for spasi_2003 in range(2 * (n_2003 - baris_2003)):
            print(" ", end="")

        for angka_2003 in range(baris_2003, 0, -1):
            print(angka_2003, end="")
            print(" ", end="")

        print("<*>", end="")

        print(" ", end="")
        for angka_2003 in range(1, baris_2003 + 1):
            print(angka_2003, end="")
            if angka_2003 < baris_2003:
                print(" ", end="")

        for spasi_2003 in range(2 * (n_2003 - baris_2003)):
            print(" ", end="")

        print(" ", end="")
        print("|", end="")
        print()

    print("|", end="")
    for spasi_2003 in range(2 * n_2003 + 1):
        print(" ", end="")
    print("<*>", end="")
    for spasi_2003 in range(2 * n_2003 + 1):
        print(" ", end="")
    print("|", end="")
    print()

    for baris_2003 in range(1, n_2003 + 1):
        print("|", end="")

        print(" ", end="")

        for spasi_2003 in range(2 * (n_2003 - baris_2003)):
            print(" ", end="")

        for angka_2003 in range(baris_2003, 0, -1):
            print(angka_2003, end="")
            print(" ", end="")

        print("<*>", end="")

        print(" ", end="")
        for angka_2003 in range(1, baris_2003 + 1):
            print(angka_2003, end="")
            if angka_2003 < baris_2003:
                print(" ", end="")

        for spasi_2003 in range(2 * (n_2003 - baris_2003)):
            print(" ", end="")

        print(" ", end="")
        print("|", end="")
        print()

    for posisi_2003 in range(1, lebar_2003 + 1):
        if posisi_2003 == 1 or posisi_2003 == lebar_2003:
            print("#", end="")
        else:
            print("=", end="")
    print()
