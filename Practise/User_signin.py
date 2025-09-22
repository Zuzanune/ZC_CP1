#ZC 1st User Sign In
user_name = input("what do you want your username to be:   ")
password = input("what do you want your password to be:  ")
unp = False
pnp = False
running = True
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
print ("Login")
print ("\n")
while running:
    unl = input("what is your username:  ")
    pl = input ("what is your password:  ")
    if unl != user_name:
        unp = True
    if pl != password:
        pnp = True
    print ("\n")
    if unp == True:
        print ("your username is incorrect")
    elif pnp == True:
        print ("your password is incorrect")
    elif pnp and unp == True:
        print ("both your username and your password is incorrect")
    else:
        print ("login credentials correct")
        print ("Welcome to our Learning world")
        print ("\n")
        print ("\n")
        print ("\n")
        print ("ADD:")
        print ("Do you want more sweat? buy Sweat juice")
        print ("to cool off from the inside as well as the outside!")
        print ("now only $40 for 12 oz!")
        running = False
