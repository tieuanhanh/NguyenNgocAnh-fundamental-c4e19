sizes = [5, 7, 300, 90, 24, 50, 75]

print ("Hello, my name is Hiep and there are my sheep sizes: ")
print (sizes, "\n")

month = int(input(" Enter a number of months: "))
print ("\n")

for j in range(1, month + 1):

    print ("MONTH {0}:".format(j))
    for i in range (len(sizes)):
        sizes[i] += 50
    print ("One month has passed, now here is my flock: ")
    print (sizes)
    max_size = max(sizes)
    print ("Now my biggest sheep has size {0} let's shear it".format(max_size))
    pos = sizes.index (max_size)
    sizes[pos] = 8
    print ("After shearing, here is my flock: ")
    print (sizes, "\n")
