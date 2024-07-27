

n = int(input("Enter the binary number: "))

bin = ''
while n > 0:
    r = n % 2
    n = n // 2
    bin = str(r) + bin



print("The binary number is", bin)