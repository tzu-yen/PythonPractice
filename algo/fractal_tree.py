import turtle
import random

def tree(branchLen, t):
    psize = t.pen()["pensize"]
    if psize < 1: t.pen(pensize=1)
    else: t.pen(pensize= psize-0.1)
    
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)

if __name__ == "__main__":
    t = turtle.Turtle()
    myWin = turtle.Screen()
    print t.heading()
    t.speed(0)
    #t.color("green")
    t.pen(pencolor="blue", pensize=20, fillcolor="black")
    t.left(90) #t.setheading(90) #0-east, 90-north, 180-west, 270-south
    t.up()
    t.backward(100) # t.setposition(0, -100)
    t.down()    
    tree(75, t)
    t.home()
    t.circle(100)
    t.circle(50, 180)
    t.circle(200, steps=10)
    t.dot(20, "blue")
    t.forward(40)
    t.dot(20, "red")
    t.color("purple")
    t.stamp()
    t.forward(20)
    myWin.exitonclick()
