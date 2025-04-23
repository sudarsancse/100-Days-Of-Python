## object oriented programing
#construct a object

# from turtle import *

# tim = Turtle()
# tim.shape("turtle")
# tim.color("green")
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.forward(100)
# tim.left(120)
# tim.forward(200)
# tim.left(120)
# tim.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# from prettytable import PrettyTable
# table = PrettyTable()
# table.field_names=["Pocikemon name" ,"Type"]
# table.add_rows([
#     ["Pikachu", "Electric"],
#     ["Squirtle","Water"],
#     ["Charmander" ,"Fire"]
# ])
# table.align= "l"

# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choise = str(input(f"What would you like? ({options}): ")).lower()
    if choise == "off":
        is_on = False
    elif choise == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choise)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost ):

                coffee_maker.make_coffee(drink)