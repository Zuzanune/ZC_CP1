#ZC 1st Caesar Cipher
#create start lists of alphebet
alphebet = ["abcdefghijklmnopqrstuvwxyz"]
enstring = ""
#ask user what they are encoding
string = input("what are you trying to encode/decode:  ")
#create function for encode
def code(Encodenum, enstring):
    newlet=0
    #ask what they want to decode/encode
    #find value in alphebet and increase it by selected amount, making sure it loops oiver if past 26
    for x in string:
        x.lower()
        if x in alphebet:
            letter_val = alphebet.index(x)
            encodednum = letter_val + Encodenum
            if encodednum > 26:
                encodednum -= 26
            newlet = alphebet[encodednum]
    return enstring + str(newlet)
#call encode function
alincrease = int(input("by which number do you want to encode your message along the Caesar cipher:  "))
enstring = code(alincrease,enstring)
#print encoded string
print (f"the encoded message is now {enstring}")
        
