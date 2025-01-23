# Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

a = input("Enter a string :")
list = []
for i  in range(len(a)):
    if i%2==0:
        list.append(a[i].lower())
    else:
        list.append(a[i].upper())
res = ''.join(list)
print(res)