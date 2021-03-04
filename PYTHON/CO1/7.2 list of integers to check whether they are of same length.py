#create list and check whether list are of same length,sum to the same value,common element
list1=[1,8,9,6,4]
list2=[4,5,2,7,3]
len1=len(list1)
len2=len(list2)
print("length of list1 is",len1)
print("length of list2 is",len2)
total1=sum(list1)
print("sum of elements in list1=",total1)
total2=sum(list2)
print("sum of elements in list2=",total2)
if(len1==len2):
    print("two llist are of same length")
else:
    print("two list are of diff length")
if(total1==total2):
    print("true")
else:
    print("false")
for x in list1:
    for y in list2:
        if x==y:
            print("the common element in the list is",x)


