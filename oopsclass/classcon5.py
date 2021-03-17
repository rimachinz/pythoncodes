# defining functions for some objects
class Employee:
    def __init__(self, first, last, pay):
        self.f = first#instance (self.f) attributes since accesed with object
        self.l = last
        self.p = pay

    def fullname(self):
        return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

    def salaryhike(self):
        self.p = int(self.p * 1.04)


emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)
print(emp1.fullname())
print(emp1.mail())
print(emp1.p)
emp1.salaryhike()
print(emp1.p)#salary hike for employee1