class Student:
    hike=1.5
    count=0
    def __init__(self,first,last,fees):
        self.f = first
        self.l = last
        #self.m = mail
        self.fe = fees
        self.fn = self.f + " " + self.l
        Student.count += 1

    def fullname(self):
        return '{} {}'.format(self.f, self.l)

    def mail(self):
        return '{}{}@gmail.com'.format(self.f, self.l)

    def feehike(self):
         self.fe = int(self.fe * 1.5)


class Teacher(Student):
    def __init__(self, first, last, fees, salary):
        super().__init__(first, last,fees)
        self.s = salary


stu1 = Student("asha", "ash", 10000)
stu2 = Student("isha", "sha", 20000)


tea1 = Teacher('Jibin', 'S', 15000, 25000)


print(tea1.__dict__)
#print(tea1.s)
#print(stu1)
#print(stu1.mail())
#print(stu2)
#print(stu1.fullname())
#print(stu1.__dict__)
#print(stu2.__dict__)
#print(stu1.fn)
#stu1.feehike()
#print(stu1.fe)
#stu2.feehike()
#print(stu2.fe)
#print(stu1.hike)
#print(Student.count)