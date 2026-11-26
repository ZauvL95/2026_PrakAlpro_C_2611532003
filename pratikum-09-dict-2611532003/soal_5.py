kas = {}

jumlah_setoran = int(input())

for i in range(jumlah_setoran):
    setor = input().split()
    nama = setor[0]
    nominal = int(setor[1])

    if nama in kas:
        kas[nama] += nominal
    else:
        kas[nama] = nominal

total = sum(kas.values())
terbesar = max(kas, key=kas.get)

for nama, jumlah in kas.items():
    print(f"{nama}: {jumlah}")

print("Total cash:", total)
print(f"Top contributor: {terbesar} ({kas[terbesar]})")