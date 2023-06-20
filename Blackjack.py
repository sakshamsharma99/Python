import random

def deal_card():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "\n\nDraw"
    elif computer_score == 0:
        return "\n\nLose, opponent has Blackjack"
    elif user_score == 0:
        return "\n\nWin with a Blackjack"
    elif user_score > 21:
        return "\n\nYou went over. You lose"
    elif computer_score > 21:
        return "\n\nOpponent wentover. You win"
    elif user_score > computer_score:
        return "\n\nYou Win 😁"
    else:
        return "\n\nYou lose"
    
def play_game():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"    Your cards: {user_card}, current score: {user_score}")
        print(f"    Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("TYpe 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"    Your final hand: {user_score}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()