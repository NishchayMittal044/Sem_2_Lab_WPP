variable1 = int(input("Enter the first variable"))
variable2 = int(input("Enter the second variable"))
print("The original variables were",variable1,variable2)
variable1 = variable1 + variable2
variable2 = variable1-variable2
variable1 = variable1-variable2
print("The swapped variables are",variable1,variable2)