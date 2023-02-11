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
profit = 0


def ask_money():
    print("Please insert coins.")
    nk = int(input("How many nickels?: "))
    qt = int(input("How many quarters?: "))
    dm = int(input("How many dimes?: "))
    pn = int(input("How many pennies?: "))
    total = qt * 0.25 + dm * 0.10 + nk * 0.05 + pn * 0.01
    return round(total, 2)


def deduct_resources(drink_ingredient):
    """Deducts resources like water , milk , coffee for passed drink from resources"""
    for item in drink_ingredient:
        resources[item] = resources[item] - MENU[choice]['ingredients'][item]


def check_resources(drink_ingredient):
    """Returns False if resources insufficient , True if resources sufficient for the passed drink"""
    for item in drink_ingredient:
        if drink_ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


coffee_check = True


while coffee_check:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    elif choice == "off":
        print("Turning off coffee machine!")
        coffee_check = False
    else:
        drink = MENU[choice]
        can_serve = check_resources(drink['ingredients'])
        if can_serve:
            money_total = ask_money()
            if money_total < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
                coffee_check = False
            else:
                money_change = round((money_total - MENU[choice]['cost']), 2)
                deduct_resources(drink['ingredients'])
                profit = profit + MENU[choice]['cost']
                print(f"Here is your ${money_change} in change.")
                print(f"Here is your {choice} ☕ Enjoy!")
