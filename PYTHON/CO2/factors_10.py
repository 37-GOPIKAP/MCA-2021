n=int(input("enter the number:"))
list_1=[]
for i in range(1,n+1):
    if n%i==0:
        list_1.append(i)
print(list_1)
