try:
    print('Before try')
    a = int(input('Enter numerator: '))
    b = int(input('Enter denominator: '))
    c = a // b
except ZeroDivisionError as err:
    print('Error:', err)
else:
    print('Division is', c)
finally:
    print('Finally block executed')

print('Outside try-except-else-finally')
