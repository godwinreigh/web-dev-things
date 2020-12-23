from tkinter import *
root=Tk()

#how to make the button to do something
def myClick():
    myLabel = Label(root, text="Look! I clicked the button!!")
    myLabel.pack()

#to disable the button you can add the function state
#to execute the following function we use command= function
myButton = Button(root, text='Click Me!', state= DISABLED)


#we can change the size of the button using the function  padx=
#to change the color of the text we use function fg= and bg= for background color [note] you can use hexcolors
myButton2 = Button(root, text='Click Me!', padx=50, pady=50, command=myClick, fg='blue', bg='black')

myButton.pack()
myButton2.pack()
root.mainloop()

