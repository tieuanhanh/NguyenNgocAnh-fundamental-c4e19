from turtle import *

color ("blue")
hideturtle()
speed (-1)
length = 150
left (135)

while length > 0:
    for i in range (4):
        forward (length)
        left (90)
    right (10)
    length -= 3
    

mainloop()