from turtle import *

shape ("arrow")
color ("red")
speed (-1)

right(30)

for i in range (4):
    for i in range (2):
        forward(100)
        left(60)
        forward(100)
        left(120)
    left(90)

left(150)

mainloop()