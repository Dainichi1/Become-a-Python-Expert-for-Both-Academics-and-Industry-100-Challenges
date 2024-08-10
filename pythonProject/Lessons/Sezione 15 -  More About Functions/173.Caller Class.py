class Dept:
    def __init__(self):
        self.depts = {'hr': 'Human Resources Department',
                      'acc' : 'Accounts and Finance Department',
                      'sd' : 'Sales and Marketing',
                      'mft' : 'Manufacturing'}

    def __call__(self, dept):
        return self.depts[dept]

d = Dept()
s = d('hr')
print(s)


#################################################

def Dept2():
    depts2 = {'hr': 'Human Resources Department',
                      'acc' : 'Accounts and Finance Department',
                      'sd' : 'Sales and Marketing',
                      'mft' : 'Manufacturing'}

    def dname(dept):
        return depts2[dept]

    return dname

d = Dept2()
s = d('hr')
print(s)
