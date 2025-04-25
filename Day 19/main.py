# from turtle import *

# tim = Turtle()
# screen =Screen()


# def move_forword():
#     tim.fd(10)

# def move_backout():
#     tim.bk(10)

# def counter_clockwise():
#     tim.lt(10)

# def right_clockwise():
#     tim.rt(10)

# def clear():
#     tim.clear()
#     tim.up()
#     tim.home()
#     tim.down()

# screen.listen()
# screen.onkey(key = "w", fun = move_forword)
# screen.onkey(key = "s", fun = move_backout)
# screen.onkey(key = "a", fun = counter_clockwise)
# screen.onkey(key = "d", fun = right_clockwise)
# screen.onkey(key = "c", fun = clear)


# screen.exitonclick()



from turtle import *
import random

is_race_on = False
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make the bet" ,prompt="Which turtle win the race? Enter a color: ")
y_postions = [-70, -40, -10, 20, 50,80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-240, y=y_postions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You won the race! The {wining_color} turtle is the winer")
            else:
                print(f"You lose the race! The {wining_color} turtle is the winer")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


screen.exitonclick()