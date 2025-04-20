##debuging code
# def my_function():
#     for i in range(1,21):
#         print(i)
#         if i == 20:
#             print("you got it")

# my_function()

## 2nd code

# from random import randint
# dice_images =["❶", "❷", "❸", "❹", "❺", "❻"]
# dic_num = randint(0, 5)
# print(dic_num)
# print(dice_images[dic_num])

## 3rd code

# year = int(input("What's your year of birth? "))

# if year > 1980 and year <= 1994:
#     print("Your are a millenial.")
# elif year > 1994 :
#     print("You are a Gen z.")

## 4th code
'''Qustion
    age = int(input("How old are you? "))
if age > 18:
    print("You can drive at age {age}")


find the all posible bug and solve it
'''

# try:
#     """ try : when user give input as a string not in numberical (like 10 such as ten) that time ValueError came in console"""

#     age = int(input("How old are you? "))
# except ValueError:
#     """except : if the except condition is true that time it run the below code (like except ValueError: ) it only work when this error came """

#     print("You have typed in an ivalid number. Please tryagain with a numerical response such and 10")
#     age = int(input("How old are you? "))

# if age > 18:
#     print(f"You can drive at age {age}")
# else:
#     print(f"You can't drive at age {age} ")


## 5th code

"""
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of word per pages: "))
total_word = pages * word_per_page
print(total_word)

find the bug
"""

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of word per pages: "))
total_word = pages * word_per_page
print(total_word)


