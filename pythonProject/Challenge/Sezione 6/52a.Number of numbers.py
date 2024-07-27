num_of_numbers = int(input("Enter the number of numbers : "))

sum = 0
count = 0

while count < num_of_numbers:
    numbers = int(input("Enter the numbers : "))
    sum = sum + numbers
    count = count + 1
print(sum)