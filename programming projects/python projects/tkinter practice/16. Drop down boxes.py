from tkinter import *
root= Tk()
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
#creating drop down boxes
clicked = StringVar()
#default
clicked.set(options[0])

drop =OptionMenu(root, clicked, *options)
drop.pack()
#to access this dropboxes or to something
def show():
    myLabel = Label(root, text=clicked.get()).pack()
myButton = Button(root,text="Enter", command=show).pack()
root.mainloop()