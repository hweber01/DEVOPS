#build the list
fb=[]
lg=int(input("enter a number to define the length of the string: "))

for j in range(lg):
    fb.append(int(input("enter a number to add to the list: ")))
    print(fb)
#check if fibonaci

fib="True"

for i in range(2,len(fb)):
    print(i)
    print(str(fb[i]) + "," + str(fb[i-1]) + "," +str(fb[i-2]))
    if fb[i]==(fb[i-1]+fb[i-2]):
        continue
    else:
        fib="False"
        break
if fib=="True":
    print("FIBO!!!!")
else:
    print("NOT FIBO")