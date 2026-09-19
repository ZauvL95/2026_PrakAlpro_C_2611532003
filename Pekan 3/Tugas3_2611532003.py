print("==========================================")
print("     SISTEM TRANSAKSI TOKO")
print("==========================================")

nama_2003 = input("Masukkan Nama Pelanggan : ")
status_2003 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2003 = float(input("Masukkan Total Belanja : "))
jumlah_barang_2003 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2003 = input("Masukkan Kode Promo : ").upper()

daftar_promo_2003 = [
    "HEMAT10",
    "HEMAT20",
    "GRATISONGKIR"
]

promo_tersedia_2003 = kode_promo_2003 in daftar_promo_2003
promo_tidak_tersedia_2003 = kode_promo_2003 not in daftar_promo_2003
syarat_belanja_2003 = total_belanja_2003 >= 200000
syarat_barang_2003 = jumlah_barang_2003 >= 3
status_member_2003 = status_2003 == "member"

diskon_member_2003 = (status_member_2003 and syarat_belanja_2003)
promo_2003 = (syarat_belanja_2003 and syarat_barang_2003 and promo_tersedia_2003)
akses_member_2003 = status_member_2003 and syarat_belanja_2003
akses_promo_2003 = (syarat_barang_2003 and promo_tersedia_2003)
akses_khusus_2003 = (akses_member_2003 or akses_promo_2003)
bukan_member_2003 = not status_member_2003

diskon_2003 = 0

if diskon_member_2003:
    diskon_2003 = total_belanja_2003 * 0.10

elif syarat_belanja_2003:
    diskon_2003 = total_belanja_2003 * 0.05

total_pembayaran_2003 = total_belanja_2003 - diskon_2003
rata_rata_barang_2003 = (total_pembayaran_2003 / jumlah_barang_2003)
sisa_bagi_2003 = jumlah_barang_2003 % 2

poin_2003 = 0
if status_member_2003:
    poin_2003 += jumlah_barang_2003
if promo_2003:
    poin_2003 += 10

nilai_a_2003 = 100
nilai_b_2003 = nilai_a_2003

identitas_sama_2003 = nilai_a_2003 is nilai_b_2003
identitas_berbeda_2003 = nilai_a_2003 is not nilai_b_2003


kode_status_2003 = 0

if status_member_2003:
    kode_status_2003 |= 1

if syarat_belanja_2003:
    kode_status_2003 |= 2

if syarat_barang_2003:
    kode_status_2003 |= 4

if promo_tersedia_2003:
    kode_status_2003 |= 8


cek_member_2003 = kode_status_2003 & 1
cek_belanja_2003 = kode_status_2003 & 2
cek_barang_2003 = kode_status_2003 & 4
cek_promo_2003 = kode_status_2003 & 8

kode_gabungan_2003 = 1 | 8

kode_referensi_2003 = 0b1011
hasil_xor_2003 = kode_status_2003 ^ kode_referensi_2003

hasil_shift_2003 = kode_status_2003 << 1

print("\n==========================================")
print("           DATA PELANGGAN")
print("==========================================")
print("Nama Pelanggan       :", nama_2003)
print("Status Pelanggan     :", status_2003)
print("Total Belanja        : Rp", total_belanja_2003)
print("Jumlah Barang        :", jumlah_barang_2003)
print("Kode Promo           :", kode_promo_2003)

print("\n==========================================")
print("           HASIL VALIDASI")
print("==========================================")
print("Belanja >= Rp200000      :",syarat_belanja_2003)
print("Jumlah Barang >= 3       :",syarat_barang_2003)
print("Status Member            :",status_member_2003)
print("Kode Promo Tersedia       :",promo_tersedia_2003)
print("Kode Promo Tidak Tersedia :",promo_tidak_tersedia_2003)
print("Mendapatkan Diskon Member :",diskon_member_2003)
print("Mendapatkan Promo         :",promo_2003)

print("\n==========================================")
print("          HASIL PERHITUNGAN")
print("==========================================")
print("Besarnya Diskon       : Rp",diskon_2003)
print("Total Pembayaran      : Rp",total_pembayaran_2003)
print("Rata-rata Harga Barang: Rp",rata_rata_barang_2003)
print("Sisa Jumlah Barang / 2:",sisa_bagi_2003)

print("\n==========================================")
print("        HAK AKSES PELANGGAN")
print("==========================================")
print("Kode Hak Akses        :", kode_status_2003)
print("Member Access         :",akses_member_2003)
print("Promo Access          :",akses_promo_2003)
print("Akses Khusus          :",akses_khusus_2003)
print("Bukan Member          :",bukan_member_2003)
print("Poin Pelanggan        :",poin_2003)

print("\n==========================================")
print("         OPERATOR IDENTITY")
print("==========================================")
print("nilai_a_2003 is nilai_b_2003 :",identitas_sama_2003)
print("nilai_a_2003 is not nilai_b_2003 :",identitas_berbeda_2003)
print("Catatan: 'is' membandingkan identitas objek.")
print("         '==' membandingkan nilai/isi objek.")

print("\n==========================================")
print("          OPERASI BITWISE")
print("==========================================")
print("Kode Status Transaksi")
print("Member       : 0001")
print("Belanja      : 0010")
print("Jumlah Barang: 0100")
print("Kode Promo   : 1000")
print("\nKode Biner   :", format(kode_status_2003, "04b"))
print("Kode Desimal :", kode_status_2003)

print("\n--- Pemeriksaan Status ---")
print("\nCek Member")
print(format(kode_status_2003, "04b"),"& 0001")
print("Hasil Biner   :",format(cek_member_2003, "04b"))
print("Hasil Desimal :",cek_member_2003)
print("\nCek Promo")
print(format(kode_status_2003, "04b"),"& 1000")
print("Hasil Biner   :",format(cek_promo_2003, "04b"))
print("Hasil Desimal :",cek_promo_2003)

print("\n--- Operator OR ---")
print("0001 | 1000")
print("Hasil Biner   :",format(kode_gabungan_2003, "04b"))
print("Hasil Desimal :",kode_gabungan_2003)

print("\n--- Perbandingan Status XOR ---")
print("Kode Transaksi :",format(kode_status_2003, "04b"))
print("Kode Referensi :",format(kode_referensi_2003, "04b"))
print(format(kode_status_2003, "04b"),"^",format(kode_referensi_2003, "04b"))
print("Hasil Biner   :",format(hasil_xor_2003, "04b"))
print("Hasil Desimal :",hasil_xor_2003)

print("\n--- Operator Shift ---")
print(format(kode_status_2003, "04b"),"<< 1")
print("Hasil Biner   :",format(hasil_shift_2003, "b"))
print("Hasil Desimal :",hasil_shift_2003)

print("\n==========================================")
print("              SELESAI")
print("==========================================")