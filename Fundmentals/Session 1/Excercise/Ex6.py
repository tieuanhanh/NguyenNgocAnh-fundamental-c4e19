import turtle
fillcolor ("green")

begin_fill()

t = turtle.Turtle()

n = int(input(" So vong tron = "))

for i in range(n):

    t.circle(50)
    t.left(360/n)

end_fill()
