from replit import clear
from art import logo

print(logo)
game_on = True
result = 0

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculate(first_number):
    for operator in operations:
        print(f"{operator} \n")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the second number?: "))

    calculate = operations[operation]
    result = calculate(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    return result

first_number = float(input("What's the first number?: "))
result = calculate(first_number)

while game_on:
    continue_game = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if continue_game == 'y':
        result = calculate(result)
    if continue_game == 'n':
        game_on = False