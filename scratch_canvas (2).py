import turtle

side = int(input('type the side of your square'))
if side > 0 and side < 100:
    turtle.fillcolor('red')
elif side >= 100 and side <= 200:
    turtle.fillcolor('green')
else:
    turtle.fillcolor('blue')

turtle.begin_fill()
for variable in range(0, 4):
    turtle.forward(side)
    turtle.left(90)
turtle.end_fill()