# Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.
length=float(input("ENTER THE LENGTH IN FEET "))
while(1):
    choice=int(input("ENTER THE CHOICE 1.inches 2.yards 3.miles 4.millimetres 5.centimeters 6.metres 7.kilometres 8.Exit"))
    if choice == 8:
        print("Exiting ...")
        exit(1)
    result=[0,0,0,0,0,0,0]
    result[0]=length*12
    result[1]=length/3
    result[2]=length/5280
    result[3]=length*304.8
    result[4]=length*30.48
    result[5]=length*0.3048
    result[6]=length*0.0003048
    print("THE CONVERTED VALUE IS", {result[choice-1]})
