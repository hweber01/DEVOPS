t = int(input("enter tomatoes:"))
c = int(input("enter cucumbers:"))
d = int(input("enter coke:"))
o = int(input("enter chicken:"))

print("tomatoes: " +str(t*3) + "NIS" + "\ncuecumbers " + str(c*2) + "NIS" + "\ncoke: " +str(d*5) + "NIS" + "\nchicken: " +str(o*20) + "NIS" + "\ntotal: " +str("%.0f"%(((t*3+c*2+d*5+o*20)*1.17))))