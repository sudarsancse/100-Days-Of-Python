## coffee vending machine
from machine_data import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
is_On = True

def show_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: Rs {money}")

def items(item_name, order_ingredients):
    item_cost = MENU[item_name]["cost"]
    print(f"{item_name.capitalize()} price is Rs: {MENU[item_name]["cost"]}, Please insert coins.")
    coin = int(input("How many Rs 1 coin: ")) * 1
    coin += int(input("How many Rs 2 coin: ")) * 2
    coin += int(input("How many Rs 5 coin: ")) * 5
    coin += int(input("How many Rs 10 coin: ")) * 10
    if coin < MENU[item_name]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else :
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        change = coin - item_cost
        print(f"Here is your {item_name.capitalize()} ☕️. Enjoy!")
        if change > 0:
            print(f"Here is your refund of Rs {change}.")
        return item_cost
    
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            show_report()
            return False
    return True

while is_On:
    order = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if order == "report":
        show_report()
    elif order == "off":
        is_On = False
        show_report()
        print(f"Total profit: Rs {money}")
    else:
        dirnk = MENU[order]
        if is_resource_sufficient(dirnk["ingredients"]):
            money +=items(order,dirnk["ingredients"])
            