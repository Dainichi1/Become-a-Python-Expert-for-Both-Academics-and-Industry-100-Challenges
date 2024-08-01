'''
If the string contain alphabets and numbers it will return true .
If it contain special alphabets
than it will return false
'''
a = 'abc123'

r = a.isalnum()

print (r)

'''
If it is only alphabets then it will return true
'''
b = 'abc123'

s = b.isalpha()

print (s)

'''
It will check if there are any spaces present in the string then it 
will return true
'''
c = '    '

t = c.isspace()

print (t)

'''
If it contain all the ASCII character , can have lower case , 
upper case , special character etc
then it will return True
'''
b = 'abc12#!'

s = b.isascii()

print (s)
