import random

rock_paper_scissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

try:
    response = int(input("What do you choose type 0 for rock, 1 for paper, and 2 for scissors. \n"))

except:
    print("Invalid Input!")
    response = int(input("What do you choose type 0 for rock, 1 for paper, and 2 for scissors. \n"))

while response not in [0, 1, 2]:
    print("Invalid Input!")
    response = int(input("What do you choose type 0 for rock, 1 for paper, and 2 for scissors. \n"))

print(rock_paper_scissors[response])

print("Computer chose:")

computer_response = random.randint(0, 2)

print(rock_paper_scissors[computer_response])

if response == computer_response:
    print("Draw")

elif response == 0:
    if computer_response == 1:
        print("You lose")

    else:
        print("You win")

elif response == 1:
    if computer_response == 2:
        print("You lose")

    else:
        print("You win")

else:
    if computer_response == 0:
        print("You lose")

    else:
        print("You win")