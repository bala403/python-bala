def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def dev(a,b):
    return a/b
print("enter the choice:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice=int(input("enter the 1/2/3/4:"))
number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))


if(choice==1):
    print(number1,"+",number2,number1+number2)
elif(choice==2):
    print(number1,"-",number2,number1-number2)
elif(choice==3):
    print(number1,"*",number2,number1*number2)
elif(choice==4):
    print(number1,"/",number2,number1/number2)
else:
    print("invalid")
