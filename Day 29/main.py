from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters)  for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols)  for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers)  for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_click():
    website_name = website_input.get()
    email_id= username_input.get()
    password = password_input.get()

    if len(website_name) == 0 or len(password ) == 0 :
        messagebox.showinfo(title="Error", message=f"Please make sure you haven't left any fields empty.")
    else:
        #messagebox
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email_id}" f"\n Password: {password}\n")

        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{website_name} | {email_id} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

## Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entrys
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "example@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

#buttons
genarate_pass_button =Button(text="Generate Password", command=password_generate)
genarate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_button_click) 
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()