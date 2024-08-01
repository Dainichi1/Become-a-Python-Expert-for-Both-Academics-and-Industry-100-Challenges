# Esempi di operatori per le liste

# Operatore di concatenazione '+'
list1 = [1, 2, 3]
list2 = list1 + [4]
print(list2)  # Output: [1, 2, 3, 4]

# Utilizzo del metodo extend()
list1 = [1, 2, 3]
list1.extend([4, 5, 6])
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# Modifica della lista con '+='
list2 = [7, 8, 9]
list2 = list2 + [10, 11, 12]
print(list2)  # Output: [7, 8, 9, 10, 11, 12]

# Operatore di ripetizione '*'
list1 = [1, 2, 3]
list1 = list1 * 2
print(list1)  # Output: [1, 2, 3, 1, 2, 3]

# Errore con la moltiplicazione per un float
try:
    list1 = [1, 2, 3]
    list1 = list1 * 2.5
except TypeError as e:
    print(e)  # Output: can't multiply sequence by non-int of type 'float'

# Operatori 'in' e 'not in'
list1 = [1, 2, 3]
print(2 in list1)  # Output: True
print(10 in list1)  # Output: False
print(10 not in list1)  # Output: True
