from tkinter import *
from PIL import ImageTk,Image

root= Tk()
#insterting picture
my_img1= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/angry_reaction.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/getoutsmarted_reaction.jpg"))
my_img3= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/heart_reaction.jpg"))
my_img4= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/hehe_reaction.jpg"))
my_img5= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/love_reaction.jpg"))
#first we have to create a label so we can insert the image
picture_label = Label(image=my_img1)
picture_label.grid(column=2, row=1, columnspan=3)

#defining buttons
def button1func():
    global picture_label
    picture_label.grid_forget()
    picture_label = Label(image=my_img1)
    picture_label.grid(column=2, row=1, columnspan=3)
def button2func():
    global picture_label
    picture_label.grid_forget()
    picture_label = Label(image=my_img2)
    picture_label.grid(column=2, row=1, columnspan=3)
def button3func():
    global picture_label
    picture_label.grid_forget()
    picture_label = Label(image=my_img3)
    picture_label.grid(column=2, row=1, columnspan=3)
def button4func():
    global picture_label
    picture_label.grid_forget()
    picture_label = Label(image=my_img4)
    picture_label.grid(column=2, row=1, columnspan=3)
def button5func():
    global picture_label
    picture_label.grid_forget()
    picture_label = Label(image=my_img5)
    picture_label.grid(column=2, row=1, columnspan=3)

#creating buttons
picturebutton1=Button(root, text="PICTURE 1", command= button1func)
picturebutton2=Button(root, text="PICTURE 2", command= button2func)
picturebutton3=Button(root, text="PICTURE 3", command= button3func)
picturebutton4=Button(root, text="PICTURE 4", command= button4func)
picturebutton5=Button(root, text="PICTURE 5", command= button5func)
#putting it to grids
picturebutton1.grid(column=1, row=0)
picturebutton2.grid(column=2, row=0)
picturebutton3.grid(column=3, row=0)
picturebutton4.grid(column=4, row=0)
picturebutton5.grid(column=5, row=0)






root.mainloop()