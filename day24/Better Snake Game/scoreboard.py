from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.display_score()


    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 16, "normal"))

    def add(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))


        self.score = 0
        self.display_score()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))
    #     self.goto(0, 270)