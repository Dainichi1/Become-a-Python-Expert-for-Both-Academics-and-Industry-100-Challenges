

birthdays = {
    'Sachin' : '03/14/2003',
    'Carl' : '01/17/2001',
    'Khan' : '12/10/2006',
    'Donald' : '06/14/2010',
    'Rohan' : '01/06/2005'
}

name = input('Enter a name: ')

for i in birthdays:
    if i == name:
        print(birthdays[i])

if name not in birthdays:
    print('Not found')

