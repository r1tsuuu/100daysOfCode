from turtle import Turtle

class StateText(Turtle):
    def __init__(self, state_name: str, x_cor: int, y_cor: int):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(arg=state_name, move=False, align="center")
