import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

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
# ---------------------------- SEARCH WEBSITE CREDENTIALS ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left the website field empty.")
        return
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Matching Credentials Found", message="No Credentials for this Website has been found!")
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="No Matching Credentials Found", message="No Credentials for this Website has been found!")
        else:
            messagebox.showinfo(title="Website Credentials",
                            message=f"E-mail: {email} \nPassword: {password}")
    finally:
        website_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            new_data = {
                website: {
                    "email": email_username,
                    "password": password,
                }
            }
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

                messagebox.showinfo(title="Success", message="Details saved successfully!")

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
generate_password_button = Button(width=14,text="Generate Password", command=generate_password)
add_button = Button(width=36, text="Add", command=save_password)
search_button = Button(width=14,text="Search", command=search)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, columnspan=2, row=4)
search_button.grid(column=2, row=1)

#Entries
website_entry = Entry(width=21)
website_entry.focus()
email_username_entry = Entry(width=38)
email_username_entry.insert(0, "biasonneilaldous@gmail.com")
password_entry= Entry(width=21, show="*")
website_entry.grid(column=1, row=1)
email_username_entry.grid(column=1, columnspan=2, row=2)
password_entry.grid(column=1, row=3)

#checkbox for show password
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
show_password_checkbox = Checkbutton(text="show", variable=checked_state, command=show_password)
show_password_checkbox.grid(column=3, row=3)

window.mainloop()