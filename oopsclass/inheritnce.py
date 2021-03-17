#defining class variable
class Employee:
    hike = 1.04
    count=0


    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay
        Employee.count += 1

    def fullname(self):
        return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

    def salaryhike(self):
        self.p = int(self.p * 1.04)


class Developer(Employee):
    def __init__(self, first, last, pay, program):
        Employee.__init__(self, first, last, pay)
        self.pl=program


emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)

print(emp1.fullname())
print(emp1.mail())
print(emp1.p)
emp1.salaryhike()
print(emp1.p)
print(Employee.hike)
print(emp1.hike)
print(emp2.hike)
print(emp1.__dict__)
print(Employee.__dict__)

Employee.hike = 1.05
emp1.hike = 1.05
print(emp1.__dict__)
print(Employee.__dict__)

print(Employee.count)#defining count in function



dev1=Developer('Rima','Rafeek',20000,'c++')
#print(help(Developer))
print(dev1.fullname())
print(dev1.pl)