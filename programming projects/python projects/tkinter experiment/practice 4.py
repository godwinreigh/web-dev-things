#simple analyzer in tkinter
from tkinter import *
root = Tk()
root.geometry("300x400")
e = Entry(root, width=50)
e.grid(row=0,column=0, columnspan=1)
def click():
    main = e.get()
    if main == "asd":
        Label(root, text="Welcome").grid(row=2,column=0)
    else:
        return
btn = Button(root, text="enter", command=click).grid(row=1,column=0)
root.mainloop()