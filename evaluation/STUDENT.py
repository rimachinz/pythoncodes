class Student:

    def __init__(self,first,mark1,mark2,mark3):
        self.first=first
        # self.last=last
        self.sub1 = mark1
        self.sub2 = mark2
        self.sub3 = mark3
        # self.name = first + ' ' + last
        # self.total = mark1 + mark2 + mark3
        # total = mark1 + mark2 + mark3
        # self.percentage = ((mark1+mark2+mark3) / 3) * 100

    @property
    def total(self):
        total = self.sub1+self.sub2+self.sub3
        return total

    @property
    def percentage(self):
        percentage = ((self.sub1+self.sub2+self.sub3)/300)*100
        return percentage

stu1=Student('Renu',50,60,70)

print(stu1.first)
print(stu1.sub3)
print(stu1.total)
print(stu1.percentage)


