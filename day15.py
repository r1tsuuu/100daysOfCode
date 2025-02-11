money_given = 0
profit = 0

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order):
    resources_not_enough = False
    if 'water' in MENU[order]["ingredients"] and MENU[order]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        resources_not_enough = True

    if 'milk' in MENU[order]["ingredients"] and MENU[order]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        resources_not_enough = True

    if 'coffee' in MENU[order]["ingredients"] and MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        resources_not_enough = True

    if resources_not_enough:
        return False

    return True

def update_resources(order):
    for resource in resources:
        if resource in MENU[order]["ingredients"]:
            resources[resource] -= MENU[order]["ingredients"][resource]

def insert_coins(coffee_cost):
    global money_given
    global profit

    print("Please insert coins.")
    try:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
    except (TypeError, ValueError):
        print("Please input integers!")
        return 1

    money_given += (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    change = coffee_cost - money_given

    if change < 0:
        print(f"Here is ${-change:.2f} in change.")
        money_given = 0

    elif change > 0:
        print("Insufficient coins, please insert more coins!")
        insert_coins(coffee_cost)

    else:
        print("You've entered exact amount!")
        money_given = 0

    profit += coffee_cost
    return

def start_order():
    order = input("What would you like? (espresso/latte/cappuccino)").lower()

    while order not in ['off', 'report', 'espresso', 'latte', 'cappuccino']:
        print("Invalid input!")
        order = input("What would you like? (espresso/latte/cappuccino)").lower()

    if order == 'off':
        print("Coffee Machine turning off.")
        return

    elif order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")

    else:
        check_resources(order)
        if check_resources(order):
            insert_coins(MENU[order]['cost'])
            update_resources(order)
            print("Here is your espresso ☕️. Enjoy!")

while True:
    start_order()