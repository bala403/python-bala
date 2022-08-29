import math as M
num1=float(input("enter the num1:"))
num2=float(input("enter the num2:"))
num3=float(input("enter the num3:"))
if(num1>num2)and(num1<num2):
    greatest=num1
elif(num2>num1)and(num2>num3):
    greatest=num2
else:
    greatest=num3
print("the greatest num is:",greatest)
