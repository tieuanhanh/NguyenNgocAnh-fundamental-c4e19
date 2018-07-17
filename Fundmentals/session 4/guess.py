print ("Think of a number from 1 to 100 then press enter " )
input()             # nhan enter xuong dong
print("""c if my guess is correct
s if it is smaller
l if it is larger""")

low = 0
high = 100

loop = True

while loop:
    mid = (low + high)//2
    n = input ("is {0} your number?".format(mid)).lower()   #chuyen tat ca cac chu thanh chu hoa (upper())

    if n == "c":
        print ("I knew it")
        loop = False
        
    if n == "s":
        low = mid
        if low >= (high - 1):
            print (" You are a liar")
            break
        
    if n == "l":
        high = mid
        if low >= (high - 1):
            print (" You are a liar")
            break
     


    





