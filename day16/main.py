from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

def start():
    continueRunning = True
    while continueRunning:
        response = input(f"What would you like? ({my_menu.get_items()}): ").lower()

        if response not in ["espresso", "latte", "cappuccino", "off", "report"]:
            print("Invalid choice. Please choose a valid drink.")
            continue

        elif response == "off":
            print("Turning off Coffee Machine.")
            continueRunning = False
            break

        elif response == "report":
            my_coffee_maker.report()
            my_money_machine.report()
            continue

        else:
            process_drink(response)

def process_drink(drink_name):
    drink = my_menu.find_drink(drink_name)
    if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
        my_coffee_maker.make_coffee(drink)

start()