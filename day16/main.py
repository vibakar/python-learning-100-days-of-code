from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}) ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
