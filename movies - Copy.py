# Yuqi Zhou
# COP 2500
# 9/11/2021
# movie going

# get user input
people=int(input("how many people are going?"))


# calculate data
if (people==1):
    totalprice=people*8.50
    # print data
    print("it will cost ","$","%.2f"%totalprice,sep="")

elif(people<20):
    totalprice=people*9.75-1.25
    # print data
    print("it will cost ","$","%.2f"%totalprice,sep="")
           
elif(people>=20 and people<50):
    totalprice=people*7.50
    # print data
    print("it will cost ", "$","%.2f"%totalprice,sep="")
    
else:
    (people>51)
    # print data
    print("that's too many people, please type in a number between 1 and 50")
    
