def objectcheck(func):
    def inner(obj):
        if type(obj) != object:
            return print("given value is not an object!")
        try:
            func(obj)
        except:
            return print("an error occurred")

    return inner


@objectcheck
def generateobjectfile(obj):
    with open(f"{obj.__class__.__name__}__{obj.name}.txt", "w+") as f:
        strings = str(obj)
        f.write(strings)


class Person:
    name = str
    age = int
    emoloymentstatus = bool
    responsabilities = list()
    wage = float
    workdays = int
    workhours = int
    monthincome = float

    def __init__(self, name, age, employmentstatus=False, responsabilities=None, wage=0, workdays=0, workhours=0):
        self.name = name
        self.age = age
        self.employmentstatus = employmentstatus
        self.responsabilities = responsabilities
        self.wage = wage
        self.workdays = workdays
        self.workhours = workhours
        self.income = f"My monthly income is: {self.monthlyincome()}. My year income is: {self.yearlyincome()}"

    # for computer representation
    def __repr__(self):
        return f"{self.name} is The object of class {self.__class__.__name__} stored ad {hex(id(self))}"

    # for humans
    def __str__(self):
        return f"class {self.__class__.__name__}:\n" \
               f"   name: {self.name}\n" \
               f"   age: {self.age}\n" \
               f"   employmentstatus: {self.employmentstatus}\n" \
               f"   responsabilities: {self.responsabilities}\n" \
               f"   wage: {self.wage}\n" \
               f"   workdays: {self.workdays}\n" \
               f"   workhours: {self.workhours}\n" \
               f"   income: {self.income}\n" \


    def greet(self):
        print("Hello, my name is ", self.name, " I'm ", self.age, "years old.")
        if self.employmentstatus is True:
            respstring = self.responsabilities
            respstring = ", ".join(respstring)
            print("My working responsabilities are: ", respstring)
        else:
            print("I'm currently unemployed.")

    def monthlyincome(self):
        monthincome = ((self.wage * self.workhours) * self.workdays) * 3
        return monthincome

    def yearlyincome(self):
        yearincome = self.monthlyincome() * 12
        return yearincome


person1 = Person("Sergei", "20", True,
                 list(['mail loading/unloading', 'mail receiving/delivery', 'workplace cleaning']),
                 45, 5, 4)
person1.greet()
print(person1.income)

person2 = Person("David", "19", False)
person2.greet()
print(person2.responsabilities, person2.wage, person2.workdays, person2.workhours)
