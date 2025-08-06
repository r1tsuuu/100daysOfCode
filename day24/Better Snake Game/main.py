import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# Start game
def start_game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.snake_head.distance(food) < 15:
            food.refresh()
            scoreboard.add()
            snake.extend()

        if snake.snake_head.xcor() < -290 or snake.snake_head.xcor() > 290:
            snake.snake_head.goto(-snake.snake_head.xcor(), snake.snake_head.ycor())

        if snake.snake_head.ycor() < -290 or snake.snake_head.ycor() > 290:
            snake.snake_head.goto(snake.snake_head.xcor(), -snake.snake_head.ycor())

        for segment in snake.snake_body[1:]:
            if snake.snake_head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


if __name__ == "__main__":
    start_game()

screen.exitonclick()


