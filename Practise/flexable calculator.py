#ZC 1st Flexable Calculator
def sum(*numbers):
    total = 0
    for x in numbers:
        for h in x:
            total += h
    print (total)
def product(*numbers):
    total = 1
    for x in numbers:
        total *= x
    print (total)
def average(*numbers):
    total = 0.0
    count = 0.0
    for x in numbers:
        total += x
        count += 1
    av = (total/count).round(2)
    print (av)
def min(*numbers):
    total = min(numbers)
    print (total)

def max(*numbers):
    total = max(numbers)
    print (total)


#create while loop for base code
nums = []
while True:
    #define how to input equation
    print ("please enter all numbers you wish to proform the operation on(type done when you are done) ")
    while True:
        numadd = input()
        if numadd == "done" or numadd == "Done":
            break
        else:
            numadd = int(numadd)
            nums.append(numadd)
    #ask which equation to do
    asked = input("which equation do you want to preform.(available options: Sum, Product, Average, max, min):  ").lower().strip()
    if asked == "sum":
        sum([i for i in nums])
    elif asked == "product":
        product([i for i in nums])
    elif asked == "average":
        average([i for i in nums])
    elif asked == "max":
        max([i for i in nums])
    elif asked == "min":
        min([i for i in nums])
    else:
        print ("invalid equation")
        nums = []
    

    #create functions for each equation type
    #args and kwargs to input all numbers
    #do equtaion