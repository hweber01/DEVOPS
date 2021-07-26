#files01
'''
filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r+")
file.write("192.168.0.1\n192.168.0.2")
print(file.read())
file.close()



#append
file = open(filename, "a")
file.write("crazy people\n192.168.0.1\n")

#print to screen
file = open(filename, "r")
print(file.read())
file.close()

#files02
filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r")
for line in file:
    print(line)
file.close()

filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r")
my_string=file.read()
file.close()
print(my_string)

filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"

file = open(filename, "r")
#for line in file:
mystring=file.read()
file.close()
print(mystring)
mylist=mystring.split(",")
print(type(mylist))
print(mylist)

mylist=[]
filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"

file = open(filename, "r")
for line in file:
    print(line)
    mylist.append(line)
file.close()
print(mylist)

mylist=[]
filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"

file = open(filename, "r")
for line in file:
    print(line)
    mylist.append(line)
file.close()
print(mylist)

filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r")
newlist=[]
newlist=file.read().splitlines()
print(type(newlist))
print(newlist)
file.close()
'''
filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r")
print(file.readlines()[1:3])
file.close()

#file = open("C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling01.txt","x")
#file.close()