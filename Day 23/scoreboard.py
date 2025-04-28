from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lavel = 1
        self.hideturtle()
        self.up()
        self.goto(-280, 260)
        self.update_scorebord()
        
    def update_scorebord(self):
        self.clear()
        self.write(f"Lavel:{self.lavel}", align="left" , font= FONT)

    def increase_lavel(self):
        self.lavel +=1
        self.update_scorebord()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center" , font= FONT)

