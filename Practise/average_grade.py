#ZC 1st Average grade
class_amount = float(input("how many classes do you have?:  "))
class_numbers = class_amount
grades = []
grade_total = 0
while class_numbers > 0:
    if class_numbers == 1:
        class1 = float(input("what is your grade for your 1st class"))
        grades.append(class1)
    elif class_numbers == 2:
        class2 = float(input("what is your grade for your 2nd class?"))
        grades.append(class2)
    elif class_numbers == 3:
        class3 = float(input("what is your grade for your 3rd class?"))
        grades.append(class3)
    else:
        classetc = float(input("what is your grade for your next class?"))
        grades.append(classetc)
    class_numbers -= 1
for avgrad in grades:
    grade_total += avgrad
    trav = round(float(grade_total/class_amount), 2)
print ("your average grade is", trav)