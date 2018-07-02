from turtle import *

title ("hinh vuong mau sac")
shape ("arrow")
speed (-1)

colors = [ "red", "blue", "brown", "yellow", "grey"]

for i in colors:
    color (i)
    fillcolor (i)
    begin_fill()
    for j in range (2):
        forward (50)
        right (90)
        forward (100)
        right (90)
    forward (50)
    end_fill()

mainloop()