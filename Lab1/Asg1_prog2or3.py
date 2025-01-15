number = int(input("Enter number of terms in the fibonacci series"))
first_term=0
second_term = 1
sum = 0
i = 3
if number<=0 :
        print("Fibonacci series not possible for negative numbers")
elif number == 1:
        print(0)
elif number == 2:
        print(0,1,sep =", " )
else:
        print(first_term,second_term,sep = ", ",end = ", ")
        while i<=number:
    
                sum = first_term + second_term
                first_term = second_term
                second_term = sum
                print(sum,end = ", ")
                i+=1


        


    

