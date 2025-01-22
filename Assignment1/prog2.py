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





