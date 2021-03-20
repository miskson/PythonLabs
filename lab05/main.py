import re


def validatestring(string):
   if string != "" and re.match(r"[\W]", string[0]) is not True and re.match(r"[\w!?,.;:]", string[len(string) - 1]):
       return True
   else:
       return False


def isnotsign(string):
    if re.match(r"[\W]", string):
        return False
    else:
        return True


thestring = input("input string: ")
if validatestring(thestring):
    stringarr = list(filter(None, re.split(r"[^-'\w]", thestring)))
    stringarr = list(filter(isnotsign, stringarr))
    stringarr.sort()

    couples = []
    coincidences = 0
    coincidenceInd = 0
    couplesnum = 0
    for i in stringarr:
        for k in stringarr:
            if i == k:
                coincidences += 1
                coincidenceInd = k

        if coincidences > 2 or coincidences <= 1:
            coincidences = 0
            coincidenceInd = 0
        elif coincidences == 2:
            couples.append(i)
            coincidences = 0
            coincidenceInd = 0

    print("Pairs of words that are similar it the string: ", couples)

else:
    print("String contains forbidden characters or empty")

