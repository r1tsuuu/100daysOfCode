from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.maxsize(width=250, height=100)
window.config(pady=10, padx=10)

#Entry for miles
entry = Entry(width=7, justify="center")
entry.grid(column=1, row=0)


#Labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

#Button
def action():
    miles = int(entry.get())
    km = round((miles * 1.60934), 2)
    answer_label.config(text=km)

button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)



window.mainloop() #this keeps the screen on