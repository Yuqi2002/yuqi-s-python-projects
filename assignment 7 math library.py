# math library
# Yuqi Zhou 
# COP 2500
# 11/1/2021

import math

import turtle

import random

# Starter Code

def randomTurtle():

 for i in range(10):

    choice = random.randint(1,2)

    if (choice==1):

        turtle.forward(random.randint(5, 50))

    elif (choice==2):

        turtle.right(random.randint(1,359))

def testTurtle():
 x1=turtle.xcor()
 y1=turtle.ycor()
 turtle.forward(100)

 turtle.left(90)

 turtle.forward(100)
 x2=turtle.xcor()
 y2=turtle.ycor()
# Call this when turning it in

randomTurtle()

# Call this when testing to make sure you have the correct answer

testTurtle()

print(x1, y1, x2, y2,)
