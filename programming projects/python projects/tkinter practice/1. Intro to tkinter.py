from tkinter import *
#meaning of this is from tkinter module import everything
#in kinter everything is a widjets
#button widjets, text widgjets, frame widjgets, everything
#first thing that you will do is root widjet it is like a window or any graphical use of interface program on your computer has like a window

root = Tk()
#to create anything in kinter is really two step process you have to define the thing to create it and you have to put it up to the screen
#first we gonna create label widgjet

#Label widget
myLabel = Label(root, text='Hello World')

#and that's it
#now we have to put our label widget into root widget
#first we have pack, you just packing, and you just shoving in there at the first available spot it will be the size of it is. It is very unsophiscated.
#primaly you can use other methods to put it into screen

#Shoving it into screen
myLabel.pack()

#now we have to create event loop
root.mainloop()
