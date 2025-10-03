#ZC 1st while loops notes
import time
import random
tocount = int(input("say a number:  "))
print(f"counting to {tocount} with a for loop:")
for num in range(1,(tocount + 1)):
    print (num)
    time.sleep(0.25)
num = 1
print (f"counting to {tocount} with a while loop:")
while num < (tocount + 1):
    print(num)
    num += 1
    time.sleep(0.25)

#print ("this is a infinite loop:")
#num = 1
#while num > 0:
#    print (num)
#    num += 1000
goosenum = int(input("enter a number:  "))
goose = random.randint (1,goosenum)
count = 0
while count != goose:
    print ("Duck!")
    count += 1
else:
    print ("Goose!")

i = 0
while i < 20:
    time.sleep(0.125)
    i += 1
    if i == 10:
        print ("I is ten")
        continue
    else:
        print(f"{i} iteration of the loop")
    