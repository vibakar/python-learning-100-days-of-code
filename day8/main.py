from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_ended = False

while not game_ended:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # def caeser(text, shift, direction):
    result = ""
    for letter in text:
        if letter in alphabet:
            if direction == 'encode':
                position = alphabet.index(letter) + (shift % 26)
            elif direction == 'decode':
                position = alphabet.index(letter) - (shift % 26)
            result+= alphabet[position]
        else:
            result+= letter
    print(f"{direction}d text is : {result}")

    # caeser(text, shift, direction)
    user_input = input("Would you like to continue? Please enter 'yes' or 'no': \n")
    if user_input == 'no':
        game_ended = True

