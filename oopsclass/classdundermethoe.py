class Employee:

    def __init__(self, first, last):
        self.f = first
        self.l = last
        self.mail = first+'.'+last+'@company.com'

    def fullname(self):
        return "{} {}".format(self.f, self.l)




emp1 =Employee('rima','rafeek')
# print(emp1.f)
# print(emp1.l)
# print(emp1.fullname())
# print(emp1.mail)
emp1.f = 'riya'
print(emp1.f)
print(emp1.l)
print(emp1.fullname())
print(emp1.mail)