# Yuqi Zhou
# COP 2500
# 9/19/2021
# line plotter

# get user input

time=int(input("when do you get off work?\n"))

delaytime=int(input("how long is each delay?\n"))

delays=int(input("how many delays are there?\n"))

# define delays and total time to set up for loop

delays1=0

totaltime=time+0

# set up while loop that displays output
while delays1<delays:
    print("delay#",delays1, "  Time=", totaltime,sep="")
    delays1=delays1+1
    totaltime=totaltime+delaytime

# I added some extra outputs just for fun
timeafterdelays=totaltime-delaytime
totaldelays=delays1-1
print("after the",totaldelays,"delays, it will be",timeafterdelays)

if(timeafterdelays>1200):
    print("that's too late, the game will be rescheduled")
