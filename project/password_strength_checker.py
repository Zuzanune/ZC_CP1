#ZC 1st Password Strength Checker

#assign score variable
score = 0
#create variable to make sure more then one uppercase letter will not increase the score
upper = False
#create variable to check length
length = 0
#create variable to make sure more then one lowercase letter will not increase the score
lower = False
#create start variable to let player only have one special character effect the score
special_character = False
#create start variable to let player only have one number effect the score
number = False
#ask the user for a password
password = input("please enter your password for analasis:\n")
#idiot proof the password
password = password.strip()
#create function for giving tips later
def code_tips():
    if length < 8:
        print ("try increasing the length")
    if upper == False:
        print ("try adding an uppercase letter")
    if lower == False:
        print ("try adding a lowercase letter")
    if number == False:
        print ("try adding a number")
    if special_character == False:
        print ("try adding a special character")
#start password for loop
for X in password:    
    #check for special characters
    if X == "(" or X =="!" or X =="@" or X =="#" or X =="$" or X =="%" or X =="^" or X =="&" or X =="*" or X =="(" or X == ")" or X =="_" or X =="+" or X =="-" or X =="=" or X =="[" or X =="]" or X =="{" or X =="}" or X =="|" or X ==";" or X ==":" or X =="," or X =="." or X =="<" or X ==">" or X =="?" or X ==")":    
        #check if a special character has already been found
        if special_character != True:
            #increase score
            score += 1
            #Special characters no longer effect score
            special_character = True
            #check if the letter is uppercase
    if X.isupper() == True:
        #check if an uppercase letter has already been found
        if upper == False:
            #increase score
            score += 1
            #uppercase letters can no longer effect the score
            upper = True
    #check if the letter is a number
    if X.isdigit() == True:
        #check if a number has already been found
        if number == False:
            #increase score
            score += 1
            #numbers can no longer effect the score
            number = True
    #check if X is a lowercase letter
    if X.islower() == True:
        #check if a lowercase number has already been found
        if lower == False:
            #increase score
            score += 1
            #lowercase numbers can no longer effect the score
            lower = True 
    #increase length
    length += 1
#check length
if length >= 8:
    #increase score
    score += 1
    #tell user their score

if score == 0:
    print ("your score is 0. you should work on that password more")
    print ("try adding a password")
elif score <= 2:
    print (f"your score is {score}. you should work on that password more")
    code_tips()
elif score == 3:
    print (f"your score is 3, about average. Don't use this password for anything important")
    code_tips()
elif score == 4:
    print (f"your score is 4. it is a great password, but it could use some little tweaks")
    code_tips()
elif score == 5:
    print ("That is a great password! you have a score of 5! I doubt anyone could figure it out.")
else:
    print ("error")
#finished





    
