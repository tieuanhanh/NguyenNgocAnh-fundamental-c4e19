rabbit = {0:0, 1:1}

month = int(input("Enter the month = "))

for n in range (2,month+3):
    if n not in rabbit:
        new_value = rabbit[n-1] + rabbit [n-2]
        rabbit[n] = new_value
    print ("Month {0}: {1} pair(s) of rabbit".format (n - 2, rabbit[n]))