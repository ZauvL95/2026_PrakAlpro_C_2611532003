nomor_absent = set(input().split())
submit = set(input().split())

print("Submitted:", len(nomor_absent & submit), "students")
print("Not Submitted:", len(nomor_absent - submit), "students")

not_submitted = nomor_absent - submit

for i in nomor_absent:
    if i in not_submitted:
        print(i)