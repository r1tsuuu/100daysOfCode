import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
spawn_chance = 0

screen.listen()

screen.onkey(player.up, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    collide_counter = 0

    for car in car_manager.cars:
        if player.distance(car) < 30 and player.xcor() + 10 >= car.xcor() - 10:
            scoreboard.game_over()
            player.reset()


    if spawn_chance % 5 == 0:
        car_manager.spawn_car()
    spawn_chance += 1
    car_manager.move_cars()

    if player.ycor() >= player.finish_line:
        player.reset()
        scoreboard.increase_level()
        for car in car_manager.cars:
            car.increase_speed()
        car_manager.increase_car_speed()

