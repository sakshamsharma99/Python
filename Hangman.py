import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Welcome to Hangman Game")
word = ["mouse","sita","laxman","ravan","hanuman","dashrath"]

chosen_word = random.choice(word)
length = len(chosen_word)
print(chosen_word)
display = []
for n in range(length):
    display += "_"
lives = 6
end_of_game = False
def converter(display):
    s = " "
    return s.join(display)
while not end_of_game:
    if lives == 6:
        print(stages[6])
    elif lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[2])
    elif lives == 1:
        print(stages[1])
    elif lives == 0:
        print(stages[0])
        print("You Lose")
        exit()
    else:
        continue
    print(f"{converter(display)}\n\n\n")
    user_input = input("Guess a Letter: ").lower()
    for position in range(length):
        if user_input == chosen_word[position]:
            display[position] = user_input
            
    if user_input not in chosen_word:
        lives -= 1
    if "_" not in display:
        end_of_game = True
        print("You Win")
    
