# ZC 1st Caesar Cipher
# create start list of alphabet
alphebet = "abcdefghijklmnopqrstuvwxyz"
enstring = ""
# ask user what they are encoding
string = input("what are you trying to encode/decode:  ")
# create function for encode
def code(Encodenum, enstring):
    newlet = ""
    # find value in alphabet and increase it by selected amount, looping if past 26
    for x in string:
        x = x.lower()
        if x in alphebet:
            letter_val = alphebet.index(x)
            encodednum = letter_val + Encodenum
            if encodednum >= 26:
                encodednum -= 26
            newlet = alphebet[encodednum]
            enstring += newlet
        else:
            enstring += x  # keep non-letter characters
    return enstring
# call encode function
alincrease = int(input("by which number do you want to encode your message along the Caesar cipher:  "))
enstring = code(alincrease, enstring)
# print encoded string
print(f"the message is now {enstring}")
