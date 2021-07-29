#LAB10A
import re
alist=[]
afile = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10A.txt"

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(cip):
    if (re.search(regex, cip)):
        isip="y"
        print("Valid Ip address")
    else:
        isip="n"
        print("Invalid Ip address")
def a1():
    file = open(afile,"r")
    mystring = file.read()
    file.close()
    print(mystring)
    mylist = mystring.split(",")
    isip = "n"
    while (isip=="n"):
        cip=input("enter an IP address:\n")
        check(cip)
        if (isip=="y"):
            mylist.append("cip")
            print(mylist)
            break
        else:
            print("enter a valid IP!")
def a2():
    print("a2")
def a3():
    print("a3")
def a4():
    print("a4")
def a5():
    print("a5")

def amenu():
    while(True):
        a_choice=input("Enter a a number between 1-5 to choose from the following options\n1. Search for an IP address from a list\n2. Add an IP address to a list\n3. delete an IP address from a list\n 4. print all IP's to the screen\n5. if you want to quit\nenter your choice: ")
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
    print("Thank you for using our system\nlogging out")