#ZC 1st Turtle Race
#import modules
import turtle as t
import time
import random
#define avalable colors
colors = ["black", "aquamarine2", "lawngreen", "grey", "DodgerBlue1", "gold", "red"]
#create turtles
t1 = t.Turtle()
t1.hideturtle()
t2 = t.Turtle()
t2.hideturtle()
t3 = t.Turtle()
t3.hideturtle()
t4 = t.Turtle()
t4.hideturtle()
t5 = t.Turtle()
t5.hideturtle()
#create screen
screen = t.Screen()
#create finish line
t.hideturtle()
t.penup()
t.teleport(300,250)
t.pendown()
t.right(90)
t.forward(500)
#define turtle shape, color, and location
t1.shape("turtle"), t2.shape("turtle"), t3.shape("turtle"), t4.shape("turtle"), t5.shape("turtle")
t1.teleport(-400,200), t2.teleport(-400,100), t3.teleport(-400,0), t4.teleport(-400,-100), t5.teleport(-400,-200)
t1.color(random.choice(colors)), t2.color(random.choice(colors)), t3.color(random.choice(colors)), t4.color(random.choice(colors)), t5.color(random.choice(colors))
#count down from 3
t1.showturtle(),t2.showturtle(),t3.showturtle(),t4.showturtle(),t5.showturtle()
screen.title("Turtle Race!")
time.sleep(1)
screen.title("3!")
time.sleep(1)
screen.title("2!")
time.sleep(1)
screen.title("1!")
time.sleep(1)
screen.title("Go!")
#make turtles move
while True:
    t1.forward(random.randint(10,25))
    t2.forward(random.randint(10,25))
    t3.forward(random.randint(10,25))
    t4.forward(random.randint(10,25))
    t5.forward(random.randint(10,25))
    #print who wins
    if t1.xcor() > 300:
        print ("Racer 1 Wins!!!!")
        break
    elif t2.xcor() > 300:
        print ("Racer 2 Wins!!!!")
        break
    elif t3.xcor() > 300:
        print ("Racer 3 Wins!!!!")
        break
    elif t4.xcor() > 300:
        print ("Racer 4 Wins!!!!")
        break
    elif t5.xcor() > 300:
        print ("Racer 5 Wins!!!!")
        break
t.done()
    
