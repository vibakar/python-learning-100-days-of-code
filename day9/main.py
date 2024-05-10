from replit import clear
from art import logo

print("Welcome to the secret auction program.")
print(logo)

list_of_players = []
continue_game = True
highest_bid = 0
winner = ""

while continue_game:
    player_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    list_of_players.append({
        "name": player_name,
        "bid": bid_amount
    })

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders == 'no':
        continue_game = False
    clear()

for player in list_of_players:
    if player["bid"] > highest_bid:
        highest_bid = player["bid"]
        winner = player["name"]

print(f"The winner is {winner} with a bid of ${highest_bid}")
        