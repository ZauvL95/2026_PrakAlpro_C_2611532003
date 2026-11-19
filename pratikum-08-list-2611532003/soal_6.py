LAST_DIGIT = 3  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for i in range(7):
    expense = int(input("Day " + str(i + 1) + ": "))
    expenses.append(expense)

total = 0
highest = expenses[0]
highest_day = 1
days_above_limit = 0

for i in range(7):
    total = total + expenses[i]
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above_limit = days_above_limit + 1

average = total / 7

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", format(average, ".1f"))
print("Highest: day", highest_day, "(" + str(highest) + ")")
print("Days above limit:", days_above_limit)