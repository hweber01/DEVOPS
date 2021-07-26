from random import randint
from time import sleep

print("getting numbers \n")
sleep(1)
n1=randint(1,6)
n2=randint(1,6)
print("#1=: " + str(n1) +"\n#2=: " + str(n2))

if (n1==n2):
    print("win!!!!")
else:
    print("beter luck next time")