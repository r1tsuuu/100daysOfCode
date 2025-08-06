from turtle import Turtle
from random import choice, uniform

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car = Car()
        car.speed = self.speed
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def increase_car_speed(self):
        self.speed += MOVE_INCREMENT



class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.color(choice(COLORS))
        self.penup()
        self.goto(x=320, y=uniform(-240, 280))
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pencolor("white")

    def move(self):
        self.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT


