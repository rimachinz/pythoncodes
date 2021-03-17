class Employee:
    def __repr__(self):
        return '{} {}'.format(self.fullname(), self.mail())

    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay

    def __add__(self, other):
        return self.p + other.p

    def fullname(self):
        return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

    def salaryhike(self):
        self.p = int(self.p * 1.04)


emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)
print(emp1)
print(emp1+emp2)