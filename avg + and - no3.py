print("enter -1 to exit*")
b=[]
(c,d,e,f)=(0,0,0,0)
for i in range(0,100):
    a=int(input("enter a element:"))
    if(a==-1):
        break
    else:
        b.append(a)
for i in b:
    if(i<=0):
        c+=i
        d+=1
    else:
        e+=i
        f+=1

print("avg -tive no:",c/d)
print("avg +tive no:",e/f)
