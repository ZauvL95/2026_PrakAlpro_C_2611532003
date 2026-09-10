# Buat nama dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2003 = float(input('Masukkan nilai jari jari: '))
luas_2003 = PI * jari_2003 *jari_2003
print("Luas lingkaran dengan jari jari %.2f adalah %.2f" % (jari_2003,luas_2003))
