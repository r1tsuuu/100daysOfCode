from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Fetch data from CSV
try:
    data = pd.read_csv("data/japanese_words.csv")
except FileNotFoundError:
    print("File not found! No data to create flashcards!")

flashcards = data.to_dict(orient="records")

try:
    familiar_words = pd.read_csv("words_learned.csv")
except FileNotFoundError:
    familiar_words = pd.DataFrame(columns=["English", "Japanese"])
    familiar_words.to_csv("words_learned.csv", index=False)

#continue this, use comments to explain your idea so your future self wouldnt be dumbfounded with your ugly code

#BUTTONS FUNCTION
#do this without AI.

#UI SETUP
screen = Tk()
screen.title("Flashy")
screen.config(background=BACKGROUND_COLOR, padx=50,pady=50)

canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
#canvas back image
back_image = PhotoImage(file="images/card_back.png")

#canvas front image
front_image = PhotoImage(file="images/card_front.png")
card_front = canvas.create_image(400,263,image=front_image)

#canvas text
language_text = canvas.create_text(
    400, 150,
    text="Japanese",
    font=("Arial", 40, "italic"), fill="black"
)

question_text = canvas.create_text(
    400, 263,
    text="question",
    font=("Arial", 60, "bold"), fill="black")

canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, borderwidth=0, command=wrong_answer, relief="flat")

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0,  borderwidth=0, command=right_answer, relief="flat")

x_button.grid(row=1, column=0)
check_button.grid(row=1, column=1)

print(flashcards)
get_next_card()
screen.mainloop()