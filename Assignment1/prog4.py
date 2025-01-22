list0=[]
list1=[]
list2=[]
list3=[]
list4=[]
for i in range(1,10001):
    rem=i%5
    if rem==0:
        list0.append(i)
    if rem==1:
        list1.append(i)
    if rem==2:
        list2.append(i)
    if rem==3:
        list3.append(i)
    if rem==4:
        list4.append(i)
ltotal=list0+list1+list2+list3+list4
ltotal.sort()
compare=[]
for i in range(1,10001):
    compare.append(i)
if ltotal==compare:
    print("EQUIVALENCE RELATION IS VALID")
else:
    print("EQUIVALENCE RELATION IS NOT VALID")