initialTerm = int(input('Enter the initial term: '))
diff = int(input('Enter the common difference: '))
num = int(input('Enter how many numbers you want to display: '))

for l in range (initialTerm,(num*diff)+initialTerm,diff):
    print(l)