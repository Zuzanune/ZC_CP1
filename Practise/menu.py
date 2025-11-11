#ZC 1st menu program
while True:
    #list all menu prices using a dictionary
    menu = {"mains:" : "", "pizza" : 7.99, "beefburger": 10.15, "spiceburger" : 11.50,"chezburg" : 5.99, "nacho" : 4.50, "nacho delux" : 6.50, "sides:" : "",  "fries" : 4.00, "fountain drink" : 2.99, "water" : 0, "iced cream" : 4.50, "condements:" : "",  "ketchup" : 0.25, "mustard" : 0.25}
    order = []
    cost = 0
    #display menu and price
    for dis in menu:
        print (f"{dis} ${menu[dis]}")
    #while loop for item selections.
    while True:
        #ask user for item
        added = input("what do you want to add to your order:  ")
        if added not in menu:
            print(f" i am sorry, we do not serve {added}")
            continue
        #add price to total
        cost += menu[added]
        order.append(added)
        #ask user if they are done adding items
        end = input("is this all(y/n):  ")
        if end.lower() == "y" or end.lower() == "yes":
            #if they are, quit
            break
        else:
            continue
    #print total menu and cost
    print ("this is your order:")
    for ic in order:
        print (f"you orderd:  {ic}")
    print (f"total cost: {cost}")
    
    #ask user for a tip of 0% 10% and 30%
    tip = int(input("please select a tip of $0, $5, $15, or custom"))
    cost += tip
    #display new total and ask for comfirmation
    print(f"your new cost is {cost}")
    print ("please enter all of your bank credentials, including your password, username, and current balance")
    input()
    break
print ("here is your order. thank you for coming to Wam Burger")
for en in order:
    print (f"1 {en}" )
