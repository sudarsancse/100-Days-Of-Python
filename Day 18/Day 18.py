from turtle import *
import colorgram
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("slowest")

rgb_colors = []
colors = colorgram.extract('Image/image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

def go():
    set_position = tim.pos()
    for _ in range (1,10):
        tim.dot(10)
        tim.up()
        tim.color(random.choice(rgb_colors))
        tim.fd(30)
        tim.dot(10)
    tim.setposition(set_position)
    tim.lt(90)
    tim.up
    tim.color(random.choice(rgb_colors))
    tim.fd(30)
    tim.rt(90)

for _ in range(10):
    go()

screen.exitonclick()
