num_of_numbers = int(input("Enter the number of numbers : "))

count = 0
max = 0
while count < num_of_numbers:
    numbers = int(input('Enter the numbers : '))
    if numbers > max:
        max = numbers

    count = count + 1
print ('The max number is: ',max)

