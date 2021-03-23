class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def peri(self):
        return(2*(self.length+self.breadth))
r1=Rectangle(4,5)
r2=Rectangle(9,2)
print("area of first rectangle is",r1.area())
print("area of second rectangle is",r2.peri())
a1=r1.area()
a2=r2.area()
if a1>a2:
    print("area of first rectangle is greatest",a1)
else:
    print("area of second rectangle is greatest",a2)
