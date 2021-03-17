class Employee:

    def __init__(self, firstname, lastname, pay):
        self.f = firstname
        self.l = lastname
        #self.m = mail
        self.p = pay
        self.dict = {'self.f': firstname, 'self.l': lastname, 'self.p': pay}

    @property
    def fullname(self):
        return '{} {}'.format(self.f, self.l)

    @property
    def mail(self):
        return '{}{}@gmail.com'.format(self.f, self.l)
