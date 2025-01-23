# Find Digits
# You are given a number N, you need to print the number of positions where digits exactly
# divides N.
# Input format
# The first line contains T (number of test cases followed by T lines each containing N).
# Constraints
# 1 <= T <= 15
# 0 <= N <= 1010
# Output Format
# For each test case print the number of positions in N where digits in that number exactly
# divides the number N in separate line.
# Input
# 2
# 12
# 13
# Output
# 2
# 1

test = int(input("Enter the number of test cases :"))
number = []
for i in range (test):
    number.append(int(input("Enter the number :")))

for i in range (test):
    count = 0
    original = number[i]
    while number[i]!=0:
        
        rem = number[i]%10
    
        if(original%rem == 0 and rem!=0):
            count +=1
        number[i] = number[i]//10
    print(count)
    


