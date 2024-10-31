from itertools import filterfalse
import time
import random

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


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def calculate_coin_total():
    """Calculates and returns the total amount from coins inserted."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        total = quarters + dimes + nickels + pennies
        return round(total, 2)
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return 0.0


def simulate_upi_transaction():
    """Simulates an automatic UPI payment verification."""
    print("Please scan the QR code to pay via UPI.")
    print("Waiting for payment confirmation...")

    # Simulate waiting for a response (3 seconds)
    time.sleep(3)

    # Randomly determine payment success or failure
    payment_success = random.choice([True, False])

    if payment_success:
        print("UPI payment successful!")
        return True
    else:
        print("UPI payment failed. Please try again.")
        return False


def process_payment(drink_cost):
    """Handles the payment process, giving users the choice between coins and UPI."""
    print("Select payment method:")
    print("1. Insert coins")
    print("2. Pay via UPI")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        total_amount = calculate_coin_total()
        print(f"Total amount from coins: ${total_amount}")
        if total_amount >= drink_cost:
            change = round(total_amount - drink_cost, 2)
            if change > 0:
                print(f"Here is your change: ${change}")
            return True
        else:
            print("Sorry, that's not enough money. Refunding coins.")
            return False
    elif choice == '2':
        if simulate_upi_transaction():
            print("Payment completed successfully.")
            return True
        else:
            print("Payment not confirmed. Please try again or use another payment method.")
            return False
    else:
        print("Invalid choice. Please select a valid payment option.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:
    choice_ = input("What would you like to have? (espresso, latte, cappuccino): ").lower()

    if choice_ == "off":
        is_on = False
    elif choice_ == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    elif choice_ in MENU:
        drink = MENU[choice_]
        if is_resource_sufficient(drink["ingredients"]):
            if process_payment(drink["cost"]):
                make_coffee(choice_, drink["ingredients"])
                profit += drink["cost"]
    else:
        print("Invalid choice. Please select a valid drink.")
