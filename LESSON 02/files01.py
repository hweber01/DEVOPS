#files01
'''
filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r+")
file.write("let's go\n")
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
'''

