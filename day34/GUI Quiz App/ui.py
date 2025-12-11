from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,text="QUESTION HERE", fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="GUI Quiz App/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_if_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="GUI Quiz App/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_if_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        next_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=next_question)
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text="QUIZ DONE")


    def check_if_true(self):
        if self.quiz.still_has_questions():
            quiz_score = self.quiz.score
            self.quiz.check_answer("True")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.answer_effect(quiz_score, self.quiz.score)
            self.window.after(500, lambda: self.next_question())

    def check_if_false(self):
        if self.quiz.still_has_questions():
            quiz_score = self.quiz.score
            self.quiz.check_answer("False")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.answer_effect(quiz_score, self.quiz.score)
            self.window.after(500, lambda: self.next_question())

    def answer_effect(self, x: int, y: int) -> None:
        if x < y:
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="Red")
        self.window.after(500, lambda: self.canvas.config(background="white"))





