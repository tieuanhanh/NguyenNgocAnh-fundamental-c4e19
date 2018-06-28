from turtle import *

shape ("arrow")
speed (-1)

for i in range (3,7,1):
    if i % 2 == 0:
        color ("green")
    else:
        color ("red")
    for j in range (i):
        forward (100)
        left (360/i)

mainloop()

