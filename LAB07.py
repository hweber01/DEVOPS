#LAB07

from random import randint
from time import sleep
p=3 #game price
money=int(input("how much money do you want to gamble:\n"))
if money > 0:
    play=input("do you want to play? y/n\n")
    if(play=="n"):
        print("ok, you have $" + str(money) + "sayonnara")
        exit()
    elif(play!="y" + play!="n"):
        print("wrong entry")
    elif play== "y":
        money = money - 3
        print("getting numbers \n")
        sleep(1)
        n1=randint(1,6)
        n2=randint(1,6)
        print("#1=: " + str(n1) +"\n#2=: " + str(n2))
        if ((n1<6)==(n2<6)):
            money=money+100
            print("you won $100")
        elif((n1==6)==(n2==6)):
            money=money+1000
            print("you won $1000")
        elif (n1 == 1):
            money = money + 20
            print("you won $20")
        else:
            print("you did not win this round you have $" + str(money) +" left")
else:
    print("beter luck next time")