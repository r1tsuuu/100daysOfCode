import random

word_list = ["skibidi", "sigma", "rizz", "mog", "ohio", "gyatt"]

STATES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def play():
    word = list(random.choice(word_list))
    word_state = []
    LIVES = 6
    current_lives = LIVES

    for char in range(len(word)):
        word_state.append('_')

    print(f"word: {''.join(word_state)}")

    while '_' in word_state and current_lives > 0:
        print(f"Lives left: {current_lives - 1}")
        guess = input("Guess a letter ").lower()

        while not guess.isalpha() or not isinstance(guess, str):
            print("Please guess a letter! ")
            guess = input("Guess a letter ").lower()
        

        if guess in word:
            for char in range(len(word)):
                if guess == word[char]:
                    word_state[char] = guess
            print("Good Job!")

        else:
            current_lives -= 1
            print("Wrong Guess!")

        print(f"word: {''.join(word_state)}")
        print(STATES[LIVES - current_lives - 1])

    if current_lives != 0:
        print("Congrats you win!")
        print(f"The word was: {''.join(word)}")

    else:
        print("Nice try!")
        print(f"The word was: {''.join(word)}")

print("Welcome to HANGMAN!")
print(STATES[0])
response = input("Do you want to play? Y/N ").lower()

while response not in ['y', 'n']:
    print("Invalid Input!")
    response = input("Do you want to play? Y/N ").lower()

if response == 'y':
    play()

