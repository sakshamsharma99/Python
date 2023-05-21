import random
str_int = input("Give me everybody's names, separated by a comma.\n")

office = str_int.split(",")

print(random.choice(office) + " going to buy meal today.")