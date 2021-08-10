#lab10b

tdict={}
import socket
from time import sleep

def ctdict():
    l = int(input("enter the length of dictionary you want to enter: "))
    for i in range(l):
        sname = input("Enter a website (URL): ")
        ipadd = socket.gethostbyname(sname)
        print(sname + " " + ipadd)
        tdict.update({sname: ipadd})
    print(tdict)


def b1():

    find=input("to check if it is in the dictionary enter a URL: ")
    if (find in tdict):
        print(find + " is in the directory")
    else:
        print(find + " is not in the directory")

def b2():
    adname = input("Enter a website (URL): ")
    adipadd = socket.gethostbyname(adname)
    tdict.update({adname: adipadd})
    print(adname + " " + adipadd + " has been added to the directory")
    print(tdict)

def b3():
    n = len(tdict)
    print(n)
    print(tdict.keys())
    a = input("enter the URL you want to delete from the directory: ")
    tdict.pop(a)
    print("the new directory is: " + str(tdict))
def b4():
    n = len(tdict)
    print(n)
    print(tdict.keys())
    a = input("which URL you want to update the IP address?\n")
    u = input("enter the new IP address:\n")
    tdict.update({a: u})
    print("the new directory is: " + str(tdict))
def b5():
    print("URL and IP for this dictionary are:\n")
    for k, v in tdict.items():
        print(k, v)


def b6():
    print("going back to main menu")
    sleep(2)


def bmenu():
    ctdict()
    while(True):
        b_choice=input("Enter a a number between 1-6 to choose from the following options\n1. Search for a URL from a dictionary\n2. Add a URL + IP address to a dictionary\n3. delete a URL from a dictionary\n4. Update the ip address of a specific URL\n5. print all IP's to the screen\n6. if you want to quit\nenter your choice: ")
        if (b_choice == "1"):
            b1()
        elif(b_choice == "2"):
            b2()
        elif(b_choice == "3"):
            b3()
        elif (b_choice == "4"):
            b4()
        elif (b_choice == "5"):
            b5()
        elif (b_choice == "6"):
            b6()
            break
        else:
            print("invalid choice, please enter a number between 1-5")
            continue