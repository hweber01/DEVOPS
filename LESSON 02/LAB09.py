 #LAB9

### dog
def dog():
    dn=input("what is your dogs name?\n")
    da=int(input("what is your dogs age?\n"))
    #dy=da*7
    print("your dog " + dn + " is " + str(int(da)*7) + " dog years old\n**********")
    #continue

### friends
def friends(x):
    flist = []
    for i in range(x):
        nn=input("enter a friends name:\n")
        if(nn in flist):
            print(nn + "is in the list please enter another name!\n")
            nn=()
            nn = input("enter a friends name:\n")
            flist.append(nn)
            print(flist)
        else:
            flist.append(nn)
            print(flist)
### factorial
def fact():
    print("fact()")

### menu
def menu():
    tf = (True)
    while (tf == True):
        n = int(input("Enter your selection 1-4:\n 1. Dog Details\n 2. Friends list\n 3. N Factorial\n 4. QUIT\n _____ \n"))
        if (n == 1):
            dog()
            continue
        elif (n == 2):
            friends(5)
            continue
        elif (n == 3):
            fact()
            continue
        elif (n == 4):
            tf = (False)
        else:
            print("wrong - enter a number between 1-3")
        #continue
###end menu

#MAIN
while(True):
    d = input("do you want to contiue (y/n)\n ")
    if (d == "y"):
        menu()
        continue
    elif (d == "n"):
        print("Bye")
    break
