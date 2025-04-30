#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[names]"


with open("./input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/Letters/starting_letter.txt") as latter_file:
    latter_contatint = latter_file.read()
    for name in names:
        striped_name = name.strip()
        new_latter = latter_contatint.replace(PLACEHOLDER , striped_name)
        with open("./Output/ReadyToSend/latter_for_{striped_name}.docx" , mode="w") as competed_file:
            competed_file.write(new_latter)