# ZC 1st Shopping List Manager

shopping_list = []

while True:
    print ("\n 1 = add to list \n 2 = remove from list \n 3 = show list \n 4 = quit\n")
    action = input("enter your action\n")
    if action == "1":
        item = input("what item do you want to add\n")
        shopping_list.append(item)
        print (f"{item} was added to your list")
    elif action == "2":
        item = input("what is the item you want to remove?")
        if item in shopping_list:
            shopping_list.remove(item)
            print (f"{item} was removed from the shopping list")
        else:
            print (f"{item} is not in your shopping list")
    elif action == "3":
        if shopping_list:
            for x,item in enumerate(shopping_list, 1):
                print(f"\n{x}. {item}")

    elif action == "4":
        break
    else:
        print ("that is not a valid command")
