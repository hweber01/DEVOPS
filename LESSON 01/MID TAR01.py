'''
#Mid tar 01

#print("Net4U, is the best place\n   …in the world")

#Mid tar02

from datetime import datetime
now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Current date and time =\n" + dt_string)

#tar03

fn=input("enter first name:\n")
ln=input("enter last name:\n")

print(ln + " " +fn +"\n" + ln[::-1] + " " +fn[::-1])

#tar04

nm=input("enter a flle name:\n")
xt=input("enter file type(extention)\n")
print(nm + "." + xt +"\nthe dumb answer is done here:" + xt + "_____\n")
fstr=(nm + "." + xt)
print(fstr)
find='.'
l=len(fstr)
print(str(l))
res1 = fstr.find(".")
print("the position is:" + str(res1))
print("the extension is: " + fstr[res1+1:l])

#tar05

n=input("enter a number between 1-9:\n")
if(int(n)<1 or int(n)>9):
    print("your number is out of range, please restart")
else:
    print("the result for n+nn+nnn is:\n" + str(int(n)+int(n*2)+int(n*3)))


#tar06

n=input("enter a number:\n")
if (int(n) % 2)==0:
    print("even")
else:
    print("odd")


#tar07

f=input("emter feet:\n")
n=input("enter inches:\n")
print(f + " feet and " + n + " inches are:" + str(int(f)*30.48 + int(n)*2.54) + " cm")

#tar08

n = 20
d = {"x":200}

print(type(n)())
print(type(d)())


def Empty_Var(lst):
   return [type(i)() for i in lst]
lst = ["python",{"x":12},[10,12,"sfsd"], (4,5), 200]
print("Original objects:")
print(lst)
print("\nEmpty the said variables without destroying it:")
print(Empty_Var(lst))


#tar09

dict_t= {0: 10, 1: 20}
print(dict_t.values())
print(dict_t.keys())
print(len(dict_t))
Keymax = max(dict_t, key=dict_t.get)
valmax = max(dict_t.values())
print(Keymax)
print(valmax)
print(dict_t)
dict_t.update({Keymax+1:valmax+10})
print(dict_t)


#tar10
from collections import defaultdict, Counter
tstr='Net4U'
my_dict = {}
for letter in tstr:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

l=len(tstr)
print(str(l))
tdict={}
bdict={}
for i in range(l):
    k=tstr[i]
    v=i+1
    tdict.update({k:v})
    print(tdict)

#tar11

first_string=input("enter a string:\n")
second_string=input("enter another string:\n")
c_string=(first_string + "," +second_string)
#print(c_string)
i=c_string.index(',')
l=len(c_string)
#print(str(i) + ',' +str(l))
print(c_string[(i+1):(l-1)] + c_string[i-1] + "," + c_string[0:(i-1)] + c_string[l-1])

#tar12
import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))

#tar13

# Python program to find sum of elements in list
total = 0


list1 = [11, 5, 17, 18, 23]

for elements in range(0, len(list1)):
	total = total + list1[elements]

print("Sum of all elements in given list: ", total)
'''
#tar17

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list1.pop(5)
list1.pop(4)
list1.pop(0)
print(list1)