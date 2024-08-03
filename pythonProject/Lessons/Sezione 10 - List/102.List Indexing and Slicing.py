# Esempio di indicizzazione e slicing delle liste

# Creazione della lista
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Indicizzazione positiva
print(list1[6])  # Output: 7
print(list1[1:4])  # Output: [2, 3, 4]

# Assegnazione a una variabile tramite indicizzazione
x = list1[6]
print(x)  # Output: 7

# Modifica di un elemento tramite indicizzazione
list1[6] = 15
print(list1)  # Output: [1, 2, 3, 4, 5, 6, 15, 8, 9, 10]

# Slicing delle liste
print(list1[:])  # Output: [1, 2, 3, 4, 5, 6, 15, 8, 9, 10]
print(list1[1:8:2])  # Output: [2, 4, 6, 8]
print(list1[::3])  # Output: [1, 4, 15, 10]
print(list1[::-1])  # Output: [10, 9, 8, 15, 6, 5, 4, 3, 2, 1]
print(list1[1:7:1])  # Output: [2, 3, 4, 5, 6, 15]
print(list1[1:7:-1])  # Output: []

# Utilizzo dello slicing con step negativo
print(list1[7:1:-1])  # Output: [8, 15, 6, 5, 4, 3]
print(list1[10:1:-2])  # Output: [10, 8, 6, 4]

# Modifica di sezioni della lista tramite slicing
list1[0:3] = [10, 20, 30]
print(list1)  # Output: [10, 20, 30, 4, 5, 6, 15, 8, 9, 10]

list1[0:3] = [11, 12]
print(list1)  # Output: [11, 12, 4, 5, 6, 7, 8, 9, 10]

list1[0:2] = [10, 20, 30, 40, 50]
print(list1)  # Output: [10, 20, 30, 40, 50, 4, 5, 6, 7, 8, 9, 10]

# Assegnazione tramite slicing con step
try:
    list1[::2] = [11, 22, 33, 44]
except ValueError as e:
    print(e)  # Output: attempt to assign sequence of size 4 to extended slice of size 6

list1[::2] = [11, 22, 33, 44, 55, 66]
print(list1)  # Output: [11, 20, 22, 40, 33, 4, 44, 6, 55, 8, 66, 10]
