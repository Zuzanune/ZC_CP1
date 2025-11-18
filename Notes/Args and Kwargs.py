#ZC 1st args and kwargs
def hello(name = "Zane", age = 23):
    print (f"hello {name}")
hello(age = 23, name = "zane")
def hi(*names, **kwargs):
    print (type(names))

    for n in names:
        print (f"hello {n} {kwargs['last_name']}")
hi("alex"," katy"," jarret"," bob"," jeff", last_name = "Carter")