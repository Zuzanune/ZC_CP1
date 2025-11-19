# ZC 1st mapping notes
numbers = [901,876,345,836,103,892,476]

"""new_nums = []
for num in numbers:
    new_nums.append(num/3)"""
def divide(num):
    return num/3
new_nums = map(lambda num: num/3, numbers)
for num in new_nums:
    print(num)
