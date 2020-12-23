from turtle import *

setup = (700, 700)

my_turtle =turtle.Turtle()
my_turtle.speed(40)
list= ['violet', 'indigo', 'blue','green','yellow','orange','red' ]

def art(d, angle, x, y):
    for color in list:
        for i in range(30):
            my_turtle.pencolor(color)
            my_turtle.circle(d)
            my_turtle.left(angle)
            d = d+1

art(50,3,0,0)