# Name: Marvel Teja
# NIM: 2611532003
# Question 5

# Bagian A
username = input("Username: ")
len_user= len(username)

if len_user >= 5:
    if username.isalnum():
        if username[0].isalpha():
            print("Valid")
        else:
            print("Invalid: must start with a letter")
    else:
        print("Invalid: letters and digits only")
else: 
    print("Invalid: at least 5 characters")

# Bagian B

nim = input("NIM: ")

if len(nim) == 10 and nim.isdigit():
    print(f"Valid, intake year 20{nim[0:2]}")
else:
    print("Invalid NIM")