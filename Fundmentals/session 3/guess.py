from random import randint

r = randint (1, 100)

loop = True
count = 0

while loop:

    n = int (input ( "Enter a number = "))

    if r < n:
        print (" Too large ")

    elif r > n:
        print (" Too small ")

    else:
        print (" Bingo")
        break

    count += 1
    if count == 7:
        print (" You lost")
        break
        # loop = False
    
 
