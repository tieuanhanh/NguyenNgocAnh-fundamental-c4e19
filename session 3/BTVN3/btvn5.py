sizes = [5, 7, 300, 90, 24, 50, 75]

max_size = max (sizes)

print ("Hello, my name is Hiep and there are my sheep sizes: ")
print (sizes, "\n")

print ("Now my biggest sheep has size {0} let's shear it.".format(max_size), "\n")

pos = sizes.index(max_size)
sizes[pos] = 8

print ("After shearing, hear is my flock: ")
print (sizes)


