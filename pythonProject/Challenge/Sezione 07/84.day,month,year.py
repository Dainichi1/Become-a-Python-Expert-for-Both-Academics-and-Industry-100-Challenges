date = input('Enter a date in dd/mm/yyyy: ')

slashposition = date.find('/')

print(slashposition)

print('day: ',date[:slashposition:])

second = date[slashposition+1::]



slashposition2 = second.find('/')



print('month: ',second[:slashposition2:])
print('year: ',second[slashposition2+1::])