#Conditions
'''
name=input("enter a name: ")

if(name=="Noa"):
    print("Great")
    age = int(input("what is " + name + "'s age? "))
    if(age==14):
         print("wow")
    else:
        print("worng!")
else:
    print("does not match")
'''

choice=int(input("enter a number between 1-4: \n"))
if(choice==1):
    n=int(input("enter a number:\n"))
    print("Your result is:\n" + str(n**3))
elif(choice==2):
    iplist=[]
    ipa=(input("enter an ip address: \n"))
    ipb=(input("enter an ip address: \n"))
    ipc=(input("enter an ip address: \n"))
    ipd=(input("enter an ip address: \n"))
    iplist.append(ipa + " , " + ipb + " , " + ipc + " , " + ipd)
    print(iplist)
elif(choice==3):
    dnsdict={}
    asite = input("enter a website name: \n")
    bsite = input("enter a website name: \n")
    csite = input("enter a website name: \n")
    dsite = input("enter a website name: \n")
    import socket
    ip_a = socket.gethostbyname(asite)
    ip_b = socket.gethostbyname(bsite)
    ip_c = socket.gethostbyname(csite)
    ip_d = socket.gethostbyname(dsite)
    print("IP Address is:" + ip_a + " , " + ip_b + " , " + ip_c + " , " + ip_d)
    dnsdict.update({asite: ip_a , bsite: ip_b , csite: ip_c , dsite: ip_d ,})
    print(dnsdict)
elif(choice==4):
    word=input("enter a word: \n")
    if word==word[::-1]:
        print(word + " is a palindrome")
    else:
        print(word + "is not a palindrome")

elif(choice<1 or choice>4):
    print("wrong choice! bye bye")