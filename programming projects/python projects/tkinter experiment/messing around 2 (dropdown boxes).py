from tkinter import *
root= Tk()
options = [
    "400x400",
    "800x800"
]
#creating drop down boxes
clicked = StringVar()
#default
clicked.set(options[0])

drop =OptionMenu(root,clicked, *options)
drop.pack()
#to access this dropboxes or to something
def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()
    get = clicked.get()
    if get =="400x400":
        root.geometry("400x400")
    elif get =="800x800":
        root.geometry("800x800")
myButton = Button(root,text="Enter", command=show).pack()
root.mainloop()