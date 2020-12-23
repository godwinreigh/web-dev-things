from tkinter import *
from PIL import ImageTk, Image
root= Tk()
root.title("My first window")
#to add different type of window
#top variable is the second window
#to control when they appear


def open():
    global my_img
    global mylabel
    top = Toplevel()
    #if you want to do inside of second window
    btn2 = Button(top, text="close window", command=top.destroy).pack()
    top.title("My second window")
    lbl = Label(top, text="This is my second window").pack()
    #to make the image appear you need to glogbal it
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/angry_reaction.jpg"))
    mylabel = Label(top, image=my_img).pack()


btn = Button(root, text="Open second window", command=open).pack()

mainloop()