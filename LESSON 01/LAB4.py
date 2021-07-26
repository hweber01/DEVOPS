alist = ["Hillel weber", 57, "hillel.weber@gmail.com", 9498649657]
print("My name is: " + alist[0] + "\nMy age is: " + str(alist[1]) + "\nMy email is: " + alist[
    2] + "\nMy phone number is: " + str(alist[3]))


#blist = ["192.168.0.1",str(a)," 192.168.0.1",str(a + 1)]
blist=["192.168.0.1"," 192.168.0.1"]
print(blist)



blist.append("192.168.0.3")
blist.append("192.168.0.4")
blist.append("192.168.0.5")

print(blist)
bstring=' '.join(blist)
print(bstring)

blist.pop(2)
cstring=' '.join(blist)
print(cstring)

print("list length:" + str(len(blist)))
