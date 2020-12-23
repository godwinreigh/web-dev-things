from tkinter import *
from tkinter import messagebox
root = Tk()
def popup():
    #messagebox.showinfo is just showing a text from the screen
    #showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    response = messagebox.askquestion("This is my Popup", "Hello world")
    #note
    #function askyesno, askokcancel, results yes=1 no=0
    #function askquestion results yes="yes" no="no"
    #function showerror, showwarning, showinfo returns ok='ok'
    #to do something the yes or no thing

    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!!").pack()

Button(root, text="Popup", command=popup).pack()


mainloop()