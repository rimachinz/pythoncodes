class Employee:
    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay
        #self.m = mail (instead of repaeatedly entering mails)

    def fullname(self):
       return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

emp1 = Employee('anu','s',100)
emp2 = Employee('dev', 'p', 200)

print(emp1.f)
print(emp1.l)
print(emp1.mail())
print(emp1.p)
print(emp1.fullname())
print(emp2.f)
print(emp2.l)
print(emp2.mail())
print(emp2.p)
print(emp2.fullname())
