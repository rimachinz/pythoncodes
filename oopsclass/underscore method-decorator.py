class Employee:

    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay
    @property
    def fullname(self):
        return "{}{}".format(self.f, self.l)

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('anu', 's', 10000)
emp2 = Employee('devika', 'p', 20000)
print(len(emp2.fullname))