# lists

newlist=[2,3.4,"stam",[],[88]]
newlist2=newlist + [99,"ehad" ]
print(type(newlist))
print(newlist2)

mystring=''.join(str(newlist2))
print(mystring)

alist=list("1234567")
print(alist)

print(alist [0])
print(alist[0:4])

astring=''.join(alist)
print(astring)

blist=astring.split()
print(blist)

print(len(newlist))
newlist.append("nice")
newlist.append("job")
print(newlist)
print(len(newlist))
cstring=''.join(str(newlist))
print(cstring)

newlist.insert(5,22)
print(newlist)

newlist.pop(5)
print(newlist)

clist=["Hillel","Ayelet","Yael","Yoav","Noa"]
print("Rachel" in clist)