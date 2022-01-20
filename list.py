shopping= ["subs", "cookings","oreos","popcorn","salsa","chips","milk"]

item=input("what food are you searching for?")
if item in shopping:
    print("found", item)

print(shopping)

if("watermelon" in shopping):
    shopping.remove("watermelon")

while("subs" in shopping):
    shopping.remove("subs")

#removes the first item in the list because programming starts counting at 0
shopping.pop(0)
print(shopping)

#adds an item to the end of the list
shopping.append("soda")
print(shopping)

import random 

choice=random.randint(0,len(shopping)-1)

print(shopping(choice))