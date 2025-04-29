# by defult it open the file is read only

# with open("my_fill.txt") as file:
#     contents = file.read()
#     print(contents)
    


## mode="w" for (write the fille)

# with open("my_fill.txt", mode="w") as file:
#     file.write("Chandan sarkar")


## mode ="a" for (add content in the file)
with open("../Desktop/my_fill.txt") as file:
    contents = file.read()
    print(contents)
