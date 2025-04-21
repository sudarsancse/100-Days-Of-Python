#higher lower game
import random
from game_data import data
from art import logo, vs

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess , a_follwers, b_follwers):
    if a_follwers > b_follwers:
        if guess == "a":
            return True
        else:
            return False
    elif b_follwers > a_follwers:
        if guess == "b":
            return True
        else:
            return False

print(logo)
score = 0
ashould_continue = True 

while ashould_continue:
    a_account = random.choice(data)
    b_account = random.choice(data)
    if a_account == b_account:
        b_account = random.choice(data)

    a_follwers_count = a_account["follower_count"]
    b_follwers_count = b_account["follower_count"]

    print(f"Compare A : {format_data(a_account)}")
    print(vs)
    print(f"Compare B : {format_data(b_account)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(guess, a_follwers_count , b_follwers_count)
    if is_correct:
        score +=1
        print(f"You are right! Current score {score}")
    else:
        ashould_continue = False
        print(f"You are Worng. Final score {score}")