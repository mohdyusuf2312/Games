import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def play_game():
    player_cards = []
    computer_card = []
    is_gameover = False

    for n in range(2):
        player_cards.append(deal_card())
        computer_card.append(deal_card())

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_card)
    print(f"   Your cards: {player_cards}, current score : {player_score}")
    print(f"   Computer's first card: {computer_card[0]}")

    if player_score == 0 or computer_score == 0 or player_score > 21:
        is_gameover = True
    else:
        player_should_deal = input("Type 'y' to get another card, type 'n' to pass : ").lower()
        if player_should_deal == 'y':
            player_cards.append(deal_card())
        else:
            is_gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"Your final hand : {player_cards} , final score: {player_score}")
    print(f"Computers hand : {computer_card}, Computer's score : {computer_score}")
    print(compare(player_score,computer_score))

def compare(player_score,computer_score):
    if player_score == computer_score:
        return "its a draw :-) "
    elif computer_score == 0:
        return "You Loose, Opponent has a blackjack!"
    elif player_score == 0:
        return "You won with a blackjack!"
    elif player_score > 21:
        return "You went over, you loose."
    elif computer_score > 21:
        return "Opponent went over. you win!"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You loose"

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()=='y':
    play_game()