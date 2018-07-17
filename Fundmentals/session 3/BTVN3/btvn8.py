sizes = [5, 7, 300, 90, 24, 50, 75]

print ("Hello, my name is Hiep and here is my flock: ")
print (sizes, "\n")

max_size = max (sizes)

print ("Now my biggest sheep has size {0} let's shear it".format(max_size), sep="\n")

pos = sizes.index (max_size)
sizes[pos] = 8

print ("After shearing, here is my flock", sizes, sep="\n")
print ("\n")

for i in range(1,3):
    print ("MONTH {0}: ".format(i))
    for j in range(len(sizes)):
        sizes[j] += 50
    print ("One month has passed, now here is my flock:", sizes, sep= "\n")
    max_size = max (sizes)
    print ("Now my biggest sheep has size {0} let's shear it".format(max_size))
    pos = sizes.index(max_size)    
    sizes[pos] = 8
    print ("After shering, here is my flock: ", sizes, sep= "\n")
    print ("\n")

print ("MONTH 3:")   
for i in range(len(sizes)):
    sizes[i] += 50
print ("One month has passed, now here is my flock:", sizes, sep="\n")
print ("\n")

total = 0
for j in sizes:
    total += j
print ("My flock has size in total: ", total)

revenue = total * 2

print ("I would get {0} * 2$ = {1}$".format(total, revenue))