# snack game
from turtle import Screen
from snake import Snake
from food import Food
from score_bord import Scorebord
import time

game_is_on = True
screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)
speed_input = screen.textinput(title="Game Lable " ,prompt="Easy, Hard and Normal ").lower()

if speed_input == "easy":
    move_speed = 0.15
elif speed_input == "hard":
    move_speed = 0.05
else:  
    move_speed = 0.1

snake= Snake()
food = Food()
scorebord = Scorebord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

segments = []

while game_is_on:
    screen.update()
    time.sleep(move_speed)

    snake.move()
    
    # food collision
    if snake.head.distance(food) < 15:
        scorebord.incress_score()
        snake.extent_snake()
        food.refresh()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scorebord.game_over()

    # collision with snake taill
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorebord.game_over()

screen.exitonclick()