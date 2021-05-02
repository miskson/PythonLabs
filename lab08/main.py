def checklistdecorator(func):
    def inner(somelist):
        if type(somelist) != list:
            return print("argument is not a list!")
        try:
            func(somelist)
        except:
            return "an error occured."

    return inner


@checklistdecorator
def lineelementswap(somelist):
    firstelem = somelist[0]
    lastelem = somelist[len(somelist) - 1]
    del somelist[len(somelist) - 1]
    somelist.append(firstelem)
    somelist[0] = lastelem

    return somelist

def reversestring(string):
    str = ""
    for i in string:
        str = i + str

    return str

#8.10.1
with open('myfile.txt') as f, open('myfileRewritten.txt', 'w') as f2:
    for line in f:
        splitted = line.split()
        lineelementswap(splitted)
        splitted[len(splitted) - 1] = splitted[len(splitted) - 1] + "\n"
        towrite = " ".join(splitted)
        f2.write(towrite)


neededline = None
with open('myfile2.txt', 'r') as f3:
    lineslist = f3.readlines()

#8.10.2
iteration = 0
for line in lineslist:
    iteration += 1
    if line[len(line) - 2] == "!":
        neededline = lineslist.pop(lineslist.index(line))
        #print(neededline)
        neededline = neededline.split()
        neededline = " ".join(neededline)
        neededline = reversestring(neededline) + "\n"
        #print(neededline)
        iteration -= 1
        break

#print("linelist:", lineslist)
#print(iteration)

if neededline is not None:
    f4 = open('myfile2.txt', 'w')
    f4.close()

    with open("myfile2.txt", "r+") as f4, open("myfile2Rewritten.txt", "w") as f5:
        for i in range(len(lineslist)):
            f4.write(lineslist[i])

        for i in range(len(lineslist)):
            if i == iteration:
                f5.write(neededline)
            f5.write(lineslist[i])
