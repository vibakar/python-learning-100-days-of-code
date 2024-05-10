import random
from replit import clear
from art import logo

print(f"{logo} \n")

cards = [11, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 10, 10, 10]
play_game = True

while play_game:
    user_cards = []
    dealer_cards = []
    user_cards_total = 0
    dealer_cards_total = 0
    is_game_over = False

    def deal_card():
        return random.choice(cards)

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_score(user_score, dealer_score):
        print(f"Dealers crd: {' '.join(map(str, dealer_cards))}")
        if user_score == dealer_score:
            return "draw"
        elif dealer_score == 0:
            return "Dealer had a blackjack. You Lose"
        elif user_score == 0:
            return "You Won"
        elif user_score > 21:
            return "You went over. You lose"
        elif dealer_score > 21:
            return "Dealer went over. You won"
        elif user_score > dealer_score:
            return "You won"
        else:
            return "You lose"

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_cards_total = calculate_score(user_cards)
        dealer_cards_total =  calculate_score(dealer_cards)

        print(f"Your card: {' '.join(map(str, user_cards))}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_cards_total == 0 or dealer_cards_total == 0 or user_cards_total > 21:
            is_game_over = True
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if new_card == 'y':
                user_cards.append(deal_card())
                user_cards_total = calculate_score(user_cards)
            else:
                is_game_over = True

    while dealer_cards_total != 0 and dealer_cards_total < 17:
        dealer_cards.append(deal_card())
        dealer_cards_total = calculate_score(dealer_cards)

    print(compare_score(user_cards_total, dealer_cards_total))

    continue_game = input("Wanna continue playing game? Type 'y' or 'n': ")
    if continue_game == 'n':
        play_game = False
    if continue_game == 'y':
        clear()