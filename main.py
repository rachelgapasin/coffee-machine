from coffee_data import MENU, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_collected, drink_cost):
    if money_collected >= drink_cost:
        change = money_collected - drink_cost
        formatted_change = "{:.2f}".format(change)
        if change > 0:
            print(f"Here is ${formatted_change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded...")
        return False


def make_coffee(order_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order_name} ☕️. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    while choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        formatted_profit = "{:.2f}".format(profit)
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${formatted_profit}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        order = MENU[choice]
        if is_resource_sufficient(order["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, order["cost"]):
                make_coffee(choice, order["ingredients"])
