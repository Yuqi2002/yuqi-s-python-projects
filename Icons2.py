# Yuqi Zhou
# COP 2500
# 9/19/2021
# icons

# position turtle to bottome left of the screen so it doesn't go out of bounds
import turtle
turtle.penup()
turtle.backward(300)
turtle.right(90)
turtle.forward(300)
turtle.left(90)

# nested for loops, the second for loop below dubplicates a drawing to the right
# and the first for loop below duplicates a drawing upwards
for x in range (3):
    for x in range(3):
        turtle.pendown()
        turtle.pencolor("black")
        turtle.pensize(1)
        # draw rectangles
        for x in range (6):
            turtle.speed(100)
            turtle.forward(75)
            turtle.right(90)
            turtle.forward(10)
            turtle.right(90)
            turtle.forward(75)
            turtle.right(90)
            turtle.forward(10)
            turtle.right(180)
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()
            turtle.left(90)
    


        # reposition turtle
        turtle.penup()
        turtle.left(135)
        turtle.forward(100)
        turtle.right(180)

        # draw white rectangles
        for x in range(7):
            turtle.pendown()
            turtle.pensize(5)
            turtle.pencolor("white")
            turtle.speed(1000)
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(150)
            turtle.left(90)
            turtle.forward(10)
            turtle.right(180)
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()
            turtle.right(90)


        # reposition turtle
        turtle.penup()
        turtle.right(45)
        turtle.forward(50)
        turtle.pendown()

        # draw diamond 
        turtle.pencolor("red")
        turtle.pensize(5)
        turtle.left(35)
        turtle.forward(25)
        turtle.right(70)
        turtle.forward(25)
        turtle.right(110)
        turtle.forward(25)
        turtle.right(70)
        turtle.forward(25)
        turtle.right(55)
        
        # reposition turtle so it duplicates the drawing to the right twice
        turtle.penup()
        turtle.forward(150)
        
    # reposition turtle so it duplicates the 3 drawings upwards twice
    turtle.penup()
    turtle.backward(535)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)

turtle.forward(500)
    








    
