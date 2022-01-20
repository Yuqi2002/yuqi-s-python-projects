# binary search

import random

hiddennumber=random.randint(1,100)

guess=-1

score=0

maxguesses=6

play= True

wins=0

losses=0

while(play==True):

    while( guess!=hiddennumber and score<maxguesses):
           guess=int(input("what is your guess?\n"))

           if(guess<hiddennumber):
               print("you guessed too low")
               score=score+1

           elif(guess>hiddennumber):
               print("you guessed too high")
               score=score+1

if(score==maxguesses):
    print("you lose you guessed too many times")
    print("the correct answer was", hiddennumber)
    losses=losses+1

else:
    print("you got it correct!")

    print("your score was", score)

    again=input("would you like to play again?\n")
    if(again=="no"):
        play=false


        

    
           
