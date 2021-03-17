class Employees:

    def __init__(self, firstname, lastname, pay,mail):
        self.f = firstname
        self.l = lastname
        self.p = pay
        self.m = mail
        self.dict = {'self.f': firstname, 'self.l': lastname, 'self.m': mail, 'self.p': pay}

    @property
    def fullname(self):
        return '{}{}'.format(self.f, self.l)

    @property
    def mail(self):
        return '{}{}@gmail.com'.format(self.f, self.l)
