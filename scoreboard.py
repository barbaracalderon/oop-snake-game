from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 13, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.write_scoreboard()
        self.keep_score()

    def write_scoreboard(self):
        self.goto(x=0, y=280)
        self.write(f'Score: {self.score} ', True, align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.clear()
        self.write_scoreboard()
        self.score += 1
