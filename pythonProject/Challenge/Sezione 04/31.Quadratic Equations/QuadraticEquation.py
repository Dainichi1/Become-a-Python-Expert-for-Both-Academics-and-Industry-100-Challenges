import math

valueA = float (input('Enter the value of a: '))
valueB = float (input('Enter the value of b: '))
while valueB <=  0 :
    print ('value of b must be positive')
    valueB = float (input('Enter the value of b: '))
valueC = float (input('Enter the value of c: '))

r1 = (-valueB + math.sqrt((valueB*valueB)-(4*valueA*valueC)))/(2*valueA)
r2 = (-valueB - math.sqrt((valueB*valueB)-(4*valueA*valueC)))/(2*valueA)

print('The results are: ',r1,' and',r2)