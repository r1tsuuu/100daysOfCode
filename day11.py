import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)


def compare_scores(player_score, computer_score):
    if player_score > 21:
        return "You lose!"
    if computer_score > 21 or player_score > computer_score:
        return "You win!"
    if player_score == computer_score:
        return "Push!"
    return "You lose!"


def display_status(player_cards, player_score, computer_cards):
    print(f"    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Computer's cards: {computer_cards}")


def play():
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card()]
    print(logo)

    while True:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        display_status(player_cards, player_score, computer_cards)

        if player_score >= 21 or computer_score >= 21:
            break

        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while choice not in ['y', 'n']:
            choice = input("Invalid input! Type 'y' to get another card, type 'n' to pass: ").lower()

        if choice == 'y':
            player_cards.append(deal_card())
        else:
            break

    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(player_score, computer_score))


def main():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        play()


if __name__ == "__main__":
    main()