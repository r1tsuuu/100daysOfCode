from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS, is_timer_running, my_timer
    REPS = 1
    is_timer_running = False
    canvas.itemconfig(timer_text, text="00:00")
    progress_label.config(text='')
    main_label.config(text="Timer", foreground=GREEN)
    window.after_cancel(my_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
is_timer_running = False
def start_timer():
    global REPS
    session_time = 0

    if REPS % 2 == 1:
        session_time = WORK_MIN
        main_label.config(text="Work", foreground=GREEN)
    elif REPS % 8 == 0:
        session_time = LONG_BREAK_MIN
        main_label.config(text="Long Break", foreground=RED)
    elif REPS % 2 == 0:
        session_time = SHORT_BREAK_MIN
        main_label.config(text="Short Break", foreground=PINK)

    if not is_timer_running:
        start_countdown(session_time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_countdown(count):
    global is_timer_running, REPS, my_timer
    is_timer_running = True
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        my_timer = window.after(1000, start_countdown, count - 1)
    else:
        is_timer_running = False
        progress_label.config(text='✓' * (REPS // 2))
        REPS += 1
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

main_label = Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, "normal"))
main_label.grid(column=1, row=0)

progress_label = Label(background=YELLOW, foreground=GREEN)
progress_label.grid(row=3, column=1)


start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset",command = reset_timer, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)


window.mainloop()