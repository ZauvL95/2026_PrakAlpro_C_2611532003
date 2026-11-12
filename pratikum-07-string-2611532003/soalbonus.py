# Name: Marvel Teja
# NIM: 2611532003
# Bonus Question

kalimat = input("Masukkan kalimat: ")

clean_kalimat = kalimat.replace(" ", "").lower()

if clean_kalimat == clean_kalimat[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")