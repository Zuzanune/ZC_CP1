import turtle
def draw_branch(length):
    if length > 5:
        for i in range(3):
            pen.forward(length)
            draw_branch(length/3)
            pen.backward(length)
            pen.right(60)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.color("Light Blue")
pen.goto(0,0)
for i in range(6):
    draw_branch(50)
    pen.right(60)
pen.hideturtle()

turtle.done()
