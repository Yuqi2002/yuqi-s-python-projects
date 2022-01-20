# Yuqi Zhou
# COP 2500
# UCF ID generator
# 11/21/2021
import random 

# ask for input
print("hello, welcome to UCF ID generator!")
title=input("are you a student or faculty?\n")
firstname=input("what is your first name?\n")
lastname=input("what is your last name?\n")
expdate=input("when do you graduate?mm/dd/yyyy\n")

# function that generates a random UCF ID
def UCFID():
    num=[]
    for i in range (7):
        num.append(str(random.randint(0,9)))
    return ''.join(num)

# function that generates a random NID with the first two letters of the user's name in the beginning 
def NID():
    x=firstname[0]
    y=x+firstname[1]
    z=y.lower()
    num2=[]
    num2.append(z)
    for i in range (6):
        num2.append(str(random.randint(0,9)))
    return ''.join(num2)

# formating strings 
firstname1=firstname.strip()
lastname1=lastname.strip()
firstname2=firstname1.title()
lastname2=lastname1.title()
title1=title.strip()
title2=title1.title()
expdate1=expdate.strip()
UCFID1=UCFID()
NID1=NID()

# keeping the card aligned no matter the length of the user input
cardwidth=44
line='| '+title2+':'+firstname2+' '+lastname2
L=len(line)
line2=line+' '*(cardwidth-L-1)+'|'

# print output
print("\nhere is your UCF ID!")
print('┌──────────────────────────────────────────┐')
print(line2)
print('|                                          |')
print(f'|   UCF ID:{UCFID1}                         |')
print(f'|   NID:{NID1}                           |')
print(f'|   EXP:{expdate1}                         |')
print('└──────────────────────────────────────────┘') 


