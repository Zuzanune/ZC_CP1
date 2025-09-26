#ZC 1st fix_the Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))
        #this is a runtime error caused by the fact that you code is a string
        #and that in line 18 you are dividing it by a intiger
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
            #on line 22 and 27, i added a attempts variable increase 
            #because that was missing. this is a logic error
        elif guess < number_to_guess:
            print("Too low! Try again.")
            attempts += 1     
        continue
    print("Game Over. Thanks for playing!")
start_game()