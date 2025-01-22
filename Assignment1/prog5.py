names = []
names2=[]
names3=[]
print("Enter Names")
for i in range (5):
    names.append(input())
print(names)
for i in names:
    names2.append(i[0:15])
    
print(names2)

for t in names2:
    names3.append(t[::-1])
print(names3)
        
