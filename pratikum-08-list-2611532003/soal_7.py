menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for i in range(number_of_days):
    row = []
    for j in range(len(menus)):
        quantity = int(input("Day " + str(i + 1) + ", " + menus[j] + ": "))
        row.append(quantity)
    sales.append(row)

print("Total per day:")

for i in range(number_of_days):
    total = 0
    for j in range(len(menus)):
        total = total + sales[i][j]
    print("Day", i + 1, ":", total)

menu_totals = []

for j in range(len(menus)):
    total = 0
    for i in range(number_of_days):
        total = total + sales[i][j]
    menu_totals.append((menus[j], total))

print("Total per menu:", menu_totals)

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print("Best seller:", best_name, "(" + str(best_total) + ")")