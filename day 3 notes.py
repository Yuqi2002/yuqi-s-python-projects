# Yuqi Zhou
# COP 2500
# 8/31/2021
# day 3 notes

money= int(input("how much money do you have?"))

# integer division- always rounds down=//
tickets=money//10

print("the number of tickts you can buy are", tickets)

# modulus-finds the remainder of a division problem
leftover=money % 10

print("you have", leftover, "dollars left over")


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

# number rounding
number=12.332574398
print("the value", "%.2f"%number)
