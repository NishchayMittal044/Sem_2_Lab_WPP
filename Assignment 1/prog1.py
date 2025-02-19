# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.
#CREATING LIST 1
list1 = []
for i in range (0,50,1):
    list1.append(i)
#PRINTING LIST 1
print("\nList 1 is")

print(list1)
#CREATING LIST 2
list2 = []
for i in range (1,51,1):
    list2.append(i*i)
#PRINTING LIST 2
print("\nList 2 is")

print(list2)
#CREATING LIST 3
list3 = []
character = 97
for i in range(1,27):
    elements = (i*chr(character))
    list3.append(elements)
    character += 1
#PRINTING LIST 3
print("\nList 3 is")

print(list3)


