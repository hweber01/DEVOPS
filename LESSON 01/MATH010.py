from turtle import goto

num = int(input("enter a 4 digit number:"))
if num > 9999:
    print("number too large enter a positive bumber between 0-9999")
    goto(num)
else:
    a = num // 1000
    h = (num - (a * 1000)) // 100
    t = (num - (a * 1000 + h * 100)) // 10
    o = (num - (a * 1000 + h * 100 + t * 10))
    print("Alafim: " + str(a) + "\nMeot: " + str(h) + "\nAsarot: " + str(t) + "\nAhadot: " + str(o))

    print("Alafim: " + str(num // 1000) + "\nMeot: " + str(num % 1000 // 100) + "\nAsarot: " + str(
        num % 100 // 10) + "\nAhadot: " + str(num % 10))
