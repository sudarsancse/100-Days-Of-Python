# def format_name(fname, lname):
#     Fname = fname.capitalize()
#     Lname = lname.capitalize()
#     print(f"{Fname} {Lname}")

# format_name("sUDARSAN" , "sARKAR")
###

# def format_name(fname, lname):
#     if fname == "" or lname == "":
#         return "You did not provide valide input"
#     Fname = fname.capitalize()
#     Lname = lname.capitalize()
#     return f"resule : {Fname} {Lname}"


# print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Docstrings

# def format_name(fname, lname):
#     """this is Docstring ,
#     it take the fname and lname and formated in to frist latter each word to capital later"""
#     if fname == "" or lname == "":
#         return "You did not provide valide input"
#     Fname = fname.capitalize()
#     Lname = lname.capitalize()
#     return f"result : {Fname} {Lname}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))


## final claculater project


import art
def add(n1, n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1-n2

def multiply(n1 , n2):
    return n1*n2

def divide(n1 , n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def claculator():
    print(art.logo)
    num1 = float (input("What is your first number?: "))
    should_accmulate = True

    while should_accmulate:
        for  operater in operations:
            print(operater)
        operator_symbol = input("Pick an operater? ")
        num2 = float (input("What is your next number?: "))

        result = operations[operator_symbol](num1,num2)
        print(f"{num1} {operator_symbol} {num2} = {result} ")

        choice = input(f"Type 'y' to continue calculating whith {result}, or Type 'n' to start a new calculation: ").lower()

        if choice == "y" :
            num1 = result
        else:
            should_accmulate = False
            print("\n"*30)
            claculator()
    

claculator()

