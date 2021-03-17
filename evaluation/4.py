class Student:

    def __init__(self, first, last, mark1, mark2, mark3):
        self.first = first
        self.last = last
        self.sub1 = mark1
        self.sub2 = mark2
        self.sub3 = mark3
        self.name = first + ' ' + last

    def total(self):

        total = self.sub1+self.sub2+self.sub3
        return total

    def revaluation(self):
        self.sub1 = mark1
        self.sub2 = mark2
        self.sub3 = mark3



stu1 = Student('Renu', 'L',50,20,40)
print(stu1.total())
print(stu1.name)






