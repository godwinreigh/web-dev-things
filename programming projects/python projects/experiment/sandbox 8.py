import turtle
turtlev=turtle.Turtle()
def forward():
    turtlev.forward(100)

def left():
    turtlev.left(90)

def right():
    turtlev.right(90)

def down():
    turtlev.back(100)

def triangle():
    turtlev.forward(100)
    turtlev.right(120)
    turtlev.forward(100)
    turtlev.left(120)
    turtlev.forward(100)
    turtlev.right(120)
    turtlev.forward(100)

def square():
    turtlev.forward(100)
    turtlev.left(90)
    turtlev.forward(100)
    turtlev.left(90)
    turtlev.forward(100)
    turtlev.left(90)
    turtlev.forward(100)

def instructions():
    while True:
        a = input(" instructions \n type s to draw square\n type z to draw zigzag\n type f to move forward \n type l to move left\n type r to move right \n type d to move down \n type off to exit\n ").lower()
        if a == 's':
            for i in range(1):
                square()
        elif a == 'z':
            for i in range(1):
                triangle()
        elif a == 'f':
            for i in range(1):
                forward()
        elif a == 'l':
            for i in range(1):
                left()
        elif a == 'r':
            for i in range (1):
                right()
        elif a == 'd':
            for i in range(1):
                down()
        elif a == 'off':
            exit()
        else:
            print("INVALID")
            instructions()

instructions()