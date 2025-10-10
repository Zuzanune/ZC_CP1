import random
player_items = []
computer_items = []
while True:
    board = [1,2,3,4,5,6,7,8,9]
    print (f"{str(board.index(1)),str((board.index(2))),str((board.index(3)))},\n,{str(board.index(4)),str((board.index(5))),str((board.index(6)))},\n,{str(board.index(7)),str((board.index(8))),str((board.index(9)))}")
    
    
    #turns
    player_choice = input("choose a square between 1 and 9")
    player_items.append(player_choice)
    board[player_choice] = "X"
    computer_choice = random.randint(1,9)
    computer_items.append(computer_choice)
    board[computer_choice] = "O"
    


