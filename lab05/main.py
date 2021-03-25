import sys
import re
from collections import namedtuple


def validatestring(string):
   if string != "" and re.match(r"[\W]", string[0]) is not True and re.match(r"[\w!?,.;:]", string[len(string) - 1]):
       return True
   else:
       return False


def validatetextEn(string):
    string = re.findall(r"[\w']+|[.,!?;]", string)
    string = list(filter(isnotsign, string))
    strlength = len(string)
    counter = 0
    for i in string:
        if re.match(r"[a-zA-Z]", i):
            counter += 1
        else: break

    if counter == strlength:
        return True

    return False


def isnotsign(string):
    if re.match(r"[\W]", string):
        return False
    else:
        return True


def customsplit(string):
    string = string.split()
    for i in string:
        re.split(r"[^-'\w]", string)
    return string


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
thetext = input("Input your text: ")
print(thetext)
thetext = re.findall(r"[\w']+|[.,!?; ]", thetext)
if len(thetext) > 3:
    wordsinfo = []
    Word = namedtuple('Word', ('theword', 'consonants', 'posindex'))
    consonatscount = 0

    for word in thetext:
        #checking if the word contains eng letters
        if re.match(r"[a-zA-Z0-9,-.:;'`\"[\]()!? ]", word):
            for i in word:
                #counting consonants in the word
                if re.match(consonants, i.lower()):
                    consonatscount += 1
            #adding current word to the named tuple that contains word information
            wordsinfo.append(Word(word, consonatscount, thetext.index(word)))
            consonatscount = 0
        else:
            # if word contains symbols different from eng -> print error and finish runtime
            print("Error, looks like text contains non-english words or characters.")
            sys.exit()

    wordsinfo.sort(key=lambda word: word.consonants, reverse=True)

    neededwords = []
    for i in range(3):
        if wordsinfo[i].consonants != 0:
            neededwords.append(wordsinfo[i])

    neededwords.sort(key=lambda word:word.posindex, reverse=True)

    print("neededwords: ", neededwords)

    if len(neededwords) == 3:
        for i in range(3):
            del thetext[neededwords[i].posindex]
    else:
        print("Looks there is less then 3 words with consonants in them, or no words with consonants at all.")
        print(''.join(thetext))
        sys.exit()

    print("the text after words being deleted:")
    thetext = ''.join(thetext)
    print(thetext)

else:
    print("the string contains forbidden characters or less than 3 words.")


