number = int(input('Enter a number: '))
result = 1
for secondNumber in range (1,number+1,1):

    result *= secondNumber

print('Factorial is: ',result)