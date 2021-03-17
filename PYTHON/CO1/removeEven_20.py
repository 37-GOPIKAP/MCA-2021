#remove even numbers from the list
list1=[1,2,88,3,4,98,46,6,72,8,9,10]
print("original list:",list1)
for i in list1[0:12]:
    if i%2==0:
        list1.remove(i)
print("list after removing even numbers:",list1)
  
