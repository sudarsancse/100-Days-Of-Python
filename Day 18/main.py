from turtle import *
import random


tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
tim.speed("fastest")

colors = ["dark blue", "chartreuse", "olive drab", "teal", "red", "indigo", "royal blue", "maroon"]
direction = [0, 90, 180 , 278]


# def draw_shap(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)


# for shape in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shap(shape)


def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    return (r, g, b)


# tim.pensize(15)
# tim.speed(10)

# for _ in range(300):
#     tim.color(random_color())
#     tim.forward(40)
#     tim.setheading(random.choice(direction))


def draw_spirograp(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        heading = tim.heading()
        tim.setheading(heading + size_of_gap)
        tim.circle(100)
        tim.color(random_color())

draw_spirograp(5)

screen.exitonclick()