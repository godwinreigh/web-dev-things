from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#the inside of the frame
frame= LabelFrame(root, text="This is my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)
#you can put anything in frame whatever youw ant
#putting it to screen
b= Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="... or here....")
b.grid(row=0, column=0)
b2.grid(row=1,column=0)

root.mainloop()