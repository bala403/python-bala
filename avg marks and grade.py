import math as M
tamil=float(input("enter the mark:"))
cse=float(input("enter the mark:"))
python=float(input("enter the mark:"))
eng=float(input("enter the mark:"))
sum=tamil+cse+python+eng
avg=sum/4
print("sum",sum)
print("average",avg)
if(avg>=90):
    print("grade S")
elif(avg>=80):
    print("grade A")
elif(avg>=70):
    print("grade B")
elif(avg>=60):
    print("grade C")
else:
    print("FAIL")
    

