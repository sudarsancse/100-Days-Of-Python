# Pong game
from turtle import Screen
from paddel import Paddel
from ball import Ball
from score_bord import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong game")
screen.tracer(0)

game_win_score = int(screen.textinput(title="Winning Point", prompt="Enter your winning point: "))


r_paddel = Paddel((380, 0))
l_paddel = Paddel((-390, 0))
ball = Ball()
score = Score((game_win_score))


screen.listen()
screen.onkeypress(r_paddel.go_up, "Up")
screen.onkeypress(r_paddel.go_down, "Down")

screen.onkeypress(l_paddel.go_up, "w")
screen.onkeypress(l_paddel.go_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    ## detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        time.sleep(ball.ball_move_speed)
        ball.bounce_y()

    ## detect collision with both_paddel
    if ball.distance(r_paddel) < 50 and ball.xcor() > 340 or ball.distance(l_paddel) < 30 and ball.xcor() < -340 :
        ball.bounce_x()

    # detect r_paddel misses the ball
    if ball.xcor() > 380 :
        #game_is_on = False
        ball.reset_position()
        score.l_point()

    # detect l_paddel misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    ## Display the wining plear 
    if score.l_score == game_win_score:
        score.game_over("Left Player Wins!")
        game_is_on = False
    elif score.r_score == game_win_score:
        score.game_over("Right Player Wins!")
        game_is_on = False



screen.exitonclick()