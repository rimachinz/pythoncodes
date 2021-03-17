# defining class variable
class Employee:
    hike = 1.04#class variable(ease to change value in the code when change in hike occurs
    count = 0

    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay
        Employee.count += 1
#no of employees (object created)will be equal to no of times init is called

    def fullname(self):
        return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

    #def salaryhike(self):
        #self.p = int(self.p * 1.04)

    def salaryhike(self):
        self.p = int(self.p * Employee.hike)

    @classmethod#change cls attribute by accessing object(change hike when needed)
    def set_salaryhike(cls, amount):
        cls.hike = amount


emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)

print(emp1.p)#initial pay displays passed value of pay
emp1.salaryhike()
print(emp1.p)#incremented  pay
print(Employee.hike)
print(emp1.hike)
print(emp2.hike)
print(emp1.__dict__)
print(Employee.__dict__)
# changing class variable, directly object variable gets changed
Employee.hike = 1.05
print(emp1.hike)#hike=1.04 changes to 1.05
emp1.salaryhike()#method called with changed value
print(emp1.p)#pay with new hike

#dict with changed hike displayed
print(emp1.__dict__)
print(Employee.__dict__)
#changing class variable using class method
Employee.set_salaryhike(1.06)
print(emp2.hike)
print(Employee.hike)
#using classmethod change of value of objects attribute can change class
emp1.set_salaryhike(1.07)
print(Employee.hike)

# defining count in function
print(Employee.count)

