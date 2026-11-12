# Name: Marvel Teja
# NIM: 2611532003
# Question 6

# Pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Soal 6
full_name = "Marvel Teja"
nim = "2611532003"
clean_name = full_name.strip().lower()
position = clean_name.find(" ")

if position == -1:
    username = clean_name + nim[-3:]
else:
    username = clean_name[:position] + nim[-3:]

print(username)