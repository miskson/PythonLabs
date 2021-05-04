# class Person:
#     name = "Bob"
#     age = 25
#     employed = True
#     responsabilities = ['Cooking', 'washing dishes', 'cleaning']
#
#     def greet(self):
#         print("Hello, my name is ", self.name, " I'm ", self.age, "years old.")
#         if self.employed is True:
#             respstring = self.responsabilities
#             respstring = ",".join(respstring)
#             print("My working responsabilities are: ", respstring)
#         else:
#             print("I'm currently unemployed.")

class Person():

    def __init__(self, name, age, employmentstatus, responsabilities, wage, workdays, workhours):
        self.name = name
        self.age = age
        self.employmentstatus = employmentstatus
        self.responsabilities = responsabilities
        self.wage = wage
        self.workdays = workdays
        self.workhours = workhours

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


person1 = Person("Sergei", "20", True,
                 list(['mail loading/unloading', 'mail receiving/delivery', 'workplace cleaning']),
                 45, 5, 4)
person1.greet()
print("mounthly income is:", person1.monthlyincome())
person2 = Person("David", "19", False, list(['studying']), 0, 0, 0)
person2.greet()
