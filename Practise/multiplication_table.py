#ZC 1st multiplication table project
cnum = 0
running = True
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nums2 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
totalist = []
tlist = []
for x in nums:
    cnum = x
    for y in nums2:
        total = x * y
        totalist.append(total)

    tlist.extend(totalist)
    tlist.append("\n")
    totalist = []
for x in tlist:
    print(str(x),end=" ")
    
    

