# control statements
import random

isstudent=input("are you a student?\n")

if (isstudent=="yes" or isstudent=="Yes"):
    print("free or discount")
    chances=random.randint(0,100)
    print(chances)
    if(chances<70):
        print("you go free!")
    else:
        print("you need to pay a discounted ticket price")
else:
    print("you didn't say you were a student")
