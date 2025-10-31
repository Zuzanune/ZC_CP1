import turtle as t
import random
import time
#define maze turtle
maze = t.Turtle()
#ask for maze width/height
maze_width = int(input("How wide do you want your maze to be?"))
maze_height = int(input("how tall do you want your maze to be"))
start = [maze_width, maze_height]
rows = []
columns = []
#create a outline of maze
maze.teleport(0, int(maze_height/2))
maze.forward(int(maze_width/2))
maze.left(90)
maze.forward(maze_height)
maze.left(90)
maze.forward(maze_width)
maze.left(90)
maze.forward(maze_height)
maze.left(90)
maze.forward(int(maze_width/2))
maze.color('white')
maze.back(20)
maze.forward(20)
for x in start:
    x /= 10
t.done()