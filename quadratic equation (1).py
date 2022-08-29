import math
a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
c=int(input("enter the num3:"))
d=(b**2)-(4*a*c)
sol1=(-b-math.sqrt(d))/(2*a)
sol2=(-b+math.sqrt(d))/(2*a)
print('solution are',sol1,'and',sol2)
