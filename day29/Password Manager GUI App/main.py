import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    chars = [ ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 ':', ';', '<', '=', '>', '?', '@',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 '[', ']', '^', '_', '`',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 '{', '|', '}', '~']

    length = random.randint(8, 12)
    password = ""

    for character in range(length):
        password += random.choice(chars)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def show_password():
    if checked_state.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas as pd

df = pd.read_csv("credentials_data.csv", sep="|")
df.columns = [col.strip() for col in df.columns]

def save_password():
    global df

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    mask = (df["Website"] == website) & (df["Username/Email"] == email_username)

    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showerror(title="Invalid Inputs", message="Please have an input in all fields.")
        return

    if mask.any():
        df.loc[mask, "Password"] = password

    else:
        new_row = {"Website": website, "Username/Email": email_username, "Password": password}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv("credentials_data.csv", sep="|", index=False)

    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo(title="Password Save Success", message="Credentials Saved!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)

my_pass_img = PhotoImage(file="logo.png", width=200, height=200)

img = canvas.create_image(100, 100, image=my_pass_img, anchor="center")

canvas.grid(row=0, column=1, columnspan=2, sticky="")



#Labels
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(width=36, text="Add", command=save_password)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, columnspan=2, row=4)

#Entries
website_entry = Entry(width=38)
website_entry.focus()
email_username_entry = Entry(width=38)
email_username_entry.insert(0, "biasonneilaldous@gmail.com")
password_entry= Entry(width=21, show="*")
website_entry.grid(column=1, columnspan=2, row=1)
email_username_entry.grid(column=1, columnspan=2, row=2)
password_entry.grid(column=1, row=3)

#checkbox for show password
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
show_password_checkbox = Checkbutton(text="show", variable=checked_state, command=show_password)
show_password_checkbox.grid(column=3, row=3)

window.mainloop()