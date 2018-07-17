from turtle import *

title ("da giac mau sac")
shape ("arrow")

colors = [ "red", "blue", "brown", "yellow", "grey"]

for index, i in enumerate (colors):
    color (i)
    for j in range (index+3):
        forward (100)
        left ( 360/ (index + 3))

# color ("red")
# for i in range (3):
#     forward (100)
# #     left (360/3)
mainloop()



