import random
def loop(n):
    for _ in range(n):
        print(f"\nYou have {n} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("Bravo, You Win 😎")
            exit()
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too Small")
        n -= 1
        if n == 0:
            print("\nYou lose 🤦‍♀️\n")
            print(f"I guess {random_number}")

def _(scenario):
    if scenario == "hard":
        loop(5)
    else:
        loop(10)
print('''
   _____                       _______ _            _   _                      _          
  / ____|                     |__   __| |          | \ | |                    | |         
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___   ___| |__  _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \ / _ \ '_ \| '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | |  __/ |_) | |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|\___|_.__/|_|   
                                                                                          
                                                                                          
''')
print("\nWelcome to the Number Guessing Game!\n\nI'm thinking of a number between 1 and 100.")
is_game_over = False
random_number = random.randint(1,100)
environment = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
if environment == "hard":
    _("hard")
else:
    _("easy")