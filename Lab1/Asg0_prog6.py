number = int(input("Enter any number you want to reverse "))
reverse = 0
remainder = 1
print("The original number was",number)
while number != 0:
    remainder = number%10
    reverse = reverse*10 + remainder
    number = number//10
print("The reversed number is",reverse)