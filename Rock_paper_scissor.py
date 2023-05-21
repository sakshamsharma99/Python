import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Wrong Input")
    exit()

combine = [rock,paper,scissors]
computer = random.randint(0,len(combine)-1)
answer = combine[computer]
print(f"Computer chose:\n{answer}")

if user_input == computer:
    print("It's a draw")
elif user_input == 1 and computer == 0 or user_input == 0  and computer == 2 or user_input == 2 and computer == 1:
    print("You win")
else:
    print("You lose")