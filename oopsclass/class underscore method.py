class Employee:
    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay

    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return "{} {}".format(self.f, self.l)


emp1 = Employee('anu', 's', 10000)
emp2 = Employee('dev', 'p', 20000)
print(len(emp1))