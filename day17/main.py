from data import question_data

from question_model import Question

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)
