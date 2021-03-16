import re


def validatestring(string):
   if string != "" and re.match(r"[\W]", string[0]) is not True and re.match(r"[\w!?,.;:]", string[len(string) - 1]):
       return True
   else: return False


thestring = input("input string: ")
if validatestring(thestring):
    print("working:", thestring)
    #stringarr = re.split(r"[^-'\w]", thestring)
    filter(re.match(r"[^-'\w]"), thestring) #to finish
    print(stringarr)
else:
    print("failed")

