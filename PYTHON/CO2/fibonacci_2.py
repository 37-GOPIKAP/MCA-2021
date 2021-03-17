#fibinocci series of n terms
n=int(input("enter the limit:"))
fib1=0
fib2=1
print(fib1)
print(fib2)
for i in range(2,n+1):
    sum=fib1+fib2
    print(sum)
    fib1=fib2
    fib2=sum
