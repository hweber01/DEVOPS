#files01

filename = "C:/Users/hille/Desktop/Documents/HILLEL/CYBER COURSE/PYTHON/handling.txt"
file = open(filename, "r+")
file.write("crazy people\n")
print(file.read())
file.close()


#append
file = open(filename, "a")
file.write("crazy people\n")

#print to screen
file = open(filename, "r")
print(file.read())
file.close()