number_of_rows = 4
seats_per_row = 5
# Write your code below
board = []

for i in range(number_of_rows):
    row = ["."] * seats_per_row
    board.append(row)
seats_taken = 0

while True:
    for i in range(number_of_rows):
        print("Row", i + 1, ":", " ".join(board[i]))
        
    row_number = int(input("Row (0 to stop): "))

    if row_number == 0:
        break

    seat_number = int(input("Seat: "))

    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    elif board[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")
    else:
        board[row_number - 1][seat_number - 1] = "X"
        seats_taken = seats_taken + 1
        print("Seat booked.")

print("Seats taken:", seats_taken)