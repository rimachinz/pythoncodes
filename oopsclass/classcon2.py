#__INIT__ DEFINED
class Employee:
#any no of objects can be assigned values with reduced LOC
def __init__(self, first, last, mail, pay):
      self.f = first
      self.l = last
      self.m = mail
      self.p = pay


emp1=Employee('anu','s','ab@gmail.com',100)
emp2=Employee('dev','p','xy@gmail.com',200)
print(emp1.p)
print(emp1.f)
print(emp1.l)
print(emp1.m)

print(emp2.p)
print(emp2.f)
print(emp2.l)
print(emp2.m)




