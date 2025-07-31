from tkinter import BooleanVar


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        while self.still_has_questions():
            user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False): ")
            self.check_answer(user_answer)
        else:
            response = input(f"Quiz Over! Final Score: {self.score}\nPlay Again? (Y/N): ")

            if response == "Y":
                self.question_number = 0
                self.score = 0
                self.next_question()

    def check_answer(self, answer):
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        self.question_number += 1
        print(f"Score: {self.score}/{self.question_number}\n")
