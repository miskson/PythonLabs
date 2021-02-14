import random

def todigit(string):
    if(string.isdigit()):
        digit = int(string)
        return digit
    else:
        return string

#task1----------------------------------
#1.a
a = list(random.randint(-60, 60) for i in range(10))
print("List A has been created.")

#1.b
n = todigit(input("Input size of list B that you wish: "))
if(type(n) != int):
    print("Invalid input")
else:
    b = list(random.randint(0, 50) for i in range(n))
    print(b)

#1.10
rev = list.copy(a)
rev.append(rev[0])
rev.pop(0)
print("Normal list A: ", a)
print("List A changed: ", rev)

#task2----------------------------------
#2.a
cols = todigit(input("Input columns quantity: "))
rows = todigit(input("Input rows quantity: "))
if (type(rows) != int or type(rows) != int):
    print("Invalid input")
else:
    a2 = [[random.randint(-10, 10) for j in range(cols)] for i in range(rows)]
    #2.b
    b2 = [[random.randint(0, 20) for j in range(cols)] for i in range(rows)]
    print("Your list a2 looks like: ", a2)
    print("Your list b2 looks like: ", b2)




