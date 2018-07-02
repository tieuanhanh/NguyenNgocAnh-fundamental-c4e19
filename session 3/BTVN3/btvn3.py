clothes = [ "T- shirt", "Sweater"]

loop = True

while loop:

    n = input ("Welcome to our shop, what do you want (C, R, U, D)? ")

    if n == "R" or n == "r":
        print ("Our items: ", end="")
        print ( *clothes, sep=", ")
        print ("\n")

    elif n == "C" or n == "c":  
        new_item = input ("Enter new items: ")
        clothes.append (new_item)
        print ("Our items: ", end="")
        print ( *clothes, sep=", ")
        print ("\n")

    elif n == "U" or n == "u":
        look = True
        while look:
            upd_pos = int (input ("Update position? "))
            if upd_pos > 3 or upd_pos < 1:
                print ("You have entered the wrong index. Plz enter the number from 1 to 3")
            else:
                look = False
                upd_item = input ("New item? ")
                clothes [upd_pos - 1] = upd_item
                print ("Our items: ", end="")
                print ( *clothes, sep=", ")
                print ("\n")          

    elif n == "D" or n == "d":
        looc = True
        while looc:
            del_pos = int (input ("Delete position? "))
            if del_pos >3 or del_pos <1:
                print ("You have entered the wrong index. Plz enter the number from 1 to 3")
            else:
                looc = False
                clothes.pop(del_pos - 1)
                print ("Our items: ", end="")
                print ( *clothes, sep=", ")
                print ("\n")

    elif n == "exit":
        print ("Exit")
        break

    else:
        print (" You have entered the wrong letter! ")
        loop = False