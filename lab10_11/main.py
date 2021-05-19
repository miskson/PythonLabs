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

    # constructor
    def __init__(self, name, age, employment=None, wage=0, workdays=0, workhours=0):
        self.name = name
        self.age = age
        self.wage = wage
        self.employment = employment
        self.workdays = workdays
        self.workhours = workhours
        self.income = f"My monthly income is: {self.monthlyincome()}. My year income is: {self.yearlyincome()}"

    # for computer representation
    def __repr__(self):
        return f"{self.name} is The object of class {self.__class__.__name__} stored ad {hex(id(self))}"

    # for humans
    # def __str__(self):
    #     return f"class {self.__class__.__name__}:\n" \
    #            f"   name: {self.name}\n" \
    #            f"   age: {self.age}\n" \
    #            f"   employmentstatus: {self.employmentstatus}\n" \
    #            f"   responsabilities: {self.responsabilities}\n" \
    #            f"   wage: {self.wage}\n" \
    #            f"   workdays: {self.workdays}\n" \
    #            f"   workhours: {self.workhours}\n" \
    #            f"   income: {self.income}\n"

    # methods
    def greet(self):
        print("Hello, my name is ", self.name, " I'm ", self.age, "years old.")
        if isinstance(self.employment, object):
            print(f"I am {self.employment} .My working responsibilities are: НЕВАЖНО")
        else:
            print("I'm currently unemployed.")

    def monthlyincome(self):
        monthincome = ((self.wage * self.workhours) * self.workdays) * 3
        return monthincome

    def yearlyincome(self):
        yearincome = self.monthlyincome() * 12
        return yearincome

# ------------------------------------------------------------------------------------------------
work1 = Work()
print(work1.profession.value[1])
person1 = Person("Sergei", 20, work1)

person1.greet()
print(person1.income)
generateobjectfile(person1)
