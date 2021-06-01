from enum import Enum
from random import choice

def objectcheck(func):
    def inner(obj):
        if isinstance(obj, object) is not True:
            return print("given value is not an object!")
        else:
            try:
                func(obj)
            except:
                return print("an error occurred")

    return inner

def checkSalaryInfo(wage, workdays, workhours):
    if workhours > 0 and workdays > 0 and wage > 0:
        return True
    else: return False

@objectcheck
def generateobjectfile(obj):
    with open(f"{obj.__class__.__name__}__{obj.name}.txt", "w") as f:
        strings = str(obj)
        f.write(strings)


class RolesAndRespons(Enum):
    role1 = ('QC', 'testing apps')
    role2 = ('BA', 'app requierments development')
    role3 = ('Dev', 'app development')
    role4 = ('PM', 'project managment')
    role5 = ('Baker', 'cooking bakery')
    role6 = ('Builder', 'building structures')
    role7 = ('Postman', 'delivering letters')
    role8 = ('Soldier', 'army service')
    role9 = ('Police officer', 'civil order maintenance')
    role10 = ('Fireman', 'extinguishing fires')


class Work:
    profession = tuple

    def __init__(self):
        self.profession = choice(list(RolesAndRespons))


class Person:
    # fields
    name = str
    age = int
    employment = Work
    wage = float
    workdays = int
    workhours = int
    monthincome = float
    income = str

    # constructor
    def __init__(self, name, age, employment=None, wage=0, workdays=0, workhours=0):
        self.name = name
        self.age = age
        self.wage = wage
        if hasattr(employment, 'profession'):
            self.employment = employment
        else:
            self.employment = None

        if checkSalaryInfo(wage, workdays, workhours):
            self.workdays = workdays
            self.workhours = workhours
            self.income = f"My monthly income is: {self.monthlyincome()}. My year income is: {self.yearlyincome()}"
        else:
            self.workdays = self.wage = self.workhours = self.income = 'not stated'

    # for computer representation
    def __repr__(self):
        return f"{self.name} is The object of class {self.__class__.__name__} stored ad {hex(id(self))}"

    # for humans
    def __str__(self):
        return f"class {self.__class__.__name__}:\n" \
               f"   name: {self.name}\n" \
               f"   age: {self.age}\n" \
               f"   employment: {self.employment.profession.value}\n" \
               f"   wage: {self.wage}\n" \
               f"   workdays: {self.workdays}\n" \
               f"   workhours: {self.workhours}\n" \
               f"   income: {self.income}\n"

    # methods
    def greet(self):
        print("Hello, my name is ", self.name, " I'm ", self.age, "years old.")

        if self.employment is not None:
            print(f"I am {self.employment.profession.value[0]} .My working responsibilities are: {self.employment.profession.value[1]}")
        else:
            print("I'm currently unemployed.")


    def monthlyincome(self):
        if self.wage != 'not stated' or self.workdays != 'not stated' or self.workhours != 'not stated':
            monthincome = ((self.wage * self.workhours) * self.workdays) * 3
            return monthincome
        else:
            return 'not stated'


    def yearlyincome(self):
        if self.wage != 'not stated' or self.workdays != 'not stated' or self.workhours != 'not stated':
            yearincome = self.monthlyincome() * 12
            return yearincome
        else:
            return 'not stated'

# ------------------------------------------------------------------------------------------------
work1 = Work()
word = 'word'
work2 = Work()

person1 = Person("Sergei", 20, work1, 24, 10, 30)
person1.greet()
print(person1.income)
print(person1.monthlyincome())
print(person1.yearlyincome())
person2 = Person("David", 21, work2)

generateobjectfile(person1)
generateobjectfile(person2)


