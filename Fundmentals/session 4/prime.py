numb = int (input ("Nhap 1 so = "))

is_prime = True

    # for i in range (2, numb):
    #     m = numb % i
    #     if m == 0:
    #         print ("{0} is not a prime number.".format(numb))
         
    #     else:
    #         print ("{0} is a prime number".format(numb))
i = 2

while i <= (numb ** 0.5) :
    if numb % i == 0:
        is_prime = False
        break       # hay nè
    i += 1
if is_prime:    # hay nè
    print ("{0} is a prime number.".format(numb))
else:
    print ("{0} is not a prime number.".format(numb))
            
