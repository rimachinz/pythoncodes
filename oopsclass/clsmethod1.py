#scenario of class method
class Employee:

    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay


emp_str = "abhijith-s-20000"
emp_str2 = "rima-rafeek-20000"

first, last, pay = emp_str.split('-')
emp1 = Employee(first, last, pay)

first, last, pay = emp_str2.split('-')
emp2 = Employee(first, last, pay)


print(emp1.f)
print(emp2.f)