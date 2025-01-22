length=float(input("ENTER THE LENGTH IN FEET "))
choice=int(input("ENTER THE CHOICE 1.inches 2.yards 3.miles 4.millimetres 5.centimeters 6.metres 7.kilometres"))
result=[0,0,0,0,0,0,0]
result[0]=length*12
result[1]=length/3
result[2]=length/5280
result[3]=length*304.8
result[4]=length*30.48
result[5]=length*0.3048
result[6]=length*0.0003048
print("THE CONVERTED VALUE IS", {result[choice-1]})