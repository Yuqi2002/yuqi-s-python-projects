# string notes 2
choice=""

# makes a list of words in a string
words=choice.split()
print(words)
# for each loop that prints each word out individually 
for word in words:
    if(word.lower()=="today"):
        print("I found today") 



# makes it follow the rules of a title
print("Title",choice.title())

# checks to see if it is a title
print("is title",choice.istitle())

# checks to see if it's a digit
print("Digit", choice.isdigit())

# checks to see if it's lower case
print(choice.islower())
# finds the index 
print(choice.find("Den"))

# capitalize only capitalizes the first letter of the input not the first letter of every word
capital=choice.capitalize()
print("capitalization", capital)

# uppercase input
choice=""
while choice!="exit":
    choice=input("what would you want to do?")
    lower=choice.upper()
    print("choice",lower)

# lowercases input 
choice=""
while choice!="exit":
    choice=input("what would you want to do?")
    lower=choice.lower()
    print("choice",lower)

