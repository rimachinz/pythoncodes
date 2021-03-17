#methods to define attribute(fullname)
class Employee:
    def __init__(self, first, last, mail, pay):
        self.f = first
        self.l = last
        self.m = mail
        self.p = pay
        self.fn = first + ' ' + last

    def fullname(self):
        return "{} {}".format(self.f, self.l)
# multiple attibutes for RETURN can be passed only if method is tuple ,list or object
# not for attributes like fullname


emp1 = Employee('anu', 's', 'anus@gmail.com', 100)
emp2 = Employee('dev', 'p', 'devp@yahoomail', 200)

print(emp1.fullname())
print(emp1.f)
print(emp1.l)
print(emp1.m)
print(emp1.p)
print(emp1.fn)

print(emp2.f)
print(emp2.l)
print(emp2.m)
print(emp2.p)
print(emp2.fullname())
print(emp2.fn)

print(emp1.f, ' ', emp1.l)