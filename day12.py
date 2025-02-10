import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

def play():
    number_to_guess = random.randint(0, 100)
    if difficulty == 'easy':
        guesses = 10

    else:
        guesses = 5

    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))

        except TypeError:
            print("Please guess an integer!")
            guess = int(input("Make a guess: "))
        
        #checks
        if guess == number_to_guess:
            print("You win!")
            return
        elif guess - number_to_guess >= 10:
            print("Too high!")
        elif guess - number_to_guess <= -10:
            print("Too low!")
        elif guess - number_to_guess > 0:
            print("A little high!")
        elif guess - number_to_guess < 0:
            print("A little low!")

        guesses -= 1

        if guesses > 0:
            print("Guess again.")

        else:
            print("You lose!")
            return

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty not in ['easy', 'hard']:
    print("Choose a valid difficulty!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

play()