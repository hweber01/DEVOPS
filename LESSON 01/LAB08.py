#lab  08
'''
fibo=[1,2,3,5,9,13,21,34,55]

boolean="True"

for i in range(2,len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i]==(fibo[i-1]+fibo[i-2]):
        continue
    else:
        boolean="False"
        break

if boolean=="True":
    print("FIBO!!!!")
else:
    print("NOT FIBO")
'''
fibo=[]

while(True):
    i=input("enter first #:\n")

