#LAB10A
import re
from time import sleep
alist=[]
afile = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10A.txt"

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
file = open(afile, "r")
mystring = file.read()
#print(mystring)
alist = mystring.split(",")

def a1():
    while (True):
        cip = input("enter an IP address:\n")
        if (re.search(regex, cip)):
            print("Valid Ip address")
            if (cip in alist):
                print(cip + " is in the list")
            else:
                print(cip + " is not in the list")
            break
        else:
            print(cip + " - Invalid Ip address")
        continue
def a2():
    while (True):
        cip = input("enter an IP address:\n")
        if (re.search(regex, cip)):
            print("Valid Ip address")
            alist.append(cip)
            print(alist)
            break
        else:
            print(cip + " - Invalid Ip address")
        continue
def a3():
    l=len(alist)
    while (True):
        d=int(input("enter a number between 1 to " + str(l-1) + " to delete an IP address from the list: " ))
        if (d>l):
            print("number exceeds the length of the list\nplease enter a number between 1 - " + str(l-1) +": ")
            continue
        else:
            alist.pop(d)
            print(alist)
            break
def a4():
    for line in file:
        print(line)
        alist.append(line)
    file.close()
    print(alist)

def a5():
    print("going back to main menu")
    sleep(2)

def amenu():
    while(True):
        a_choice=input("Enter a a number between 1-5 to choose from the following options\n1. Search for an IP address from a list\n2. Add an IP address to a list\n3. delete an IP address from a list\n4. print all IP's to the screen\n5. if you want to quit\nenter your choice: ")
        if (a_choice == "1"):
            a1()
        elif(a_choice == "2"):
            a2()
        elif(a_choice == "3"):
            a3()
        elif (a_choice == "4"):
            a4()
        elif (a_choice == "5"):
            a5()
            break
        else:
            print("invalid choice, please enter a number between 1-5")
            continue