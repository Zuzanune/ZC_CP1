#ZC 1st Libraries and built in functions
import turtle
num = 1
stamp = turtle.Turtle()
stamp.shape('turtle')
stamp.color('blue')
stamp.begin_fill()
while num < 5:
    stamp.forward(150)
    stamp.left(90)
    num += 1
stamp.end_fill()
stamp.color('black')
stamp.penup()
stamp.goto(150,0)
stamp.pendown()
num = 1
stamp.begin_fill()
while num < 5:
    stamp.forward(150)
    stamp.left(90)
    num += 1
stamp.end_fill()
stamp.left(90)
stamp.color('white')
stamp.shape('arrow')
stamp.shapesize(10)
stamp.stamp()
stamp.shapesize(1)
stamp.shape('turtle')
stamp.color('black')
stamp.goto(0,0)
num = 1
stamp.begin_fill()
while num < 5:
    stamp.back(150)
    stamp.left(90)
    num += 1
stamp.end_fill()

stamp.right(90)
stamp.forward(300)
num = 1
stamp.begin_fill()
stamp.color("blue")
while num < 5:
    stamp.right(90)
    stamp.forward(150)
    num += 1
stamp.end_fill()
stamp.back(150)
stamp.right(90)
stamp.shape('arrow')
stamp.color('white')
stamp.shapesize(10)
stamp.stamp()
stamp.shapesize(10)
turtle.done()