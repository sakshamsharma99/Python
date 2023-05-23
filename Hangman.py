import random
import Hangman_resource
print(Hangman_resource.logo)
chosen_word = random.choice(Hangman_resource.word_list)
length = len(chosen_word)
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
        print(Hangman_resource.stages[6])
    elif lives == 5:
        print(Hangman_resource.stages[5])
    elif lives == 4:
        print(Hangman_resource.stages[4])
    elif lives == 3:
        print(Hangman_resource.stages[3])
    elif lives == 2:
        print(Hangman_resource.stages[2])
    elif lives == 1:
        print(Hangman_resource.stages[1])
    elif lives == 0:
        print(Hangman_resource.stages[0])
        print("You Lose")
        print(f"Word : {chosen_word}")
        exit()
    else:
        continue
    print(f"{converter(display)}\n\n")
    user_input = input("Guess a Letter: ").lower()
    for position in range(length):
        if user_input == chosen_word[position]:
            display[position] = user_input
    if user_input in display:
        print(f"You've already guessed {user_input}")
    if user_input not in chosen_word:
        lives -= 1
        print(f"You guessed {user_input}, that's not in the word, You lose a life.")
    if "_" not in display:
        end_of_game = True
        print(f"{converter(display)}")
        print("You Win") 