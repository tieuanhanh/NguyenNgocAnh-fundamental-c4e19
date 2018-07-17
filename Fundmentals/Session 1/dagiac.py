from turtle import *
shape('turtle')
color('green')
speed(-1)

canh = int(input("so canh cua da giac:"))

for i in range(canh):
    forward(100)
    left(360/canh)

mainloop()
    