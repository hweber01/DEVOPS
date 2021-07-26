#LAB07

from random import randint
from time import sleep
p=3 #game price
money=int(input("how much money do you want to gamble:\n"))
print("you can play " + str(money//p) + " turns")
prize = 0
for i in range(money//p):
    if money > 0:
        play=input("do you want to play? y/n\n")
        if(play=="n"):
            print("ok, you have $" + str(money) + " sayonnara")
            exit()
        elif play== "y":
            money = money - 3
            print("getting numbers \n")
            sleep(1)
            n1=randint(1,6)
            n2=randint(1,6)
            print("#1=: " + str(n1) +"\n#2=: " + str(n2))
            if(n1==n2):
                if(n1<6):
                    prize=prize+100
                    print("you won $100\nyour total earnings are: $" + str(prize))
                    continue
                else:
                    prize=prize+1000
                    print("you won $1000\nyour total earnings are: $" + str(prize))
                    continue
            elif (n1 == 1):
                prize = prize + 20
                print("you won $20\nyour total earnings are: $" + str(prize))
                continue
            elif (n2 == 2):
                prize = prize + 40
                print("you won $40\nyour total earnings are: $" + str(prize))
                continue
            else:
                print("you did not win this round you have $" + str(money) +" left")
                continue
        elif(play!="y" + play!="n"):
            print("wrong entry")
            continue
    else:
        print("beter luck next time")
print("you are out of turns!\nsee you next time\nbye")