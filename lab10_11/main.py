from enum import Enum
from random import choice
from abc import ABC, abstractmethod


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


class HumanExeption(Exception):
    pass


class WorkExeption(HumanExeption):
    pass


# abstract class
class Human(ABC):
    def greet(self):
        pass

    def walk(self):
        pass

    @staticmethod
    def breathe():
        print("*inhale*...*exhale*...")


class StudiesAndDescr(Enum):
    stud1 = ('KhPI', 'Computer engeneering')
    stud2 = ('Economic University', 'Economics')
    stud3 = ('Cadet Academy', 'Cadet study')
    stud4 = ('MIT', 'Nuclear Physics')
    stud5 = ('Cambridge', 'Lawyer')


class Study:
    info = tuple

    def __init__(self):
        self.info = choice(list(StudiesAndDescr))


class Student(Human):
    name = str
    age = str
    study = Study

    def __init__(self, name, age, study):
        self.name = name
        self.age = age
        self.study = study

    def __repr__(self):
        return f"{self.name} is The object of class {self.__class__.__name__} stored ad {hex(id(self))}"

    def __str__(self):
        return f"class {self.__class__.__name__}:\n" \
                f"   name: {self.name}\n" \
                f"   age: {self.age}\n" \
                f"   employment: {self.study.info.value}\n" \


    def greet(self):
        print(f"Hello my name is {self.name} I am {self.age} years old")
        print(f"I am student of {self.study.info.value[0]} .My study program is: {self.study.info.value[1]}")

    def walk(self):
        if self.age <= 30:
            print("It's not difficult for me to walk 10000+ steps during the day")
        else:
            print("My walking norm is 10000 steps a day")


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


def checksalaryinfo(wage, workdays, workhours):
    if workhours > 0 and workdays > 0 and wage > 0:
        return True
    else: return False


class Worker(Human):
    name = str
    age = int
    employment = Work
    wage = float
    workdays = int
    workhours = int
    income = str

    # constructor
    def __init__(self, name, age, employment, wage=0, workdays=0, workhours=0):
        self.name = name
        self.age = age
        self.wage = wage
        self.employment = employment

        if checksalaryinfo(wage, workdays, workhours):
            if workdays > 7:
                raise WorkExeption("There are only 7days in a week!")
            else:
                self.workdays = workdays

            if workhours > 12:
                raise WorkExeption("Cannot work more than 12 hours!")
            else:
                self.workhours = workhours
                self.income = f"My monthly income is: {self.monthlyincome()}. My year income is: {self.yearlyincome()}"

        else:
            self.workdays = self.wage = self.workhours = self.income = 'not stated'

    def __repr__(self):
        return f"{self.name} is The object of class {self.__class__.__name__} stored ad {hex(id(self))}"

    def __str__(self):
        return f"class {self.__class__.__name__}:\n" \
               f"   name: {self.name}\n" \
               f"   age: {self.age}\n" \
               f"   employment: {self.employment.profession.value}\n" \
               f"   wage: {self.wage}\n" \
               f"   workdays: {self.workdays}\n" \
               f"   workhours: {self.workhours}\n" \
               f"   income: {self.income}\n"

    def greet(self):
        print("Hello, my name is ", self.name, " I'm ", self.age, "years old.")
        print(f"I am {self.employment.profession.value[0]} .My working responsibilities are: {self.employment.profession.value[1]}")

    def walk(self):
        if self.workhours >= 12:
            print("I'm walking more than 10000 steps a day")
        else:
            print("My walking norm is 10000 steps a day")

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
work2 = Work()

study1 = Study()
student1 = Student('Sergo', 31, study1)
student1.greet()
student1.breathe()
student1.walk()

person1 = Worker("Sergei", 20, work1, 24, 5, 10)
person1.greet()
person1.walk()
person1.breathe()
