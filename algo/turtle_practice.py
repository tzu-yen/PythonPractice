import turtle


t = turtle.Turtle()
myWin = turtle.Screen()
t.pen(fillcolor='red', pencolor='green', pensize=5)
#t.color('red', 'yellow')
t.fill(True) # t.begin_fill()
t.circle(80)

t.pendown()


turtle.forward(100)

turtle.left(120)

t.fill(False) #t.end_fill()
myWin.exitonclick()

