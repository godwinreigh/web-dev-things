from tkinter import *
root = Tk()
#how big to window will be
root.geometry("400x400")
#creating slider widjet
#where to start where to end
def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=400)
vertical.pack()
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()
#how to use the return number to sliders
my_label = Label(root, text=horizontal.get()).pack()
my_btn = Button(root, text="Click Me", command=slide).pack()
root.mainloop()