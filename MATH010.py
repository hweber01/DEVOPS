num=9485
a=num//1000
h=(num-(a*1000))//100
t=(num-(a*1000+h*100))//10
o=(num-(a*1000+h*100+t*10))
print("Alafim: " + str(a) + "\nMeot: " + str(h) + "\nAsarot: "+ str(t) + "\nAhadot: " + str(o))

print("Alafim: " + str(num//1000) + "\nMeot: " + str(num%1000//100) + "\nAsarot: "+ str(num%100//10) + "\nAhadot: " + str(num%10))