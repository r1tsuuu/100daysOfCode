from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.xcor = xcor
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.place_score()


    def place_score(self):
        self.goto(self.xcor, 220)
        self.write(arg=self.score, move=False, align="center", font=("Arial", 32, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.place_score()