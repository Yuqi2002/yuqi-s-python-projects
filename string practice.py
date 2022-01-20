import random 
firstname=input("what's your first name")
lastname=input("what's your last name")

def NID():
    x=firstname[0]
    y=x+firstname[1]
    z=y.lower()
    num2=[]
    num2.append(z)
    for i in range (6):
        num2.append(random.randint(0,9))
    num3=*num2,sep=""
    print('|    UCF ID:',*num2,sep="")
NID()