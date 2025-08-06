from turtle import Turtle
from random import uniform, choice, randint
from types import new_class


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.direction = 0
        self.shape("circle")
        self.penup()
        self.color("red")
        self.setheading(randint(0, 70))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move
        if self.move_speed - 0.05 > 0:
            self.move_speed -= 0.05

    def reset(self):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1