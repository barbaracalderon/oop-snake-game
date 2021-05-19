from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 13, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=280)
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0                      # reset to zero so it counts again next round

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write('GAME OVER', True, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} ', True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.update_scoreboard()
        self.score += 1
