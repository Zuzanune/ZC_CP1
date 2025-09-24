#ZC 1st What is my grade assignment
Pgrade = float(input("what is your grade:  "))
if Pgrade > 100:
    print (f"Wow! you got extra-credit! you got {Pgrade - 100} points of extra credit! ")
elif float(Pgrade) >= 94.0 and Pgrade < 100:
    print ("you got an A! great job!")
elif float(Pgrade) >= 90 and Pgrade < 94.0:
    print ("you got a A-")
elif float(Pgrade) >= 87 and Pgrade < 90:
    print ("you got a B+")
elif float(Pgrade) >= 84 and Pgrade < 87:
    print ("you got a B")
elif float(Pgrade) >= 80 and Pgrade < 84:
    print ("you got a B-")
elif float(Pgrade) >= 77 and Pgrade < 80:
    print ("you got a C+")
elif float(Pgrade) >= 75 and Pgrade < 77:
    print ("you got a C")
elif float(Pgrade) >= 70 and Pgrade < 75:
    print ("you got a C-")
elif float(Pgrade) >= 67 and Pgrade < 70:
    print ("you got a D+")
elif float(Pgrade) >= 64 and Pgrade < 67:
    print ("you got a D")
elif float(Pgrade) >= 60 and Pgrade < 60:
    print ("you got a D-")
elif float(Pgrade) >= 0 and Pgrade < 60:
    print ("you got a F. what can you do to improve that?")
elif float(Pgrade) < 0:
    print ("you somehow got less then zero? is that even possible?")