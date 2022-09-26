def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)
s=int(input("Enter n value:"))
print("no of ways",fibonacci(s+1))
