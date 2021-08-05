#lab10b

bfile = open("C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/LAB10B.txt", "w")

file = open(bfile, "r")
def b1():
    print("b1")
def b2():
    print("b2")
def b3():
    print("b3")
def b4():
    print("b4")
def b5():
    print("b5")
def b6():
    print("b6")


def bmenu():
    l = int(input(print("enter the length of dictionary you want to enter: ")))
    while(True):
        a_choice=input("Enter a a number between 1-6 to choose from the following options\n1. Search for a URL from a dictionary\n2. Add a URL + IP address to a dictionary\n3. delete a URL from a dictionary\n4. Update the ip address of a specific URL\n5. print all IP's to the screen\n6. if you want to quit\nenter your choice: ")
        if (a_choice == "1"):
            b1()
        elif(a_choice == "2"):
            b2()
        elif(a_choice == "3"):
            b3()
        elif (a_choice == "4"):
            b4()
        elif (a_choice == "5"):
            b5()
        elif (a_choice == "6"):
            b6()
            break
        else:
            print("invalid choice, please enter a number between 1-5")
            continue