# generate the random word

# display the dashes, whose count should be the length of the word

# ask user to enter the word

# if the guess is right display the letter replacing dashes
# if not reduce the life

import random
from hangman_words import word_list
from hangman_art import stages,logo

print("Welcome to Hangman game!!! \n")
print(f"{logo}")

chosen_word = random.choice(word_list)
display = []
lives = 6
end_of_game = False

for _ in range(len(chosen_word)):
    display.append("_")
print(f"{' '.join(display)} \n")

while not end_of_game :
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already guessed {guess}")

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You Lose!!!")
            print(f"The word is {chosen_word}")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Won!!!")

    print(stages[lives])