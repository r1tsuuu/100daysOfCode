from turtle import Turtle
from scoreboard import Scoreboard

STEP_DISTANCE = 20

class Pong(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.create_pong(x_cor)
        self.scoreboard = Scoreboard(x_cor - 80 if x_cor >= 0 else x_cor + 80)

    def create_pong(self, xcor):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(x=xcor, y=0)
        self.setheading(90)

    def up(self):
        if self.ycor() + 50 + STEP_DISTANCE >= 300:
            return

        self.forward(STEP_DISTANCE)


    def down(self):
        if self.ycor() - 50 - STEP_DISTANCE <= -300:
            return

        self.back(STEP_DISTANCE)

