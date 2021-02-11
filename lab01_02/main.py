import math

def checkNum(number):
    try:
        number = float(number)
        if(number <= 0):
            return False
    except Exception:
        return False
    else: return True

# task1------------------------------------------

print("Z = cos^e(x) - sqrt(x)")
x = input("Input x: ")
if(checkNum(x)):
    x = float(x)
    try:
        z = math.pow(math.cos(math.radians(x)), math.exp(1)) - math.sqrt(x)
        #z = math.cos(math.radians(x))
        print("z =", z)
    except ValueError as err:
        print("Value", x, "causes error:", err, ",wich means expression can only be described with formula"
                                                " or impossible to count.")
else:
    print("Value of X contains invalid data. Try again")
print("***")

# task2------------------------------------------

print("Спортсмен пробігає за 1-й день М км, кожний наступний день він збільшує норму пробігу на К%."
      " Визначите через скільки днів норма пробігу може стати більше 50 км.")
M = input("Input M: ")
K = input("Input K: ")
if(checkNum(M) and checkNum(K)):
    M = float(M) * 1000
    K = float(K)
    days = 1
    while( M <= 50000):
        tempK = (M * K)/100
        M = M + tempK
        days += 1
        print(M)
    print("Running norm distance is going to become more than 50km in", days, " days")
else:
    print("Values of M and K may contain invalid data. Try again")
