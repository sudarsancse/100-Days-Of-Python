from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.goto(0, 265)
        self.score = 0
        self.update_scorebord()
        self.hideturtle()
        

    def update_scorebord(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def incress_score(self):
        self.score +=1
        self.clear()
        self.update_scorebord()