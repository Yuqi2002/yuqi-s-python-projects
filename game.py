# Yuqi Zhou
# COP 2500
# 9/12/2021
# Knightro's game

# get user input
print("Welcome to Knightro's new game!")
guess=input("guess whether knightro picked odd or even to win the Sword.\n")

import random

hiddennumber=random.randint(1,2)

# this part below gave me the most trouble having me stuck for hours
# I ended up realizing that I needed to put quotation marks on the word
# even and odd to make the program run correctly
if(hiddennumber==1):
    hiddennumber="odd"
if(hiddennumber==2):
    hiddennumber="even"

if(hiddennumber==guess):
    print("horray! you've won the golden sword!")
if(hiddennumber!=guess):
    print("sorry, that was not Knightro's pick, better luck next time")
    




    
