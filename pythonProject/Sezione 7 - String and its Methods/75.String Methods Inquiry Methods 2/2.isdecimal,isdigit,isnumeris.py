'''
It will say of there are decimal present in the string
s = ‘ 125 ‘ ——> True
s = ‘ 1.25 ‘ ——>False
What are decimal ?? Decimal are the numbers between 0 - 9
'''
s = '125'
b = '1.25'

print(s.isdigit())
print(b.isdigit())

'''
= ‘ 1682 ‘ ——> True
• If you have special numbers it will return true
• But in s.isdecimal ( ) it will return False
'''
s = '125\u00b2'
b = '1.25'
print(s.isdigit())
print(s.isnumeric())
print(s.isdecimal())



'''
s.isnumeric( )
s = ‘ 5 1/2 ‘ ——> True
• But in decimal and digit it will be false
• It will return true to any number
'''
s = '125\u00bd'
print(s.isdigit())
print(s.isnumeric())
print(s.isdecimal())