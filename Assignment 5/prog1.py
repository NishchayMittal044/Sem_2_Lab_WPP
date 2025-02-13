#MAXIMIZING XOR
L = int(input("Enter L :"))
R = int(input("Enter R :"))

max = 0

for i in range (L,R+1):
    for j in range(L,R+1):
        if(i^j>max):
            max = i^j

print("The maximum XOR is :",max)

