from tkinter import *

def btn_clicked():
    data = input.get()
    my_lable["text"] = data

window = Tk()

window.title("Program")
window.minsize(width=500, height=300)
#padding
window.config(padx=20, pady=20)

my_lable = Label(text="I AM A Label", font=("Arial", 24, "bold"))
#postioning
##my_lable.place(x=100, y=0)
my_lable.grid(column=0, row=0) # you cant use pack and grid one program

## entry
input = Entry(width=10)
#postioning
input.grid(column=1, row=1)

#button
button = Button(text="click me" ,command=btn_clicked)
button.grid(column=2, row=0)

button = Button(text=" next click me" ,command=btn_clicked)
button.grid(column=2, row=2)








window.mainloop()