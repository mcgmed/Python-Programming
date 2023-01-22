logo = """
  ______       ___  ___              ______              _     _             
 / _____)     / __)/ __)            |  ___ \            | |   (_)            
| /      ___ | |__| |__ ____ ____   | | _ | | ____  ____| | _  _ ____   ____ 
| |     / _ \|  __)  __) _  ) _  )  | || || |/ _  |/ ___) || \| |  _ \ / _  )
| \____| |_| | |  | | ( (/ ( (/ /   | || || ( ( | ( (___| | | | | | | ( (/ / 
 \______)___/|_|  |_|  \____)____)  |_||_||_|\_||_|\____)_| |_|_|_| |_|\____
"""

print(logo)

menu = {
    "espresso": {"ingredients": {"water": 50,
                                 "milk":0,
                                 "coffee": 18},
                 "cost": 1.5},
    "latte": {"ingredients": {"water": 200,
                              "milk": 150,
                              "coffee": 24},
              "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250,
                                   "milk": 100,
                                   "coffee": 24},
                   "cost": 3.0}
}

resources = {"water": 300,
             "milk": 200,
             "coffee": 100,
             "money": 0}


def resource_checker(order, resources):
    for i in order['ingredients']:
        if order['ingredients'][i] > resources[i]:
            print(f"Sorry, there is not enough {i}.")
            return False
        else:
            return True


def money_calculator(order, resources):
    print("Please insert coin")
    quarter = int(input("How many quarters: "))
    nickel = int(input("How many nickels: "))
    dime = int(input("How many dimes: "))
    penny = int(input("How many pennies: "))
    total = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    if total < order["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total >= order["cost"]:
        change = total - order['cost']
        print(f"Here is ${round(change, 2)} dollars change")
        resources['money'] += order["cost"]
        return True


def prepare_drink(order, resources):
    for i in order['ingredients']:
        resources[i] -= order['ingredients'][i]


machine_on = True

while machine_on:
    query = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if query == 'off':
        print("The machine has closed")
        machine_on = False
    elif query == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        order = menu[query]
        if resource_checker(order, resources):
            if money_calculator(order, resources):
                prepare_drink(order, resources)
                print(f"Here is your {query}. Enjoy!")
