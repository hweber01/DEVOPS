import re
alist=[]
afile = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10A.txt"

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
'''
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
'''
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