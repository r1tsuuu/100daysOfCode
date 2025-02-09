import random

letters = [
    'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
    'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
    'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
    's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
    'y', 'Y', 'z', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
try:
    num_letters = int(input("How many letters would you like?\n"))
    num_numbers = int(input("How many numbers would you like?\n"))
    num_symbols = int(input("How many symbols would you like?\n"))

except ValueError:
    raise ValueError("Invalid Input, please write integers only!")

character_container = []
new_password = []

while num_letters > 0:
    character_container.append(random.choice(letters))
    num_letters -= 1

while num_numbers > 0:
    character_container.append(random.choice(numbers))
    num_numbers -= 1

while num_symbols > 0:
    character_container.append(random.choice(symbols))
    num_symbols -= 1

pass_length = len(character_container)
chosen_characters = []
while pass_length > 0:
    idx = random.randint(0, len(character_container) - 1)

    if idx in chosen_characters:
        continue

    chosen_characters.append(idx)
    new_password.append(character_container[idx])
    pass_length -= 1

print(character_container)
print(f"Your new password: {''.join(new_password)}")