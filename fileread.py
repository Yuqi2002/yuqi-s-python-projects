# yuqi zhou 
# input and output

filehandle=open("output.txt","r")

text=filehandle.read()

numbers=text.split("\n")

for index in range(len(numbers)):
    numbers(index)=int(numbers(index))

print(numbers)
filehandle.close()