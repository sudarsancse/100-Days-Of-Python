# loops
# for loop
""" latters = ["a","b","c","d","e","f","g","h"]
for latter in latters:
    print(latter) """

## find the max number in the list using loops
""" numbers = [1,11,50,2,4,8,892,560,47,93,12,7,5,64,18,27,63,8,4,72,14,53,21,4,42]

max_number = 0
for number in numbers:
    if number >= max_number:
        max_number = number

print(max_number)

print(max(numbers)) """

# using for loop range fun
""" total = 0
for number in range(1,101):
    total +=number

print(total) """

##You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
##1 . Your program should print each number from 1 to 100 in turn and include number 100.
##2 . But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
##3 . When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
##4 . And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

""" for number in range (1 , 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3== 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number) """
    

## Final Project password Generator
import random
latters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","_","+","~","{","}",":"]
password = ""
print ("Wellcome to the Password Generator!")
my_latters = int (input("How many latters would you like in your password? \n"))
my_numbers =int (input("How many number would you like? \n"))
my_symbols =int (input("How many symble would you like? \n"))
""" for char in range (1, my_latters+1):
    random_char = random.choice(latters)
    password += random_char
for num in range (1, my_numbers+1):
    random_num = random.choice(numbers)
    password += random_num
for sym in range (1, my_symbols+1):
    random_sym = random.choice(symbols)
    password += random_sym
    password = ''.join(random.sample(password, len(password)))

print(password) """
