""" print ("Wellcome to teh rollercoaster!")
hight = round(float(input("Pleace enter your hight : ")), 2)
if hight >= 5.0  :
    age=int(input("Enter your age : "))
    if(age <=12 ):
        bill = 7
        catagury = "Child"
    elif ( 12 <age <=18):
        bill = 10
        catagury = "Youth"
    elif (age >= 45 and age <= 55):
        bill = 0
        catagury = "Old"
    elif (age > 18):
        bill = 12
        catagury = "Adult"

    pic = str(input("Do you want photo Y/N "))
    if pic in ("Y", "y"):
        bill +=3
    
    print(f"Your final ticket is {catagury} catagury and total bill is {bill}$" )
else:
    print(f"To ride rollercoaster your hight at list {5.0} fite and your hight is {hight} fit") """


## chalange 1
##  cheque the number is EVEN or ODD

""" number = int(input("enter your number "))

if (number %2 == 0) :
    print(f"Your enter number {number} is EVEN ")
else:
    print(f"Your enter number {number} is ODD ") """


## chalange 2
## pizza delivery chalange

""" print ("Wellcome to pizza Deliveries!")
size = str (input("What size Pizza you want? S , M, or L: ") )
pepperoni = str(input ("Do you want pepperoni on your Pizza? Y/N "))
extra_cheeze = str(input("Do you wnat extra Cheeze? Y/N "))

bill = 0
if size in ("S" ,"s"):
    bill += 15
elif size in ("M" ,"m"):
    bill +=20
elif size in ("L" ,"l"):
    bill +=25

if pepperoni in ("Y" , "y"):
    if size in ("s","S"):
        bill +=2
    elif size in ("m","M","L","l"):
        bill +=3

if extra_cheeze in ("Y","y"):
    bill +=1


print(f"Your total bill is : {bill}") """


## Final PRoject 
print(
'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Wellcome to Treasure island.")
print("Your Mission is to find the treasure!")
direction = str (input("You're at a cross road. Where do you want to go \n Type \"left\" or \"right\" "))

if direction in ("LEFT", "left" , "Left"):
    print("you've come to a lake. There is an island in the middle of the lake.")
    Wait_Swim = str(input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across. "))
    if Wait_Swim in ("Wait" , "wait"):
        print("you've come to a house. There is an 3 doors in the house .")
        doors = str(input("Type \"Red\" , \"Blue\" , and \"Yellow\" which door you want to go in "))
        if doors in ("Red" , "red"):
            print("Burned by fire.Game Over.")
        elif doors in ("Blue" , "blue"):
            print("Eaten by beasts.Game Over.")
        elif doors in ("Yellow" , "yellow"):
            print("You found the Treasure. you win the game.")
        else:
            print("You Chose a door that does't exist. Game Over.")
    else :
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")