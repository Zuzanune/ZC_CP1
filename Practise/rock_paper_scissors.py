# ZC 1st rock Paper scissors
import random
import time
running = True
while running:
    attack = random.randint(1,3)
    if attack == 1:
        attack = "rock"
    elif attack == 2:
        attack = "paper"
    elif attack == 3:
        attack = "scissors"
    pattack = input("enter rock, paper, or scissors:  ")
    if attack == "rock":
        print ("rock!!")
        print("""
              ________
            /        \\
           / //       |
           | \\       |
           \\         / 
            \\_______/    """)
        print ("(just pretend that is a rock)")
    elif attack == "scissors":
        print ("Scissors!!")
        print ("""
           _____    
          / / \\\\       _______ 
         /  \\ /\\  ____/ ______|
         \\     \\_/  ___/
         |_________  /
         |      ___  \\___
        /  / \\  \\ \\___ \\_____
        \\  \\ /   |     \\______|
         \\______/    

               """)

    elif attack == "paper":
        print ("Paper!!")
        print ("""
                _______
               | ~~~~~ |
               | ~~~~~ |
               | ~~~~~ |
               |_______|""")
    if pattack == attack:
        print ("Its a tie!")    
    elif (pattack.lower() == "rock" and attack == "scissors") or (pattack.lower() == "scissors" and attack == "paper") or (pattack.lower() == "paper" and attack == "Rock"):
        print ("You win!")
    elif (pattack.lower() == "rock" and attack == "paper") or (pattack.lower() == "scissors" and attack == "rock") or (pattack.lower() == "paper" and attack == "scissors"):
        print ("You lose!")
    else:
        print("error")
    
    quits = input("do you want to quit?(y/n)")
    if quits.lower() == "y":
        print ("ok, goodbye")
    else:
        continue

