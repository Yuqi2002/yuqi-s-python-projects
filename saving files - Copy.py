# yuqi zhou
# input and output

filehandle=open("file1.test","w")

for count in range(0,1000,2):
    filehandle.write(str(count),"\n")

filehandle.close