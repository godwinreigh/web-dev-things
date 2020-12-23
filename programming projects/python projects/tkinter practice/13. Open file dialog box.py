#open files in computer using tkinter
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
root = Tk()

#root.filename = filedialog.askopenfilename(initialdir="C:/Users/godwi/Desktop/collected pictures from fb", title='Select a file', filetypes=(("png files","*.png"),("all files","*.*")) )
##default image directory = "/gui/images"
##how to return something in root.file
#my_label = Label(root, text=root.filename).pack()
#my_image = ImageTk.PhotoImage(Image.open(root.filename))
#my_image_label = Label(image=my_image).pack()



def open():
    top = Toplevel()
    global my_image
    top.filename = filedialog.askopenfilename(initialdir="C:/Users/godwi/Desktop/collected pictures from fb",
                                               title='Select a file',
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    #file types can be jpg files, png files etc...
    my_label = Label(top, text=top.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(top.filename))
    my_image_label = Label(image=my_image).pack()
my_btn =Button(root,text="Open file", command=open).pack()
root.mainloop()
