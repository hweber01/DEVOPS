'''
import re
alist=[]
afile = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10A.txt"

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

isip="z"
def check(cip):
    if (re.search(regex, cip)):
        isip = "a"
        isip="y"
        print("Valid Ip address")
        print(isip)
        return isip
    else:
        isip="n"
        print("Invalid Ip address")
        print(isip)
        return isip

file = open(afile,"r")
mystring = file.read()
print(mystring)
alist = mystring.split(",")
while (True):
    cip = input("enter an IP address:\n")
    if (re.search(regex, cip)):
        print("Valid Ip address")
        if(cip in alist):
            print(cip + " is in the list")
        else:
            print(cip + " is not in the list")
        break
    else:
        print(cip + " - Invalid Ip address")
    continue
    #print(alist)
    #n = [line.rstrip() for line in file]
    #print(n)
    #print(file.readlines()[1:(n)])
    #file.close()

import socket

sname = input("Enter a website (URL): ")
ipadd = socket.gethostbyname(sname)
print(sname + " " + ipadd)


import socket
#bfile = open("C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10C.txt", "w")
file = open("C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10C.txt", "r+")
tdict={}

lst = file.read()
print(lst)
n = len(lst)
res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
print(res_dct)
print(res_dct.keys())
a = input("enter the URL you want to delete from the directory: ")
res_dct.pop(a)
print("the new directory is: " + str(res_dct))

l = int(input("enter the length of dictionary you want to enter: "))
for i in range(l):
    sname = input("Enter a website (URL): ")
    ipadd = socket.gethostbyname(sname)
    print(sname + " " + ipadd)
    tdict.update({sname: ipadd})
    print(tdict)

file.write(str(tdict))
print(file.read())
file.close()



file = open("C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10C.txt", "r")
#print(file.readlines()[0:3])
#file.close()

mystring=file.read()
file.close()
print(mystring)
mylist=mystring.split(",")
print(type(mylist))
print(mylist)
'''

a_dictionary = {}
a_file = open("C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10C.txt")
for line in a_file:
    key, value = line.split()
    a_dictionary[int(key)] = value

print(a_dictionary)
