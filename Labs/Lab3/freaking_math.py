from random import randint, choice
import eval

x = randint (1, 10)
y = randint (1, 10)

ops = ['+', '-', '*', '/']
op = choice (ops)

res = eval.calc(x, y, op)

errors = [-1, 0, 1]
error = choice (errors)

print ("{0} {1} {2} = {3}".format(x, op, y, res+error))

ans = input("(Y/N)? ").lower()
if error == 0:
    if ans == 'y':
        print ("Yay")
    elif ans == 'n':
        print ("You're wrong")
else:
    if ans == 'y':
        print ("You're wrong")
    elif ans == 'n':
        print ("Yay")

# if (error == 0 and ans == "Y") or (error !=0 and ans == "N"):
#     print ("Yay")
# else:
#     print ("Wrong")


