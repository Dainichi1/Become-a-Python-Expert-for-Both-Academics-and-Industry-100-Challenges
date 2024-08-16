file = open('ModeTypes.txt','w')
file.write('Hello\n')
file.write('How are you\n')
file.write('Do you know Python\n')

file.close()


file = open('ModeTypes.txt','a')
file.write('I am learning Python\n')
file.write('It is a very easy language\n')
file.write('I am practicing every day\n')

file.close()

file = open('ModeTypes.txt','r+')
str1 = file.read(10)
print(str1)
file.write('Goodbye')
file.close()


