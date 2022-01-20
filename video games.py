# Yuqi Zhou
# COP 2500
# video games
# 9/27/2021

# set gamesplayed to 0 and groups to 1 so it can print out group 1 at first
gamesplayed=0
groups=1

import random

# while statement to loop the program when there's less than 20 games
while gamesplayed<20:
    print("visiting group#",groups,sep="")
    groupmembers=random.randint(1,6)
    # if there is less than 4 group members, the if statement will run
    if groupmembers<5 and gamesplayed<20:
        print("played game")
        gamesplayed=gamesplayed+1
        # random integer between 1 and 2 to give a 50% chance of playing again
        rematch=random.randint(1,2)
        while rematch==1 and gamesplayed<20:
            print("played game")
            gamesplayed=gamesplayed+1
            rematch=random.randint(1,2)
            # if statement for the program to find a new group 
            if rematch==2 and gamesplayed<20:
                groups=groups+1
                print("visiting group#",groups,sep="")
    groups=groups+1
