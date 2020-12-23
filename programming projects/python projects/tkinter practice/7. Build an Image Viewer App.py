from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("My simple image viewer")
root.iconbitmap('C:/Users/godwi/Downloads/myicons/Sbstnblnd-Plateau-Apps-image-viewer.ico')

#creating images
my_img1= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/angry_reaction.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/getoutsmarted_reaction.jpg"))
my_img3= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/heart_reaction.jpg"))
my_img4= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/hehe_reaction.jpg"))
my_img5= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/love_reaction.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label= Label(image=my_img1)
my_label.grid(row=2,column=0,columnspan=3)

#functions
def forward(image_number):
    global my_label
    global button_forward
    global button_backward
    #my_label.grid_forget() is an internal function to get rid something
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    # we need to update it so it you can click na button more than once
    button_forward = Button(root, text=">>", command=lambda: forward(image_number +1))
    button_backward = Button(root, text="<<", command=lambda: back(image_number - 1))
    #disabling the button for the last part
    if image_number == 5:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=2, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
def back(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    # we need to update it so it you can click na button more than once
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_backward = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_backward = Button(root,text="<<", state= DISABLED)
    my_label.grid(row=2, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

#creating buttons
button_forward=Button(root, text= '>>',  command=lambda: forward(2))
button_backward=Button(root, text= '<<',  command=back, state= DISABLED)
button_exit=Button(root, text="EXIT PROGRAM", width=20, command=root.quit)

button_backward.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
root.mainloop()