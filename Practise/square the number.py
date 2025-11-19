#ZC 1st square the number
#define numbers list
nums = []
print ("please input all numbers you want to square. type done when you are done")
#let user place items into number list
while True:
    add = input("")
    if add == "Done" or add == "done" or add == "d":
        break
    nums.append(int(add))
#create map function to square all numbers in numbers list
squared = list(map(lambda num: num * num, nums))
#print new list
for i,x in enumerate(squared):
    print (f"original: {nums[i]} squared: {squared[i]}")

