print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill += tip/100 * bill
people = int(input("How many people to split the bill? "))
result = bill / people
answer = round(result,2)
print(f"Each person sshould pay: ${answer}")