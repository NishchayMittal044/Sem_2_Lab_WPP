# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
import random
listrandom = []
for i in range (0,100):
    listrandom.append(random.randrange(0,2))
print(listrandom)
count  = 0
maxcount = 0
for i in range (0,len(listrandom)):
    if listrandom[i] == 0:
        count += 1
        if count >maxcount:
            maxcount  = count
    else:
        count = 0
print("The longest run of zeroes =",maxcount)





