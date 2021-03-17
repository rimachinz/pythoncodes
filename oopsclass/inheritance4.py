#hierarchical
class Employee:
    hike = 1.04     #defining class variable
    count = 0       #taking count of objects

    def __init__(self, first, last, pay):   #constructor of class
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


class Developer(Employee):      #single inheritance=developer from employee
    def __init__(self, first, last, pay, program):
        super().__init__(first, last, pay)      #functions inherited from superclass
        self.pl = program       #function of subclass


class Manager(Employee):        #hierarchical inheritance
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
    def add_emps(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emps(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emps(self):
        for emp in self.employee:
            print(emp.fullname())
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
#print(emp1.__dict__)
#print(Employee.__dict__)

Employee.hike=1.05 #class variable
emp1.hike=1.05
#print(emp1.__dict__)
#print(Employee.__dict__)
print(Employee.count)#defining count in function

#single inheritance
dev1=Developer('Rima','Rafeek',20000,'c++')
print(dev1.fullname())
print(dev1.pl)
#hierarchical inheritance
mrg1=Manager('Ram','G',5000,None)
mrg2=Manager('Ramaz','S',6000,[dev1])

print(mrg1.employee)
print(mrg1.__dict__)
print(mrg2.employee)
print(mrg2.__dict__)
mrg2.print_emps()
