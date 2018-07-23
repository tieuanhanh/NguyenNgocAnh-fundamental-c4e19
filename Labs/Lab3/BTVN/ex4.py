from turtle import *
from ex3 import drawing_square

for i in range (30):
    drawing_square(i*5, 'red')
    left(17)
    penup()
    forward (i*2)
    pendown()

mainloop()