from tkinter import *
from random import randint
root = Tk()
root.geometry("400x370")
root.title("rock paper scissors")
            #AI
t = ["rock", "paper","scissors"]
computer = t[randint(0,2)]
a = str(computer)
print(a)
            #ENTRY
myentry = Entry(root, width=50)
myentry.grid(column=3, row=2)
mylbl = Label(myentry, text="pick a move")
mylbl.grid(column=3, row=2)
            #CONTROLS
def tie():
    global mylbl
    mylbl.grid_forget()
    mylbl=Label(myentry, text="tie")
    mylbl.grid(row=2,column=2)
def scissors():
    global a
    global mylbl
    enemy = a
    if enemy == "rock":
        mylbl.grid_forget()
        mylbl = Label(myentry, text="you lose")
        mylbl.grid(row=2, column=2)
    elif enemy == "scissors":
        tie()
    elif enemy == "paper":
        mylbl.grid_forget()
        mylbl = Label(myentry, text="you win")
        mylbl.grid(row=2, column=2)
def paper():
    global mylbl
    global a
    enemy = a
    if enemy == "scissors":
        mylbl.grid_forget()
        mylbl = Label(myentry, text="you lose")
        mylbl.grid(row=2, column=2)
    elif enemy == "paper":
        tie()
    elif enemy == "rock":
        mylbl.grid_forget()
        mylbl = Label(myentry, text="you win")
        mylbl.grid(row=2, column=2)
def rock():
    global a
    global mylbl
    enemy = a
    if enemy == "paper":
        mylbl.grid_forget()
        mylbl = Label(myentry, text="you lose")
        mylbl.grid(row=2, column=2)
    elif enemy == "rock":
        tie()
    elif enemy == "scissors":
        mylbl.grid_forget()
        mylbl = Label(myentry, text="you win")
        mylbl.grid(row=2, column=2)
buttonscissors = Button(root,text="Scissors",width=10,pady=50, command=scissors)
buttonpaper = Button(root,text="paper",width=10,pady=50, command=paper)
buttonrock = Button(root,text="rock",width=10,pady=50, command=rock)
buttonpaper.grid(row=1,column=0,)
buttonrock.grid(row=2,column=0,)
buttonscissors.grid(row=3,column=0,)
root.mainloop()