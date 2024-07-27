num_of_numbers = int(input("Enter the number of numbers : "))

sumP = 0
sumN = 0
count = 0

while count < num_of_numbers:
    numbers = int(input("Enter the numbers : "))
    if numbers >=0:
        sumP = sumP + numbers
    else:
        sumN = sumN + numbers
    count = count + 1
print('Sum of positive numbers: ',sumP)
print('Sum of negative numbers: ',sumN)