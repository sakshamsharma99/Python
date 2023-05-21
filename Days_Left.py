age = int(input("Enter age: "))

year_left = 100 - age

days = year_left*365
months = year_left*12
weeks = year_left*52

print(f"Months : {months}")
print(f"Days: {days}")
print(f"Weeks: {weeks}")