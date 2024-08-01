'''
Variable can not Start with a number so it will return false
• This method will check if it gives the valid name of the variable
• For keywords also it will return true
s = ‘ if ‘ ——> True
'''
a = 'length1'
b = '1lenght'
print(a.isidentifier())
print(b.isidentifier())

'''
All the ASCII letters , other language letters are printable but there 
are escape characters \n \t \r
are not printable so it will return false
s = ‘ hello ‘ ——> True
s = ‘ hello \n how are you ‘ ——> False
'''
a = 'hello world'
b = 'hello \n world'
print(a.isprintable())
print(b.isprintable())



