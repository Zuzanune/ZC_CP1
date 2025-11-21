#ZC 1st Factorial project using  Pseudocode
#original Pseudocode:
#   declare variable as in -- num -- as a user input
#   asking user for any whole numper. use .strip() and .lower
#   define function as calculate(factorial -- num)
#   place in while loop: if num is greater than 100, tell user that is is not valid and try again
#   elif num is a string or float

def calculate():
    while True:
        #i moved this code here so that i can change the number during error handling
        num = int(input("enter a number between 1 and 100:  "))
        #you can not use .lower or .strip on a intiger, so I left those out
        if num > 100:
            print ("please enter a number less than 100")
            continue
        elif isinstance(num, str) or isinstance(num, float):
            print ("please enter a number")
            continue
        #this is as far as the original psudocode went. everything after this is of my own hand
        total = 1
        original = num
        for x in range(num):
            total *= num
            num -= 1
        print (f"factorial: {total}. original: {original}")
calculate()
    
