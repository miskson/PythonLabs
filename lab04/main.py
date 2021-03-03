import random


def showall(dictionary):
    print("*****")
    for key in dictionary:
        print(key, dictionary[key])
    print("*****")


def showallsorted(dictionary):
    keylist = list(dictionary.keys())
    keylist.sort()
    for i in keylist:
        print(i, ':', dictionary[i])


def deletekey(base):
    keyname = input("Input key you want to delete(or input 'q' to exit): ")
    if quitinput(keyname): return False
    for key in base:
        if keyname == key:
            del base[key]
            print("/Key has been deleted.")
            return True
    print("There is no such key in base.")
    return False


def updatebase(base):
    status = False
    while status is False:
        print("Let's update the dictionary, input following values(or input 'q' to exit): ")
        surname = input("Surname: ")
        if quitinput(surname): return False
        salary = input("Salary: ")
        if quitinput(salary): return False
        sex = input("1 - male / 2 - female: ")
        if quitinput(sex): return False
        status = validateinfo(surname, salary, sex)

    salary = round(float(salary), 2)
    if sex == "1":
        sex = 'male'
    elif sex == "2":
        sex = 'female'
    base.update({surname: {'salary': salary, 'sex': sex}})
    print("/Base has been updated.")


def quitinput(string):
    if string == "q":
        return True
    else: return False


def validateinfo(surname, salary, sex):
    surnamevalid = False
    salaryvalid = False
    sexvalid = False
    if surname.isalpha():
        surnamevalid = True
    else:
        print("!Surname contains forbidden characters or empty.")

    try:
        float(salary)
        salaryvalid = True
    except ValueError:
        print("!Salary is invalid.")

    if sex == "1" or sex == "2":
        sexvalid = True
    else:
        print("!Sex is invalid.")

    if surnamevalid is True and salaryvalid is True and sexvalid is True:
        return True
    else:
        return False


surnames = ['Joebob', 'Dude', 'Bill', 'Mann', 'Xuan', 'Weaver', 'Pavlov', 'Shlapic', 'Anderson', 'Smith']
base = {}
for i in range(len(surnames)):
    sex = random.randint(0, 1)
    if sex == 0:
        sex = 'male'
    else:
        sex = 'female'
    base.update({surnames[i]: {'salary': round(random.uniform(200, 500), 2), 'sex': sex}})
showall(base)
updatebase(base)
showall(base)
deletekey(base)
showall(base)
showallsorted(base)
#hi