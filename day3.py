print("                      .\n"
      "                     /|\\\n"
      "                    / |)\\\n"
      "                   /  I( \\\n"
      "    ,._           /   I`) \\\n"
      "  /'\\  `~.       /    | (  \\\n"
      " /  _\\    '.    /     | `)  \\\n"
      "/,-'  \\     `. /      I  )   \\/`-..\n"
      "       \\      /       |  )    \\    `;-,.._\n"
      "        \\    /        I  )     \\           ``-.._\n"
      "         \\  /         I.)'      \\                ``\"..\n"
      "          \\/          |J_,,..__.,\\.,.__..,,._,,,._,,._`;-,..\n"
      "           \\     _,.;'\n"
      "            \\_,-'\")")

print("Welcome to a random place on Earth!")
response = input("You've encountered a giant origami! Quick, what will you do? Fight or Pet? ").lower()

while response not in ["fight", "pet"]:
    print("Invalid Response!")
    response = input("You've encountered a giant origami! Quick, what will you do? Fight or Pet? ").lower()

if response == "fight":
    print("The origami destroyed you. Game over. ")

else:
    response = input("The origami let's you ride on its back! Y/N?").lower()

    while response not in ['y', 'n']:
        print("Invalid Response!")
        response = input("The origami let's you ride on its back! Y/N? ").lower()
    if response == 'y':
        print("You travel around the world! You and the origami become great friends for a long time. Congrats! ")
    elif response == 'n':
        print("The origami was embarrassed and therefore killed you so there is no witness for the minus aura. ")
