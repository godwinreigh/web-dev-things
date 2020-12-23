#grid system is like a grid think of your program as a grid
from tkinter import *
root = Tk()
#creating a label
myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='My name is John Elder')
#shoving it onto the screen
#this were using grid system
myLabel1.grid(row=0, column= 0)
myLabel2.grid(row=1, column= 5)
root.mainloop()