#static method
import datetime
class Employee:
    def __init__(self, first, last, pay):
        self.f = first
        self.l = last
        self.p = pay

    def fullname(self):
        return "{} {}".format(self.f, self.l)

    def mail(self):
        return "{}{}@gmail.com".format(self.f, self.l)

    def salaryhike(self):
        self.p = int(self.p * 1.04)

    @staticmethod
    def _is_workingday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


my_date = datetime.date(2017, 7, 10)
a = Employee._is_workingday(my_date)
if a == True:
    print('workingday')
else:
    print('holiday')



