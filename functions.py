# functions

import turtle

# abstractions is making a complex system simpled

def drawtriangle(size):
    for x in range(3):
        turtle.forward(size)
        turtle.left(120)

def drawbox(stemlength):
    for x in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(stemlength)
        turtle.left(90)

def drawtree(stemlength1,flowers):
    drawbox(stemlength1)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    drawtriangle(size)


drawtree(80)
