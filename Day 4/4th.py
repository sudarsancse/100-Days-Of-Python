## random number generater
 
import random
"""import day4th_my_module

randomInteget = random.randint(1,10)
print(randomInteget)
print(day4th_my_module.my_favourite_number) """

## random Floting point number
""" random_number_0_to_1 = random.random()
random_number_0_to_10 = random.random() * 10 
## random flot number b/w using uniform
random_number_1_to_10 = random.uniform(1,10)
print(random_number_0_to_1)
print(random_number_0_to_10)
print(random_number_1_to_10) """

## challenge to Hade and Tails prog

""" number = random.randint(1,100)
if(number % 2 == 0):
    print(number)
    print("Head")
else:
    print(number)
    print("Tails") """

## list DataStructer

""" latter = ["a","b","c","d","e","f","g"]
print(latter[0])
print(latter[-1])
# to change the existing list data
latter[0]="."
print(latter[0])
# to add the data in list
latter.append("h")
print(latter)
#to extended tha data from the list
latter.extend([".",">","/"])
print(latter) """

## code challange
#who will pay the bill
""" frind_name=["chandan","soumik","raju","rohit","sundor"]
bill = int(input("What's you bill amount : "))
number = random.randint(0,4)
print(f"{frind_name[number]} Will pay the {bill}")
##--------------OR--------------##
print(random.choice(frind_name)) """

## indexError

""" dirty_dozen = ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "mango", 
    "pineapple", "strawberry", "blueberry", "raspberry", "blackberry", "peach", "pear", 
    "plum", "cherry", "apricot", "date", "fig", "guava", "lemon", "lime", "mango", "papaya", 
    "pomegranate", "avocado", "passion fruit", "tangerine", "nectarine", "cantaloupe", 
    "honeydew", "mulberry", "star fruit", "loquat", "jackfruit", "durian", "lychee", 
    "pomelo", "sapodilla", "rambutan", "longan", "ugli fruit", "breadfruit", "acerola", 
    "black sapote", "cacao", "chayote", "durian", "soursop", "star apple","Carrot", "Potato", "Onion", 
    "Tomato", "Spinach","Cucumber", "Cauliflower", "Cabbage", "Peas", "Green Beans",
    "Eggplant", "Pumpkin", "Bell Pepper", "Radish", "Sweet Potato",
    "Garlic", "Ginger", "Chili", "Broccoli", "Zucchini",
    "Mushroom", "Lettuce", "Asparagus", "Leek", "Corn",
    "Beetroot", "Turnip", "White Radish", "Celeriac", "Rutabaga",
    "Parsnip", "Horseradish", "Artichoke", "Brussels Sprouts", "Kale",
    "Celery", "Spring Onion", "Coriander", "Water Spinach", "Okra",
    "Bottle Gourd", "Bitter Gourd", "Capsicum", "Pointed Gourd", "Hyacinth Beans",
    "Arugula", "Endive", "Collard Greens", "Kohlrabi"]
dirty_dozen_f = ["banana", "orange", "grape", "watermelon", "kiwi", "mango", 
    "pineapple", "strawberry", "blueberry", "raspberry", "blackberry", "peach", "pear", 
    "plum", "cherry", "apricot", "date", "fig", "guava", "lemon", "lime", "mango", "papaya", 
    "pomegranate", "avocado", "passion fruit", "tangerine", "nectarine", "cantaloupe", 
    "honeydew", "mulberry", "star fruit", "loquat", "jackfruit", "durian", "lychee", 
    "pomelo", "sapodilla", "rambutan", "longan", "ugli fruit", "breadfruit", "acerola", 
    "black sapote", "cacao", "chayote", "durian", "soursop", "star apple","Carrot", "Potato", "Onion", 
    "Tomato", "Spinach","Cucumber", "Cauliflower", "Cabbage", "Peas", "Green Beans",
    "Eggplant", "Pumpkin", "Bell Pepper", "Radish", "Sweet Potato",
    "Garlic", "Ginger", "Chili", "Broccoli", "Zucchini",
    "Mushroom", "Lettuce", "Asparagus", "Leek", "Corn",
    "Beetroot", "Turnip", "White Radish", "Celeriac", "Rutabaga",
    "Parsnip", "Horseradish", "Artichoke", "Brussels Sprouts", "Kale",
    "Celery", "Spring Onion", "Coriander", "Water Spinach", "Okra",
    "Bottle Gourd", "Bitter Gourd", "Capsicum", "Pointed Gourd", "Hyacinth Beans",
    "Arugula", "Endive", "Collard Greens", "Kohlrabi"]
dirt=[dirty_dozen,dirty_dozen_f]
print(dirt[1][1]) """

## final project rock paper game

rock = '''
Rock
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
'''
paper= '''
Paper
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''
sciccors= '''
Scissors
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
'''
game=[rock,paper,sciccors]
human = int(input("What do your choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))
computer = random.randint(0,2)
if human ==  computer  :
    print(f"You chose : {human}")
    print(game[human])
    print(f"Computer chose : {computer}")
    print(game[computer])
    print("Match Draw!")
elif human== 1 and computer == 0 or human == 0 and computer == 2 or human == 2 and computer == 1:
    print(f"You chose : {human}")
    print(game[human])
    print(f"Computer chose : {computer}")
    print(game[computer])
    print("You win!")
elif human == 1 and computer == 2 or human == 2 and computer == 0 or human== 0 and computer == 1:
    print(f"You chose : {human}")
    print(game[human])
    print(f"Computer chose : {computer}")
    print(game[computer])
    print("You lose!")
else:
    print("invalid button")