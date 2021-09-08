#pre drvops
'''
#Targil #1

budget = int(input("what is your marketing budget: \n"))
fb = int(input("how many days do you want the facebook campagin to run (cost is 100 a day):\n"))
ig = int(input("how many days do you want the instagram campagin to run (cost is 50 a day):\n"))

a=fb*100
b=ig*50
c=(a+b)*1.17
print((a) + (b))

print("your cost for the campaigns is: " + str(c))
if (c<=budget):
    print("Success")
else:
    print("you need to add " + str(c-budget))

'''

