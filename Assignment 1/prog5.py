# You are a student in a class of 10. Your class teacher assigns you a task of entering the
# names of all the students in the class. You finally want to display the names given the
# condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
# names and display them. [Hint: Slicing works when you are selecting maximum characters]
names = []
names2=[]
names3=[]
print("Enter Names")
for i in range (10):
    names.append(input())
print(names)
for i in names:
    names2.append(i[0:15])
    
print(names2)

for t in names2:
    names3.append(t[::-1])
print(names3)
        
