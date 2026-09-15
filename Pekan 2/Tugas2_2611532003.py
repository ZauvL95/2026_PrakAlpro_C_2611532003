from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_2003 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2003 = input("Masukkan Jenis Kelamin (L/P): ")
alamat_2003 = """Jl. Kotomarapak no 16,
Padang Barat,
Kota Padang"""
umur_2003 = int(input("Masukkan Umur : "))
nilai_2003 = float(input("Masukkan Skor Tes Awal : "))

token_2003 = 100 + 3j
lulus_2003 = nilai_2003 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_2003, "| Tipe:", type(nama_2003))
print("Jenis Kelamin :", jenis_kelamin_2003, "| Tipe:", type(jenis_kelamin_2003))
print("Alamat Domisili:")
print(alamat_2003, "| Tipe:", type(alamat_2003))
print("Umur :", umur_2003, "tahun | Tipe:", type(umur_2003))
print("Skor Tes Awal :", nilai_2003, "| Tipe:", type(nilai_2003))
print("ID Token Sinyal:", token_2003, "| Tipe:", type(token_2003))
print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", lulus_2003, "| Tipe:", type(lulus_2003))