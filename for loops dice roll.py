total=0

import random
total=0

# below means "for each number in the range of 2, do this
for count in range(2):
    dice=random.randint(1,6)
    total=dice+total
    print("total=", total, "die roll", dice)

count2=2

while (count2<2):
    count2=count2+1
    dice=random.randint(1,6)
    total=dice+total

    print("total=", total, "dieroll:", dice)

