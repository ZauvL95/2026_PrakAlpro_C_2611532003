schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# Bagian A
busiest_day = ""
max_count = 0
for day in schedule:
    count = len(schedule[day])
    if count > max_count:
        max_count = count
        busiest_day = day
print(f"Busiest day: {busiest_day} ({max_count} courses)")

# Bagian B
course = input("Course name: ")
days_count = 0
for day in schedule:
    if course in schedule[day]:
        days_count += 1
print(f"{course}: {days_count} days")