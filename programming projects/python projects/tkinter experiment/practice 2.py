from tkinter import *
root = Tk()

e=Entry(root, width =15, borderwidth=5)
e.grid(row=3, column=1)
e.insert(0, 'NAME')

e2 = Entry(root, width= 15, borderwidth=5)
e2.grid(row=3, column=2)
e2.insert(0, 'NAME')

def clickbutton1():
    thetext = 'THEN YOU ARE THE ' + e.get().upper() + ' PERSON.'
    label = Label(root, text=thetext)
    label.grid(row=2,column=1)

def clickbutton2():
    thetext2 ='THEN YOU ARE THE ' + e2.get().upper() + ' PERSON.'
    label = Label(root, text=thetext2)
    label.grid(row=2, column=2)

button1 = Button(root, text= 'WHO ARE YOU? ', padx= 10, pady= 30, command=clickbutton1)
button1.grid(row=2, column=1)

button2 = Button(root, text='WHO ARE YOU? ', padx= 10, pady= 30, command=clickbutton2)
button2.grid(row=2, column=2)

root.mainloop()