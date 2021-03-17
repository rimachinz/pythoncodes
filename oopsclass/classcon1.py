#no class definition
class Employee:
    pass


emp1 = Employee()#object created ,constructor invoked
emp2 = Employee()
print(emp1)#returns location of object
print(emp2)
emp1.first = 'anu'
emp1.last = 's'
emp1.email = 'anus@yahoo.com'
emp1.pay = 10000
print(emp1.first)#check if assigned value entered
print(emp1.last)
print(emp1.email)
print(emp1.pay)
emp2.first='dev'
emp2.last='b'
emp2.email='devb@yahoo.com'
emp2.pay=20000
print(emp2.first)
print(emp2.last)
print(emp2.email)
print(emp2.pay)
#pblm:LOC is more