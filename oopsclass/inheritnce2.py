#defining class variable
class Employee:
    hike = 1.04     #class variable
    count=0         #count of objects


    def __init__(self, first, last, pay):   #constuctor of class
        self.f = first
        self.l = last
        self.p = pay
        Employee.count += 1

    def fullname(self):
        return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

    #def salaryhike(self):
       # self.p = int(self.p * 1.04)
    @classmethod            #replacing function with class method
    def salaryhike(cls, amount):
        cls.hike = amount

class Developer(Employee):      #subclass
    def __init__(self, first, last, pay, program):
        super().__init__(first, last, pay)      #functions of super for sub
        self.pl = program

emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)

print(emp1.fullname())
print(emp1.mail())
print(emp1.p)
#emp1.salaryhike()
print(emp1.p)
print(Employee.hike)
print(emp1.hike)
print(emp2.hike)
#print(emp1.__dict__)
#print(Employee.__dict__)

#Employee.hike=1.05     #changing hike by using class
#emp1.hike=1.05
#print(emp1.__dict__)       #checking if hike is changed in class and object dict
#print(Employee.__dict__)

#defining object of subclass
dev1=Developer('Rima','Rafeek',20000,'c++')
print(dev1.fullname())
print(dev1.pl)
#print(help(Developer))     #find mro
print(Employee.count)#defining count in function
#Employee.salaryhike(1.06)
print(Employee.hike)
print(emp1.hike)

emp1.salaryhike(1.06)   #method salaryhike is called with a object of class causing hike to change
print(Employee.hike)
print(emp1.hike)
