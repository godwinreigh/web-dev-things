from tkinter import *
#for making images
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to Code at Codemy.com')
#making icons
root.iconbitmap('C:/Users/godwi/Downloads/myicons/Treetog-I-Documents.ico')

#exit button
button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.pack()


#making images
my_img= ImageTk.PhotoImage(Image.open("C:/Users/godwi/Desktop/collected pictures from fb/reactions/angry_reaction.jpg"))
my_label= Label(image=my_img)
my_label.pack()

root.mainloop()