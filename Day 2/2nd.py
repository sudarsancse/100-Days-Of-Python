""" print(len("1335"))
a = ["appel","appel","appel","appel","appel","appel"]
print(len(a)) """


""" b= type(False)
c= type(1235)
d=type(152.45)
e = type("Sudarsan")
print(b)
print(c)
print(d)
print(e) """


""" print( int("123")+ int("213"))
print(float("11")+ float("11"))
print( str(123)+ str(456))
print( type(bool("True")+ bool("True"))) """


""" print("Number of latters in your name : " + str(len(input("enter your name ")))) """

## round func and bmi calculater
""" height = 1.65 
weight = 84
# Write your code here.
# Calculate the bmi using weight and height.
bmi =weight /  height**2
print(round(bmi))
print(round(bmi, 2)) """


## f-strings
""" score = 0
hightt = 1.8
win = True
print(f"Your score is ={ score} and hight is = {hightt} and you ar wining = {win}") """


## Final projectp
print("Wellcome to the tip calculater")
bill = int(input("what was the total bill ?"))
tip = int(input ("How much tip would you like to give? 10, 12, or 15?"))
person= int(input("How many people to split the bills?"))
print(f"Each person should pay : {round(tip/100 * bill + bill , 2)}")