import turtle
import time
import random
colors = ["black", "aquamarine2", "lawngreen", "grey", "DodgerBlue1", "gold", "red"]
for t in ["t1","t2","t3","t4","t5"]:
    
finish = turtle.Turtle()
screen = turtle.Screen()
t[0].shape("turtle"), t[1].shape("turtle"), t[2].shape("turtle"), t[3].shape("turtle"), t[4].shape("turtle")
t[0].teleport(-200,200)
t[1].teleport(-200,100)
t[2].teleport(-200,0)
t[3].teleport(-200,-100)
t[4].teleport(-200,-200)
t[0].color(random.choice(colors))
t[1].color(random.choice(colors))
t[2].color(random.choice(colors))
t[3].color(random.choice(colors))
t[4].color(random.choice(colors))
screen.title("Turtle Race!")
time.sleep(1)
screen.title("3!")
time.sleep(1)
screen.title("2!")
time.sleep(1)
screen.title("1!")
time.sleep(1)
screen.title("Go!")
while True:
    for turtles in t:
        turtles.forward(random.randint(10,25))
        if turtles.xcor() > 300:
            print(f"{turtles.color()[1]} turtle wins")
            exit()

    
