# generate a list of integers with over if n>100
n=int(input("enter the limit:"))
list=[]
for i in range(n) :
    num=int(input("enter the number"))
    if num < 100:
        list.append(num)
    else:
        list.append("over")
print(list)
