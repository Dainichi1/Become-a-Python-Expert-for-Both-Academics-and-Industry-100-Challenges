n = int(input("Enter a number: "))

sum = 0

while n > 0:
    r = n % 10
    n = n // 10
    sum += r

print('The sum of digits is: ',sum)