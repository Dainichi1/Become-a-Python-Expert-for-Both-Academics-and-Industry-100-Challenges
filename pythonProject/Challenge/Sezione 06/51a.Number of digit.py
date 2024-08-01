n = int(input("Enter a number: "))

counter  = 0

while n > 0:
    n = n // 10
    counter = counter + 1

print ('The number has ', counter, ' digits.')


