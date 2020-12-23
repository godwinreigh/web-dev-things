from tkinter import *
root = Tk()
root.geometry("400x400")
#creating checkboxes
var = StringVar()

c=Checkbutton(root, text="Check this box",variable=var,onvalue="On", offvalue="Off")
gettingonvalue = c.__getitem__("onvalue")
gettingoffvalue = c.__getitem__("offvalue")
#deselect function is use to deselect something that is selected by default
c.deselect()
c.pack()
#updating
def show():
    global gettingoffvalue
    global gettingonvalue
    # to do something
    if gettingonvalue =="On":
        root.geometry("200x200")
    elif gettingoffvalue =="Off":
        root.geometry("1000x1000")
    mylabel = Label(root, text=var.get()).pack()
myButton =Button(root, text="Show Selection", command=show)
myButton.pack()
root.mainloop()