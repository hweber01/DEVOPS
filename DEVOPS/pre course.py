#pre drvops
'''
#Targil #1

budget = int(input("what is your marketing budget: \n"))
fb = int(input("how many days do you want the facebook campagin to run (cost is 100 a day):\n"))
ig = int(input("how many days do you want the instagram campagin to run (cost is 50 a day):\n"))

a=fb*100
b=ig*50
c=(a+b)*1.17
print((a) + (b))

print("your cost for the campaigns is: " + str(c))
if (c<=budget):
    print("Success")
else:
    print("you need to add " + str(c-budget))




# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for i in range(6):
	value = randint(0, 37)
	print(value)

'''

import random
from time import sleep
#game price
p=3
money=int(input("how much money do you want to play:\n"))
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
            print("Your luckey numbers are:\n")
            sleep(1)
            prandomlist = random.sample(range(37), 6)
            prandomlist.sort()
            print(str(prandomlist))
            print("Winning numbers are:\n")
            sleep(1)
            grandomlist = random.sample(range(37), 6)
            grandomlist.sort()
            print(str(grandomlist))
            match = prandomlist + grandomlist
            print(str(match))
            #def Repeat(match):
            size = len(match)
            repeated = []
            for i in range(size):
                k = i + 1
                for j in range(k, size):
                    if match[i] == match[j] and match[i] not in repeated:
                        repeated.append(match[i])
            n = len(repeated)
            if (n==6):
                print("you won 1M")
            elif (n==5):
                print("you won 500")
            elif (n==4):
                print("you won 100")
            elif (n==3):
                print("you won 10")
            else:
                print("you did not win")
        continue
'''        
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
'''