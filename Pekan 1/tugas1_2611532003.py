while True:
    angka_1 = int(input("Masukkan angka pertama: "))
    angka_2 = int(input("Masukkan angka kedua: "))
    operasi = input("Masukkan operasi (+, -, *, /): ")

    def tambah(a, b):
        hasil = a + b
        return hasil

    def kurang(a, b):
        hasil = a - b
        return hasil

    def kali(a, b):
        hasil = a * b
        return hasil

    def bagi(a, b):
        hasil = a / b
        return hasil

    if operasi == "+":
        print("Hasil penjumlahan adalah:", tambah(angka_1, angka_2))
    elif operasi == "-":
        print("Hasil pengurangan adalah:", kurang(angka_1, angka_2))
    elif operasi == "*":
        print("Hasil perkalian adalah:", kali(angka_1, angka_2))
    elif operasi == "/":
        print("Hasil pembagian adalah:", bagi(angka_1, angka_2))
    else:
        print("Operasi tidak valid. Silakan masukkan operasi yang benar (+, -, *, /).")
