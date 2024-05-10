MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def add_to_profit(order):
    global profit
    profit = round(profit + MENU[order]['cost'],2)

def make_coffee(order):
    for ingredient in MENU[order]['ingredients']:
        resources[ingredient] = resources[ingredient] - MENU[order]['ingredients'][ingredient]
    add_to_profit(order)
    print(f"Here is your {order}. Enjoy!!!")

def get_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def check_resource(order):
    for ingredient in MENU[order]['ingredients']:
        if resources[ingredient] < MENU[order]['ingredients'][ingredient] and resources[ingredient] != MENU[order]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def power_on_machine():
    power_on = True
    while power_on:
        order = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "off":
            power_on = False
        elif order == 'report':
            for key in resources:
                print(f"{key.title()}: {resources[key]}")
            print(f"Money: {profit}")
        else:
            if check_resource(order):
                coins = get_coins()
                if coins > MENU[order]["cost"] or coins == MENU[order]["cost"]:
                    balance = coins - MENU[order]["cost"]
                    print(f"Here is ${round(balance, 2)} in change.") if balance > 0 else ""
                    make_coffee(order)
                elif coins < MENU[order]["cost"]:
                    print("Sorry that's not enough money. Money refunded")
            
power_on_machine()