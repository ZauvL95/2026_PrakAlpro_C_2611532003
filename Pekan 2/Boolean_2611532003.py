# Buat file dengan nama Boolean_NIM.py
# Nama variable dtambah 4 digit terakhir contoh: nilai_1234
# Deklarasi variable dengan tipe data boolean
is_lulus_2003 = True
is_cumlaude_2003 = True

# Mengisi Boolean
nilai_2003 = 85
batas_lulus_2003 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2003 = nilai_2003 >= batas_lulus_2003 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2003)
print("Apakah Lulus?:", status_kelulusan_2003)
if is_lulus_2003 and is_cumlaude_2003:
    print("Selamat, Anda lulus dengan predikat Cum Laude")
