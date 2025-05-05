# Attempt to open the file "a_text.txt"
# If it doesn't exist, create it and attempt to read from it (though this would raise an error since the file is empty)
# try:
#     file = open("a_text.txt")
# except:
#     with open("a_text.txt", "w") as file:
#         file.read()  # This would cause an error since the file is empty

# It's better to handle specific exceptions to control the flow of the program more accurately

try:
    # Try opening the file
    file = open("a_text.txt")

    # A sample dictionary for demonstration
    a_dict = {"key": "value"}

    # Accessing a valid key in the dictionary
    print(a_dict["key"])

    # Performing a simple arithmetic operation
    a = 2 + 2
    print(a)

# Handle the case where the file is not found
except FileNotFoundError:
    # If the file doesn't exist, create it and write some content to it
    file = open("a_text.txt", "w") 
    file.write("kbdgiusf")

# Handle the case where a non-existent key is accessed in the dictionary
except KeyError as error_mess:
    print(f"That key '{error_mess}' doesn't exist")

# This block will run only if no exception occurs in the try block
else:
    # Read and print the file content
    content = file.read()
    print(content)

# This block runs no matter what, even if an exception occurs
finally:
    # Close the file and print a confirmation
    file.close()
    print("File is closed")
