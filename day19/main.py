from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

colors = ["red", "green", "blue", "pink", "yellow"]
turtles = []
y_positions = [-100, -50, 0, 50, 100]

# Create turtles and position them
for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    turtles.append(t)

finish_line = 230
winner = None

# Start the race
while not winner:
    for t in turtles:
        t.forward(choice([0, 5, 10, 15, 20, 25]))
        if t.xcor() >= finish_line:
            winner = t.color()[0]
            break  # Stop all turtles once one wins

# Display result
if user_bet and user_bet.lower() == winner:
    print(f"You win! The winner is {winner}.")
else:
    print(f"You lose! The winner is {winner}.")

screen.exitonclick()
