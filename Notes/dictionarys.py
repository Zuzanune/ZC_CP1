#ZC 1st Dictionary Notes!

#Key:Value pairs:
person = {"name":"John Doe", "age": 18, "job": "costco", "favfood" : "yogurt"}
print (person["favfood"])
for key in person.keys():
    print(f"{key} is {person[key]}")
person["favfood"] = "milk"
print (person["favfood"])