#namespachs local vs global scope

'''Global scope'''
# enemies = 1

# def incress_enemies():
#     '''local scope'''
#     enemies = 2
#     print(f"eneimes inside the function {enemies}")

# incress_enemies()
# print(f"eneimes outside the function {enemies}")

##

# count = 1 

# def incress_count():
#     '''you can call global varible in the local scope using Global statment'''
#     global count
#     count +=1
#     print (count)

# incress_count()


## final project
import random
from art import logo
EASY_MODE = 10
HARD_MODE = 5
number =random.randint(1, 100)

print(logo)
print("Welcome to the Number GuessingGame!")
print("I'm thinking of a number between 1 and 100.")


def check_guess(guess , number, turn):
    if guess == number:
        print (f"You Got it! The answer was {guess}")
    elif guess < number:
        print("Too low")
        return turn-1
    else:
        print("Too high")
        return turn-1

def set_difficulty():
    user_choose = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    if user_choose == 'easy':
        return EASY_MODE
    else:
        return HARD_MODE
    

def game():
    turn = set_difficulty()
    guess = 0

    while guess!= number:
        print(f"You have {turn} attempts remaining to guess the number :")
        guess= int(input("Make a guess: "))
        turn = check_guess(guess, number, turn)
        if turn == 0:
            print("You've run out of guesses, you lose")
            return


game()

