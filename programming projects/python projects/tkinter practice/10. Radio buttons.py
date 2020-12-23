from tkinter import *
root = Tk()

#to keep track things over time
#r=IntVar()
#r.set("2")
#creating radio buttons using list

TOPPINGS = [
    ("Pepperroni","Pepperroni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable = pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#another new function for radio buttons
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#to correct that it do anything
#myLabel = Label(root, text=r.get())
#myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda:clicked(pizza.get()))
myButton.pack()

root.mainloop()