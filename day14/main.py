import random
from replit import clear
from art import logo, vs
from game_data import data

def get_random_data():
    return random.choice(data)

def format_data(account_a, account_b, score):
    print(logo)
    print(f"You're right! Current score: {score}") if score > 0 else ""
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
    
def check_answer(account_a, account_b, answer):
    if account_a["follower_count"] > account_b["follower_count"]:
        return answer == 'a'
    else:
        return answer == 'b'

def end_game(score):
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def game():
    account_a = get_random_data()
    account_b = get_random_data()
    score = 0
    game_over = False

    while not game_over:
        account_a = account_b
        account_b = get_random_data()
        while account_a == account_b:
            account_b = get_random_data()

        format_data(account_a, account_b, score)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_right = check_answer(account_a, account_b, answer)
        clear()
        if is_right:
            score = score + 1
        else:
            game_over = True
            end_game(score)

game()