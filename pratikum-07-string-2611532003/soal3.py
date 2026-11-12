# Name: Marvel Teja
# NIM: 2611532003
# Question 3

# Bagian A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# Bagian B
text = "Marvel Teja"
text = text.lower()
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
