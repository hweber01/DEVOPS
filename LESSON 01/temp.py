'''
test_dict = {"Gfg": ["34", "45", 'geeks'], 'is': ["875", None, "15"], 'best': ["98", 'abc', '12k']}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Extract Numerical Dictionary values
# Using loop + zip() + isdigit()
res = []
for a, b, c in zip(*test_dict.values()):
    if a.isdigit():
        res.append((a, b, c))

# printing result
print("The Numerical values : " + str(res))


import socket
IP_addres = socket.gethostbyname('google.com')
print("IP Address is:" + IP_addres)
'''

n=1

#s1=str(n)*2
#m=int(s1)*2
#print("\n" + str(s1))

for i in range(3):
    s1 = str(n) * i
    m=int(s1)*i
    print("\n" +str(s1))
    i=i+1
    #q=s
    #r=int(q)+m
    #print(str(r))