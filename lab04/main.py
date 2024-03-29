import random
from collections import namedtuple


def showperson(person):
    print(person.surname, ": salary -", person.salary, ", sex -", person.sex)


def showall(persons):
    for person in persons:
        showperson(person)
    print("*****")


def showallsorted(base):
    base.sort(key=lambda Person: Person.surname)
    print("Sorted list:")
    showall(base)


def deletekey(base):
    keyname = input("Input key you want to delete(or input 'q' to exit): ")
    if quitinput(keyname): return False
    for person in base:
        if keyname == person.surname:
            del base[base.index(person)]
            print("-Key has been deleted.")
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
    base.append(Person(surname, salary, sex))
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


def getmaxsalaryperson(base):
    maxsalaryperson = max(base, key=lambda person: person.salary)
    return maxsalaryperson


def getminsalaryperson(base):
    minsalaryperson = min(base, key=lambda person: person.salary)
    return minsalaryperson


def getminimalsalarypeople(base):
    men = []
    women = []
    result = []
    for person in base:
        if person.sex == "male":
            men.append(base[base.index(person)])
        elif person.sex == "female":
            women.append(base[base.index(person)])
    result.append(getminsalaryperson(men))
    result.append(getminsalaryperson(women))
    print("Minimal salary staff:")
    showall(result)


Person = namedtuple('Person', ('surname', 'salary', 'sex'))
surnames = ['Joebob', 'King', 'Bill', 'Mann', 'Ripley', 'Weaver', 'Hicks', 'Nukem', 'Anderson', 'Smith']
sex = ('male', 'female')
base = [Person(surnames[i], round(random.uniform(200, 500), 2), random.choice(sex)) for i in range(10)]

showall(base)
showallsorted(base)
showall(base)
updatebase(base)
showall(base)
print("Minimal salary people: ")
getminimalsalarypeople(base)
showall(base)
print("Minimal salary person:")
showperson(getminsalaryperson(base))
print("Maximal salary person:")
showperson(getmaxsalaryperson(base))
