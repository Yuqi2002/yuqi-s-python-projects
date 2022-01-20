
IV="none"
while IV !="exit":
    print("menu")
    print("say help to get to our help menu")
    print("say charge on to go to UCF")
    print("say exit to exit")

    IV=input()
    IV=IV.lower

    
    if(IV=="help"):
        print("you asked for help")
    elif(IV=="charge on"):
        print("you are at UCF now")
    elif(IV=="exit"):
        print("you are exiting now")
    else:
        print("i dont understand")


