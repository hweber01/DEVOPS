#lab  08
'''
f=[]
l=input("enter a number to define the length of the string: ")
if((isinstance(l,int))):
    for i in range(l):
        f.append(str(input("enter a number to add to the list: ")))
        print(f)
#else:
#    l=input("you did not enter a number\nplease enter a number to define the length of the string: ")



'''
fb=[1,2,3,5,8,13]
boolean="True"

for i in range(2,len(fb)):
    print(str(fb[i]) + "," + str(fb[i-1]) + "," +str(fb[i-2]))
    if fb[i]==(fb[i-1]+fb[i-2]):
        continue
    else:
        boolean="False"
        break

if boolean=="True":
    print("FIBO!!!!")
else:
    print("NOT FIBO")


#while(True):
#i=input("enter first #:\n")