# ZC 1st rock Paper scissors
import random
import time
running = True
while running:
    attack = random.randint(1,3)
    if attack == 1:
        attack = "Rock"
    elif attack == 2:
        attack = "Paper"
    else:
        attack = "scissors"
    Pattack = input("enter rock, paper, or scissors:  ")
    if attack == "Rock":
        print("""
              ________
            /         \\
           /          \\
           l          l
            \\       / 
              \\    /
                l__I    """)
        print ("(just pretend that is a rock)")
