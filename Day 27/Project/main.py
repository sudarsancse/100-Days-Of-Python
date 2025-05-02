from tkinter import*

def button_clicked():
    data= round(float(input.get()) * 1.609344)
    my_label_3["text"] = data

window = Tk()
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)


input = Entry(width=10)
input.grid(column=1, row=0)

my_label_1= Label(text="Miles", font=("Arial" , 10))
my_label_1.grid(column=2, row=0)

my_label_2= Label(text="is equal to", font=("Arial" , 10))
my_label_2.grid(column=0, row=2)

my_label_3= Label(text="0", font=("Arial" , 10))
my_label_3.grid(column=1, row=2)

my_label_4= Label(text="Km", font=("Arial" , 10))
my_label_4.grid(column=2, row=2)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1 , row=3)

window.mainloop()