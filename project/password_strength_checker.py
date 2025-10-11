#ZC 1st Password Strength Checker
score = 0
#assign score variable
upper = False
#create variable to make sure more then one uppercase letter will not increase the score
length = 0
#create variable to check length
lower = False
#create variable to make sure more then one lowercase letter will not increase the score
SC = False
#create start variable to let player only have one special character effect the score
number = False
#create start variable to let player only have one number effect the score
password = input("please enter your password for analasis:  ")
#ask the user for a password
password.strip()
#idiot proof the password
for X in password:
    #start password for loop
    if X == "(" or "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "_" or "+" or "-" or "=" or "[" or "]" or "{" or "}" or "|" or ";" or ":" or "," or "." or "<" or ">" or "?" or ")":
        #check for special characters
        if SC != True:
            #check if a special character has already been found
            score += 1
            #increase score
            SC = True
            #Special characters no longer effect score
    if X.isupper() == True:
        #check if the letter is uppercase
        if upper == False:
            #check if an uppercase letter has already been found
            score += 1
            #increase score
            upper = True
            #uppercase letters can no longer effect the score
    if X.isdigit() == True:
        #check if the letter is a number
        if number == False:
            #check if a number has already been found
            score += 1
            #increase score
            number = True
            #numbers can no longer effect the score
    if X.islower() == True:
        #check if X is a lowercase letter
        if lower == False:
            #check if a lowercase number has already been found
            score += 1
            #increase score
            lower = True
            #lowercase numbers can not longer effect code
    length += 1
    #increase length
if length > 8:
    #check length
    score += 1
    #increase score
if score < 2:
    print (f"your score is{score} you should work on that password more")
elif score == 3:
    print (f"your score is 3, about average. dont use this password for anything important")
elif score == 4:
    print (f"your score is 4. it is a great password, but it could use some work")
elif score == 5:
    print ("That is a great password! you have a score of 5! I doubt anyone could figure it out.")
#tell player score




    
