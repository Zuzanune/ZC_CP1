#ZC 1st who_are_you.py
run = True
name_list = []
print ("hey! i want to know a bit about you")
while run == True:
    print ("what is your name?")
    name = input()
    
    if name in name_list:
        print ("you have already entered your name",name,",you do not need to complete this again")
        run = False
        break
    name_list.append(name)
    print ("thank you! may i ask, how old are you?")
    age =input()
    print ("thank you",name)
    print ("what is your favorite color?")
    color = input()
    
    print ("nice to meet you",name," i know now that you are",age," years old and your favorite color is",color)