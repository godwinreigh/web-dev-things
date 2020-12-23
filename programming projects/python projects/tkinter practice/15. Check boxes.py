from tkinter import *
root = Tk()
root.geometry("400x400")
#creating checkboxes
var = StringVar()

c=Checkbutton(root, text="Check this box",variable=var, onvalue="On", offvalue="Off")
#deselect function is use to deselect something that is selected by default
c.deselect()
c.pack()

#updating
def show():
    # to do something
    mylabel = Label(root, text=var.get()).pack()
myButton =Button(root, text="Show Selection", command=show)
myButton.pack()
root.mainloop()