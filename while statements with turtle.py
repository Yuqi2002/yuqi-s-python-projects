# Yuqi Zhou
# COP 2500
# 9/19/2021
# icons 

# first loop, make black rectangles
import turtle
number=6
while(number>0):
    number=number-1
    turtle.speed(1000)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.left(90)

# reposition turtle to set it up for the second loop
import turtle
turtle.penup()
turtle.left(135)
turtle.forward(200)
turtle.right(180)

# second loop make white rectangles 
number=7
import turtle
while(number>0):
    number=number-1
    turtle.pendown()
    turtle.pensize(10)
    turtle.pencolor("white")
    turtle.speed(1000)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.right(90)

# draw a diamond 
import turtle
turtle.penup()
turtle.right(45)
turtle.forward(100)
turtle.pendown()
turtle.pencolor("red")
turtle.pensize(5)
turtle.left(35)
turtle.forward(50)
turtle.right(70)
turtle.forward(50)
turtle.right(110)
turtle.forward(50)
turtle.right(70)
turtle.forward(50)





    
