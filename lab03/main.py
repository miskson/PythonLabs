import random
import re


def todigit(string):
    if string.isdigit():
        digit = int(string)
        return digit
    else:
        return string


# task1----------------------------------
# 1.a
a = list(random.randint(-60, 60) for i in range(10))
print("List A has been created.")

# 1.b
n = todigit(input("Input size of list B that you wish: "))
if type(n) != int:
    print("Invalid input")
else:
    b = list(random.randint(0, 50) for i in range(n))
    print(b)

# 1.10
rev = list.copy(a)
rev.append(rev[0])
del rev[0]
print("Normal list A: ", a)
print("List A changed: ", rev)


# task2----------------------------------
# 2.a

rows = todigit(input("Input rows quantity: "))
cols = todigit(input("Input columns quantity: "))
if type(rows) != int or type(cols) != int:
    print("Invalid input")
else:
    a2 = [[random.randint(-10, 10) for j in range(cols)] for i in range(rows)]
    # 2.b
    b2 = [[random.randint(0, 20) for j in range(cols)] for i in range(rows)]
    print("Your list a2 looks like: ", a2)
    print("Your list b2 looks like: ", b2)


# 2.10

try:
    a2
except NameError:
    print("There is no list to operate on.")
else:
    oddSum = 0
    if len(a2) > 0 and cols < 3:
        print("There is not enough columns in your list, can only count sum of all odd elements of the first row.")
        for k in range(len(a2[0])):
            if a2[0][k] % 2 != 0:
                oddSum = oddSum + a2[0][k]
        print("Sum of odd elements of the firs row is: ", oddSum)
    elif len(a2) > 0 and cols >= 3:
        maxCol = a2[0][2]
        for j in range(len(a2)):
            if maxCol <= a2[j][2]:
                maxCol = a2[j][2]
        print("Max element of third column is: ", maxCol)
        for k in range(len(a2[0])):
            if a2[0][k] % 2 != 0:
                oddSum = oddSum + a2[0][k]
        print("Sum of odd elements of the firs row is: ", oddSum)

# 3.10


def sortbylength(element):
    return len(element)


theString = input("input the string: ")
if theString != "" and re.match(r"[\W]", theString[0]) is not True and re.match(r"[\w!?,.;:]", theString[len(theString) - 1]):
    newString = theString.split(" ")
    newString.sort(key=sortbylength)
    print(newString)
else:
    print("Error, the string may contain forbidden characters in the beginning or end of the string."
          " Or there is no string at all.")
