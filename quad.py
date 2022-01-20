# Yuqi Zhou
# COP 2500
# quad.py
# 10/11/2021

# collect user input for the values Ax**2+BX+C

a=float(input("enter coefficient a: "))
b=float(input("enter coefficient b: "))
c=float(input("enter coefficient c: "))

# solve and define discriminant 
discriminant=b**2-4*a*c

# calculate two roots if discriminant is greater than zero
if discriminant>0:
    numerator1=b*-1+discriminant**.5
    numerator2=b*-1-discriminant**.5
    denominator=2*a
    root1=numerator1/denominator 
    root2=numerator2/denominator 
    print("the two real roots are ",root1," and ",root2)

# print error message if discriminant is less than zero
if discriminant<0:
    print("sorry, the quadratic has complex roots")

# calculate one root if discriminant is equal to zero 
if discriminant==0:
    denominator=2*a
    numerator3=b*-1+discriminant**.5
    root3=numerator3/denominator 
    print("the one real root is ",root3)