#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()
#Replace the [name] placeholder with the actual name.
with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

#Save the letters in the folder "ReadyToSend".
for name in invited_names:
    name = name.strip("\n") #removes the \n for each name
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as letter_to_send:
        new_letter = letter_content.replace("[name]", name) #this changes the name in the letter
        letter_to_send.write(new_letter)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp