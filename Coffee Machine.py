Money = 0


def is_resources_enough(u):
    drink = MENU[u]
    for item in drink["ingredients"]:
        if resources[item] <= drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many 1 rupees: ")) * 1
    total += int(input("how many 2 rupees: ")) * 2
    total += int(input("how many 5 rupees: ")) * 5
    total += int(input("how many 10 rupees: ")) * 10
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is {change} in change.")
        global Money
        Money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
while is_on:
    user = input("What would yo like? (espresso/latte/cappuccino): ")

    if user == 'report':
        for key, value in resources.items():
            print("{}: {}".format(key, value))
        print(f"Money: ${Money}")
    elif user == 'off':
        is_on = False
    elif user == 'latte' or user == 'cappuccino' or user == 'espresso':
        if is_resources_enough(user):
            payment = process_coins()
            if is_transaction_successful(payment, MENU[user]['cost']):
                for i in MENU[user]['ingredients']:
                    resources[i] -= MENU[user]['ingredients'][i]
                print(f"Here is yours {user} ☕")
    else:
        print("Wrong Input")
