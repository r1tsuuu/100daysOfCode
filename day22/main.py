import time

from turtle import Turtle
from pong import Pong
from turtle import Screen
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

pong1 = Pong(-340)
pong2 = Pong(340)

ball = Ball()

is_game_on = True

screen.listen()
screen.onkey(pong1.up, "w")
screen.onkey(pong1.down, "s")
screen.onkey(pong2.up, "Up")
screen.onkey(pong2.down, "Down")


def draw_line():
    y_cor = -300
    line = Turtle()
    line.ht()
    line.pensize(2)
    line.goto(0, y_cor)
    line.pencolor("white")

    alternate = True
    while line.ycor() < 300:
        line.goto(0, y_cor)

        if alternate:
            line.pendown()
            alternate = False
        else:
            line.penup()
            alternate = True

        y_cor += 10
    line.penup()

def start_game():
    draw_line()
    right_bounce = True
    left_bounce = False

    while is_game_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        #Detech collision with the upper and lower walls
        if ball.ycor() + 20 > 300 or ball.ycor() - 20 < -300:
            ball.bounce_y()

        #Detect collision with left and right walls
        if ball.xcor() + 20 > 400:
            ball.reset()
            pong1.scoreboard.update_score()
            right_bounce = True
            left_bounce = False

        if ball.xcor() - 20 < -400:
            ball.reset()
            pong2.scoreboard.update_score()

            right_bounce = True
            left_bounce = False


        #Detect collision with right paddle
        if ball.distance(pong2) < 50 and 310 < ball.xcor() < 380 and right_bounce:
            ball.bounce_x()
            left_bounce = True
            right_bounce = False

        #Detect collision with left paddle
        if ball.distance(pong1) < 50 and -380 < ball.xcor() < -310 and left_bounce:
            ball.bounce_x()
            left_bounce = False
            right_bounce = True

if __name__ == "__main__":
    start_game()
screen.exitonclick()
