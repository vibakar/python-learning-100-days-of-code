from random import randint

print("Welcome to the Number Guessing game!")

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    chances = HARD_LEVEL if level == 'hard' else EASY_LEVEL
    return chances

def check_answer(guess, number_to_find, no_of_chances):
    if guess == number_to_find:
        print(f"You got it. Answer is {number_to_find}")
        return no_of_chances
    elif guess > number_to_find:
        print("Too high")
        return no_of_chances - 1
    elif guess < number_to_find:
        print("Too low")
        return no_of_chances - 1
        
def game():
    print("I'm thinking of a number between 1 and 100")
    number_to_find = randint(1, 100)
    no_of_chances = set_difficulty()
    guess = 0

    while no_of_chances > 0 and guess != number_to_find:
        print(f"You have {no_of_chances} chances to guess the number")
        guess = int(input("Make a guess: "))
        no_of_chances = check_answer(guess, number_to_find, no_of_chances)

        if no_of_chances == 0 and guess != number_to_find:
            print("You have run out of guesses. You Lose!!!")

game()