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
'''

#tar08

