# Name: Marvel Teja
# NIM: 2611532003
# Question 7

full_name = "Marvel Teja"
nim = "2611532003"
clean_name = full_name.strip().lower()
position = clean_name.find(" ")

if position == -1:
    username = clean_name + nim[-3:]
else:
    username = clean_name[:position] + nim[-3:]

intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {full_name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)
