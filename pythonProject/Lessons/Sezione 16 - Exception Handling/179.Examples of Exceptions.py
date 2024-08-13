# Index Error Example
L = [10, 20, 30, 40, 50]  # List of elements

# Asking user to enter an index
index = int(input('Enter an index: '))

# Attempt to access the list at the given index
try:
    print(L[index])
except IndexError:
    print("Index Error: List index out of range")

# Value Error and Type Error Examples

# Value Error Example
try:
    val = int('abc')  # This will cause a ValueError
except ValueError:
    print("Value Error: Invalid literal for int()")

# Type Error Example 1
try:
    res = '2' + 3  # This will cause a TypeError
except TypeError:
    print("Type Error: Can't concatenate str and int")

# Type Error Example 2
a = 10
s = 'number'
try:
    print(s + a)  # This will cause a TypeError
except TypeError:
    print("Type Error: Can't concatenate str and int")

# Key Error Example
D = {1: 'a', 2: 'b', 3: 'c'}  # Dictionary example

# Asking user to enter a key
key = int(input('Enter a key: '))

# Attempt to access the dictionary with the given key
try:
    print(D[key])
except KeyError:
    print("Key Error: The key does not exist in the dictionary")

# Zero Division Error Example

# Asking user to enter two numbers
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Attempt to divide the first number by the second
try:
    res = a / b
    print(res)
except ZeroDivisionError:
    print("Zero Division Error: Division by zero is not allowed")
