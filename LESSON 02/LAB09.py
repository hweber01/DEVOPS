 #LAB9
### menu
def menu():
    while(True):
        n = int(input("Enter your selection 1-3:\n 1. Dog Details\n 2. Friends list\n 3. N Factorial\n _____ \n"))
        if (n == 1):
            print("DD()")
            continue
        elif (n == 2):
            print("FL()")
        elif (n == 3):
            print("fact(i)")
        else:
            print("wrong - enter a number between 1-3")

###end menu

#MAIN
while(True):
    d = input("do you want to contiue (y/n)")
    if (d == "y"):
        menu()
    elif (d == "n"):
        print("Bye")
    break
