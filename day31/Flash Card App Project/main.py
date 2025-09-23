from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Fetch data from CSV
try:
    data = pd.read_csv("data/japanese_words.csv")
except FileNotFoundError:
    print("File not found! No data to create flashcards! Please create a 'data.csv' to continue!")
else:
    flashcards = data.to_dict(orient="records")

try:
    familiar_words = pd.read_csv("words_learned.csv")
except FileNotFoundError:
    familiar_words = pd.DataFrame(columns=["English", "Japanese"])
    familiar_words.to_csv("words_learned.csv", index=False)
finally:
    known_words = familiar_words.to_dict(orient="records")

#continue this, use comments to explain your idea so your future self wouldnt be dumbfounded with your ugly code

#BUTTONS FUNCTION
#since flashcards and known words is a LIST of DICTIONARIES, we can create a list a iterate through the elements of flashcards.
unknown_words = [card for card in flashcards if card not in known_words]
current_card = choice(unknown_words) if unknown_words else None

def right_answer():
    reset_timer()
    #if word is not in familiar words, add it
    if not current_card:
        reset_known_words()
        return
    
    if current_card not in known_words:
        known_words.append(current_card)
        pd.DataFrame(known_words).to_csv("words_learned.csv", index=False)
    
    #then, get next card
    get_next_card()

def wrong_answer():
    reset_timer()
    #if word is in familiar words, remove it
    if not current_card:
        reset_known_words()
        return
    
    if current_card in known_words:
        known_words.remove(current_card)
        pd.DataFrame(known_words).to_csv("words_learned.csv", index=False)
    #then, get next card
    get_next_card()

def get_next_card():
    #start_timer
    global current_card
    if not unknown_words:
        reset_known_words()
        return
    current_card = choice(unknown_words)
    canvas.itemconfig(card_front, image=front_image)
    canvas.itemconfig(language_text, text="Japanese", fill="black")
    canvas.itemconfig(question_text, text=current_card["Japanese"], fill="black")
    start_timer()

def flip_card():
    #change canvas image to back image
    canvas.itemconfig(card_front, image=back_image)
    #change language to english
    canvas.itemconfig(language_text, text="English", fill="white")
    #change question to english word
    canvas.itemconfig(question_text, text=current_card["English"], fill="white")

def start_timer():
    #after 3 seconds, flip card
    screen.after(3000, flip_card)

def reset_timer():
    screen.after_cancel(start_timer)

def reset_known_words():
    global known_words, unknown_words
    canvas.itemconfig(language_text, text="No more words!")
    canvas.itemconfig(question_text, text="You have learned all the words.")
    canvas.itemconfig(card_front, image=front_image)
    screen.after(3000, get_next_card) 
    known_words = []
    pd.DataFrame(known_words).to_csv("words_learned.csv", index=False)
    unknown_words = [card for card in flashcards if card not in known_words]
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

get_next_card()
screen.mainloop()