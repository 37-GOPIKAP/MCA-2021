import operator
d={"pen":8,"pencil":5,"eraser":6,"book":45,"bag":1050,"pouch":30}
acs=sorted(d.items(),key=operator.itemgetter(1))
print("ascending order",acs)
sort_dict=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("descending order",sort_dict)
