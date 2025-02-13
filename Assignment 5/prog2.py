import math

t = int(input("Enter the number of test cases :"))
list =[]
for i in range (t):
    list.append(int(input()))
print(list)
for i in list:
    num = math.floor((i/2)*(i/2))
    print(num)
    
