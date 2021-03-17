#class method
class Employee:
    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay
    @classmethod#take class name as default
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_str1 = "abhijith-s-20000"
emp_str2 = "rima-rafeek-20000"

emp1 = Employee.from_string(emp_str1)
emp2 = Employee.from_string(emp_str2)

print(emp1.f)
print(emp2.p)
