n=int(input("enter the value:"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(temp==sum):
    print("the num is palindrome")
else:
    print("the num is not palindrome")
