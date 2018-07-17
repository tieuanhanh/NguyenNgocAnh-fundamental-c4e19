from turtle import *

shape ("turtle")
fillcolor ("yellow")

speed (-1)

begin_fill()

canh = int(input ("So canh cua da giac la "))

for i in range(canh):
    forward (100)
    left (360/canh)

end_fill()

mainloop()