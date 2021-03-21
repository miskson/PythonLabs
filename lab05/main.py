import re
from collections import namedtuple


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

#2.A
consonants = re.compile(r"[bcdfghklmnpqrstvwxz]")
#thetext = ['This','is','the','list','of','some','words','so','what']
thetext = ['aaa','some','shit','bout','that','aaaa']
wordinfo = []
Word = namedtuple('Word', ('theword', 'consonants', 'posindex'))
consonatscount = 0
for word in thetext:
    for i in word:
        if re.match(consonants, i.lower()):
            consonatscount += 1
    wordinfo.append(Word(word, consonatscount, thetext.index(word)))
    consonatscount = 0
print(wordinfo)
wordinfo.sort(key=lambda word: word.consonants, reverse=True)
print(wordinfo)
print(thetext)
#for i in range(2):
del thetext[wordinfo[0].posindex]
del thetext[wordinfo[1].posindex]
del thetext[wordinfo[2].posindex]

print(thetext)

