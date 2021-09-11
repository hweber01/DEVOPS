#LAB 01

#PART 1

#PART 2
'''
from time import sleep
for i in range(5):
    sleep(1)
    print(str(i) + " have past")

#PART 3

from random import randint
from time import sleep

print("getting numbers \n")
sleep(1)
n1 = randint(1, 6)
n2 = randint(1, 6)
print("#1=: " + str(n1) + "\n#2=: " + str(n2))
if (n1 == n2):
    print("Equal")
else:
   print("Mot equal")
'''
#PART 4
import os
import tarfile
#1/bin/python

import os
import tarfile
#import os.path

fname= "lab01-4.tar"
for i in range(10):
        tname = (str(i+1) + ".txt")
        f = open(os.path.expanduser(os.path.join("~/Desktop", str(i+1) + ".txt")), "a")
        fn = tarfile.open(fname , "w")
        fn.add(tname)
        fn.close()

#PART 5