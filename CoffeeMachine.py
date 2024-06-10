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
Money = 0
quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

def calculator():
    quarters = int(input('How many quarters?: '))
    quarters = quarters * quarter
    dimes = int(input('How many dimes?: '))
    dimes = dimes * dime
    nickles = int(input('How many nickles?: '))
    nickles = nickles * nickle
    pennies = int(input('How many pennies?: '))
    pennies = pennies * penny
    total = quarters + dimes + nickles + pennies
    return total
def drink_or_report():
    global Money
    off = False
    while off == False:
        user_input = input('What would you like? (espresso/latte/cappuccino): ')
        user_input = user_input.lower()
        if user_input == 'report':
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${Money}')
        elif user_input == 'espresso':
            print('Please insert coins.')
            espresso_cost = float(calculator()) - MENU["espresso"]["cost"]
            if espresso_cost >= 0 and resources["water"] >= 50 and resources["coffee"] >= 18:
                print(f'Here is ${espresso_cost:.2f} in change.')
                print('Here is your espresso Enjoy!')
                Money += 1.50
                resources["water"] -= 50
                resources["coffee"] -= 18
            elif espresso_cost < 0:
                print("Sorry that's not enough money. Money refunded.")
            elif resources["water"] < 50:
                print('Sorry there is not enough water')
            elif resources["coffee"] < 18:
                print('Sorry there is not enough coffee')
        elif user_input == 'latte':
            print('Please insert coins.')
            latte_cost = float(calculator()) - MENU["latte"]["cost"]
            if latte_cost >= 0 and resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
                print(f'Here is ${latte_cost:.2f} in change.')
                print('Here is your latte Enjoy!')
                Money += 2.50
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24
            elif latte_cost < 0:
                print("Sorry that's not enough money. Money refunded.")
            elif resources["water"] < 200:
                print('Sorry there is not enough water')
            elif resources["milk"] < 150:
                print('Sorry there is not enough milk')
            elif resources["coffee"] < 24:
                print('Sorry there is not enough coffee')
        elif user_input == 'cappuccino':
            print('Please insert coins.')
            cappuccino_cost = float(calculator()) - MENU["cappuccino"]["cost"]
            if cappuccino_cost >= 0 and resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
                print(f'Here is ${cappuccino_cost:.2f} in change.')
                print('Here is your cappuccino Enjoy!')
                Money += 3.00
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24
            elif cappuccino_cost < 0:
                print("Sorry that's not enough money. Money refunded.")
            elif resources["water"] < 250:
                print('Sorry there is not enough water')
            elif resources["milk"] < 100:
                print('Sorry there is not enough milk')
            elif resources["coffee"] < 24:
                print('Sorry there is not enough coffee')
        elif user_input == 'off':
            off = True
drink_or_report()