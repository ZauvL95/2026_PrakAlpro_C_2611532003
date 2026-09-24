print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# ------------------------------------------------------------
# 1. INPUT DATA PENGUNJUNG
# ------------------------------------------------------------

nama_2003 = input("Masukkan Nama Pengunjung        : ")
umur_2003 = int(input("Input umur anda                 : "))
sim_2003 = input(
    "Apakah Anda Sudah Punya SIM C (y/t): "
).strip().lower()[0]

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_2003 = int(input("\nMasukkan nomor paket (1-5)   : "))
jumlah_tiket_2003 = int(input("Masukkan jumlah tiket         : "))
is_member_2003 = input("Apakah Anda member? (y/t)     : ").strip().lower()
kode_promo_valid_2003 = input("Apakah kode promo valid? (y/t): ").strip().lower()


# ------------------------------------------------------------
# 2. VALIDASI JUMLAH TIKET
# IF TUNGGAL
# ------------------------------------------------------------

if jumlah_tiket_2003 <= 0:
    print("\nPeringatan: Kuota tiket tidak valid.")


# ------------------------------------------------------------
# 3. PEMILIHAN WAHANA DENGAN MATCH-CASE
# ------------------------------------------------------------

match paket_2003:

    case 1:
        nama_wahana_2003 = "Wahana Safari Rimba"
        harga_satuan_2003 = 50000

    case 2:
        nama_wahana_2003 = "Wahana Arung Jeram"
        harga_satuan_2003 = 75000

    case 3:
        nama_wahana_2003 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2003 = 120000

    case 4:
        nama_wahana_2003 = "Wahana Roller Coaster Kilat"
        harga_satuan_2003 = 100000

    case 5:
        nama_wahana_2003 = "Wahana All-Access VIP"
        harga_satuan_2003 = 220000

    case _:
        print("\nPaket wahana tidak valid!")
        raise SystemExit


# ------------------------------------------------------------
# 4. VALIDASI KELAYAKAN PENGENDARA
# TIDAK MENGGUNAKAN NESTED-IF
# ------------------------------------------------------------

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2003 == 3 and umur_2003 >= 17 and sim_2003 == 'y':
    status_akses_2003 = (
        "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
    )

elif paket_2003 == 3 and umur_2003 >= 17 and sim_2003 != 'y':
    status_akses_2003 = (
        "Anda sudah dewasa tetapi tidak boleh bawa motor ATV "
        "(wajib didampingi instruktur)."
    )

elif paket_2003 == 3 and umur_2003 < 17 and sim_2003 == 'y':
    status_akses_2003 = (
        "Identitas tidak valid: Belum cukup umur memiliki SIM."
    )

elif paket_2003 == 3 and umur_2003 < 17 and sim_2003 != 'y':
    status_akses_2003 = (
        "Anda belum cukup umur dan tidak boleh bawa motor ATV."
    )

elif paket_2003 != 3 and umur_2003 >= 10:
    status_akses_2003 = (
        "Anda memenuhi batas usia untuk wahana ini."
    )

else:
    status_akses_2003 = (
        "Anda belum cukup umur untuk wahana ini."
    )

print("Status Akses:", status_akses_2003)


# ------------------------------------------------------------
# 5. MENGHITUNG SUBTOTAL
# ------------------------------------------------------------

subtotal_2003 = harga_satuan_2003 * jumlah_tiket_2003


# ------------------------------------------------------------
# 6. MULTI-IF TERPISAH UNTUK DISKON AKUMULATIF
# ------------------------------------------------------------

total_diskon_persen_2003 = 0

# Diskon Belanja Besar
if subtotal_2003 >= 200000:
    total_diskon_persen_2003 += 10

# Diskon Member
if is_member_2003 in ['y', 'ya']:
    total_diskon_persen_2003 += 5

# Diskon Voucher Promo
if kode_promo_valid_2003 in ['y', 'ya']:
    total_diskon_persen_2003 += 15

# Diskon Tambahan Rombongan
if jumlah_tiket_2003 >= 5:
    total_diskon_persen_2003 += 5


# ------------------------------------------------------------
# 7. MENGHITUNG TOTAL PEMBAYARAN
# ------------------------------------------------------------

nominal_diskon_2003 = (
    subtotal_2003 * (total_diskon_persen_2003 / 100)
)

total_bayar_2003 = (
    subtotal_2003 - nominal_diskon_2003
)


# ------------------------------------------------------------
# 8. EVALUASI BONUS
# IF-ELSE
# ------------------------------------------------------------

if total_bayar_2003 > 300000:
    catatan_layanan_2003 = (
        "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    )
else:
    catatan_layanan_2003 = (
        "Terima kasih telah berkunjung."
    )


# ------------------------------------------------------------
# 9. MENAMPILKAN RINCIAN PEMBAYARAN
# ------------------------------------------------------------

print(f"Subtotal Belanja  : Rp {subtotal_2003:,.0f}")
print(
    f"Total Diskon      : {total_diskon_persen_2003}% "
    f"(Rp {nominal_diskon_2003:,.0f})"
)
print(f"Total Bayar       : Rp {total_bayar_2003:,.0f}")
print(f"Catatan Layanan   : {catatan_layanan_2003}")
print("\nProgram Selesai")