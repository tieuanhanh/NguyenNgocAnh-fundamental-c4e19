numb = int (input( "Enter a number = "))
original_numb = numb
count = 0

loop = True

while loop:
# While numb > 0: (thi ko phai dat loop = True nua)
    numb = numb//10
    count += 1
    if numb == 0 :       
        loop = False

# print (original_numb, "has", count, "digit(s)")
    
print ("{0} has {1} digit(s).".format(original_numb, count))
   
    