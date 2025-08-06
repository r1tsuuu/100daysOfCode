from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.ht()
        self.write(arg=f"Level: {self.current_level}", move=False, align="left", font=FONT)

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.current_level}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.update_level()

    def game_over(self):
        self.current_level = 1
        self.update_level()
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)
