#function2
'''
#Not recieving and returning values
def calc():
     n1 = int(input("enter a #: "))
     n2 = int(input("enter a #: "))
     print("your calc # is: " + str(n1*n2))

### MAIN
calc()

#  recieving and not returning values

def calc2(x,y):
    print("1st # is: " + str(x) + "\n2nd # is: " + str(y))
    print("result is: " +str(x**y))
###MAIN

calc2(2,3)


# not recieving value and rturning value
def calc3():
    n1 = (input("enter a #: "))
    n2 = (input("enter a #: "))
    sum=(int(n1)*int(n2))
    print("your calc # is: " + str(sum))
    return sum

a=calc3()+57
print("yasss" + str(a))

# recieving value and rturning value
def calc4(x,y):
    print("1st # is: " + str(x) + "\n2nd # is: " + str(y))
    sum=x**y
    print("result is: " + str(sum))
    return sum


###MAIN
a = int(input("enter a #: "))
b = int(input("enter a #: "))
j=calc4(a,b) + 28
print("Yas: "+ str(j))

'''

def add_ip(list,ip1,ip2,ip3):
    #print("list in def: " + str(list))
    list=[]
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list

ip_list=[]
ip_n1=input("enter ip1: ")
ip_n2=input("enter ip2: ")
ip_n3=input("enter ip3: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
#ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)