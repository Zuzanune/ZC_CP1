#ZC 1st elif and logical operators notes
grade = float(input("what is your grade:  "))
if grade > 100:
    print ("Wow! you got extra-credit! amazing")
elif grade == 100.0:
    print ("A perfect Score! great job!")
elif float(grade) >91.5 and grade < 100:
    print ("you got an A! great job!")
elif float(grade) >= 89 and grade < 91.5:
    print ("a A-. not bad")
elif float(grade) >= 83 and grade < 89:
    print ("a B+ or a B is not terrible.")
elif grade < 0.0:
    print ("what? how! you got less then zero?")
else:
    print ("you need to work on your grades")