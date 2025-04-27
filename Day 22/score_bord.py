from turtle import Turtle

FONT = ("Courier", 40 , "normal")

class Score(Turtle):
    def __init__(self , game_win_score):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.game_win_score = game_win_score
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score }/{self.game_win_score}" , align="center" , font=FONT)
        self.goto(100, 250)
        self.write(f"{self.r_score}/{self.game_win_score}" , align="center" , font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self, winner_text):
        self.goto(0, 0)
        self.write(winner_text, align="center", font=("Courier", 30, "bold"))

