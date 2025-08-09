import pandas
import turtle
from turtle import Screen
from state_text import StateText

screen = Screen()
screen.setup(width=725, height=491)
screen.title("US States Game")


image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#data from csv using pandas
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()

correct_guess = 0
state_count = len(states_list)
answer_state = screen.textinput(title="Guess a state", prompt="Write down a name of a state")
states_guessed = []

while correct_guess < 50:
    guess_state = answer_state.title()
    if guess_state in states_list:
        correct_guess += 1
        correct_state = StateText(guess_state, int(states_data[states_data["state"] == guess_state].x), int(states_data[states_data["state"] == guess_state].y))
        if guess_state not in states_guessed:
            states_guessed.append(guess_state)
        else:
            print(f"Already guessed {guess_state}!")

    elif guess_state == "Exit":
        states_to_learn = states_data[~states_data["state"].isin(states_guessed)]["state"]
        states_to_learn.to_csv("states_to_learn.csv")
        break

    answer_state = screen.textinput(title=f"{correct_guess}/{state_count} States Correct",
                                    prompt="Write down a name of a state")

screen.exitonclick()