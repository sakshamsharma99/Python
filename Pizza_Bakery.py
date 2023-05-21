print("Welcome to Pizza Bakery")

size = input("What's the size of Pizza (S, M or L): ")
bill = 0
if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else: bill = 25

pepperoni = input("Do you want Pipper(Y or N): ")

if pepperoni == 'Y':
    bill = bill + 2

extra_cheese = input("Do you want extra Cheese(Y or N): ")

if extra_cheese == 'Y':
    bill= bill+3

print(f"Your Bill is ${bill}")