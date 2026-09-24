# Buat file dengan nama Multi_if2_NIM.py
# Buat program untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: total_belanja_NIM.py
# Program ini mengggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2611532003 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2003 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_2003 = input_member_2003 in ['y', "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2003 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promot_valid_2003 = input_promo_2003 in ['y', "y"]

total_diskon_persen_2003 = 0

# Multi-IF terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk  (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2611532003 > 1000000:
    total_diskon_persen_2003 += 10

if is_member_2003:
    total_diskon_persen_2003 += 5

if kode_promot_valid_2003:
    total_diskon_persen_2003 += 15

# Menghitung nominal  diskon dan total belanja
nominal_diskon_2003 = total_belanja_2611532003 * (total_diskon_persen_2003 / 100)
total_bayar_2003 = total_belanja_2611532003 - nominal_diskon_2003

# Output hasil
print("/n--- Rincian Pembayaran ---")
print(f"Total Diskon    : {total_diskon_persen_2003}%(Rp{nominal_diskon_2003:,.0f})")
print(f"Total Bayar     : Rp {total_bayar_2003: ,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2003}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid