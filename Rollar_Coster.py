height = float(input("What's your height (cm): "))
rupees = 0
if height >= 120:
    print("You can ride rollar coster\n")
else:
    print("Sorry you have to grow taller\n")
    exit()

age = int(input("What's your age: "))
print()
if age < 12:
    print("Child Ticket $5\n")
    rupees = 5
elif age <=18:
    print("Young Ticket $7\n")
    rupees = 7
else:
    print(("Adult Ticket $12\n"))
    rupees = 12

photo = input("Do you want photo for $3(yes or no): ")

if photo == 'yes':
    rupees = rupees + 3
    print(f"Your Total fair Charge: {rupees}")
else:
    print(f"Your Total fair Charge: {rupees}")