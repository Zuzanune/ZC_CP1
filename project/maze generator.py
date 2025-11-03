import turtle as t
import random

maze = t.Turtle()
maze.speed(0)
maze.pensize(2)

def build_maze():
    square_count = 25
    square_size = 20
    start_x = -250
    start_y = 250

    # draw outline of maze
    maze.penup()
    maze.goto(start_x, start_y)
    maze.pendown()
    for _ in range(4):
        maze.forward(square_count * square_size)
        maze.right(90)

    # draw each square
    for row in range(square_count):
        for col in range(square_count):
            # top-left of square
            x = start_x + col * square_size
            y = start_y - row * square_size
            maze.penup()
            maze.teleport(x, y)

            if random.choice([True, False]):
             #draw top side
                maze.setheading(0)
                maze.pendown()
                maze.forward(square_size)
                maze.penup()

            if random.choice([True, False]):
                # draw right side
                maze.setheading(-90)
                maze.pendown()
                maze.forward(square_size)
                maze.penup()

            if random.choice([True, False]):
                # draw bottom side
                maze.setheading(180)
                maze.pendown()
                maze.forward(square_size)
                maze.penup()

            if random.choice([True, False]):
                # draw left side
                maze.setheading(90)
                maze.pendown()
                maze.forward(square_size)
                maze.penup()

build_maze()
t.done()
