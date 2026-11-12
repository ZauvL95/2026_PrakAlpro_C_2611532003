# Name: Marvel Teja
# NIM: 2611532003
# Question 4

phone = "082611532003"
masked = phone[:4] + "*" * len(phone[4:-3]) + phone[-3:]
print(masked)
