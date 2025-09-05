#ZC 1st Idiot proofing
print("...")
print("...")
namrun = True
while namrun:
    print("please enter your name:   ")
    name = input()
    name = name.lower().capitalize().strip()
    print(f"do you want to confirm {name} as your name?")
    nameq = input("y/n:  ")
    nameq = nameq.lower().strip()
    if nameq == "y" or "yes":
        namrun = False
print ("what is your phone number?(type it in as 000-000-0000)")
phonenum = input()
phonenum = phonenum.strip().replace("-"," ")
print("what is your GPA")
GPa = input()
GPa = float(GPa.strip())
print(f" thank you {name} i know know that your phone number is{phonenum} and your GPA is {GPa}")
print("please expect to be bombarded with emails and phone calls.")





    