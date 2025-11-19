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
        for h in x:
            total *= h
    print (total)
def average(*numbers):
    total = 0.0
    count = 0.0
    for x in numbers:
        for h in x:
            total += h
            count += 1
    av = (total/count)
    round(av, 2)
    print (av)
def bot(*numbers):
    for x in numbers:
        total = min(x)
    print (total)

def top(*numbers):
    for x in numbers:
        total = max(x)
    print (total)


#create while loop for base code

while True:
    nums = []
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
        top([i for i in nums])
    elif asked == "min":
        bot([i for i in nums])
    else:
        print ("invalid equation")
        nums = []
    