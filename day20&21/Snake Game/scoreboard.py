from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.display_score()


    def display_score(self):
        self.write(arg=self.score, move=False, align="center", font=("Arial", 16, "normal"))

    def add(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))
        self.goto(0, 270)