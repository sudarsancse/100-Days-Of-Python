#caeser cipher program

""" def great(name):
    print(f"1 {name}")
    print("2")
    print("3")

great("sudarsan") """

##Positional argument
""" def greet_win(name , location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")

greet_win(location ="jateshwer", name="sudarsan" ) """


## final project
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your Message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text , shift):
    alp = text.find(alphabet)
    print(alp)


encrypt(text , shift)