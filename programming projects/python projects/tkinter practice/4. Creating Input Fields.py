from tkinter import *
root=Tk()
#creating entry widget for input fields

#we can change the size of it using the width= and function
#we can also change the color using bg and fg
#we can also change the border width using borderwidth= function
e = Entry(root, width=50, bg='Blue', fg='White', borderwidth = 5)
e.pack()
#to make the text always be there
e.insert(0, "Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel= Label(root,text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name!", command =myClick)
myButton.pack()

root.mainloop()