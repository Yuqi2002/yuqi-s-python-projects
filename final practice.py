

def b1speak():
    i=0
    line=input("type a few sentences")
    line2=line.split(".")
    for x in line2:
        i=i+1
        line3=line2[:i]+"roger roger."
    return line3

b1speak()




