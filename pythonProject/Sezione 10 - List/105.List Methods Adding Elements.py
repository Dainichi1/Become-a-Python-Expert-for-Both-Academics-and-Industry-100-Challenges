# Metodo append(x)
# Aggiunge un elemento alla lista

L1 = [5, 6, 7, 8, 9]
print(len(L1))  # Output: 5

L1.append(10)
print(len(L1))  # Output: 6

print(L1)  # Output: [5, 6, 7, 8, 9, 10]

# Usare append con slicing
# L1.append(11, 12, 13) # Questo genera un errore
# L1[len(L1):] = [10] # Aggiunge 10 alla fine della lista
# print(L1)  # Output: [5, 6, 7, 8, 9, 10, 10]
# L1[6:6] = [11] # Inserisce 11 alla posizione 6
# print(L1)  # Output: [5, 6, 7, 8, 9, 10, 11]

# Metodo extend(iterable)
# Estende la lista con un iterabile

L1 = [5, 6, 7, 8, 9]
L1.extend([10, 11, 12])
print(L1)  # Output: [5, 6, 7, 8, 9, 10, 11, 12]

L1.extend('abc')
print(L1)  # Output: [5, 6, 7, 8, 9, 10, 11, 12, 'a', 'b', 'c']

# Metodo insert(i, x)
# Inserisce un elemento alla posizione specificata

L1 = [5, 6, 7, 8, 9]
L1.insert(0, 10)
print(L1)  # Output: [10, 5, 6, 7, 8, 9]

L1.insert(3, 20)
print(L1)  # Output: [10, 5, 6, 20, 7, 8, 9]

L1[1:4] = [22]
print(L1)  # Output: [10, 22, 7, 8, 9]

L1[0:0] = [25]
print(L1)  # Output: [25, 10, 22, 7, 8, 9]

# Metodo copy()
# Crea una copia superficiale della lista

L1 = [5, 6, 7, 8, 9]
L2 = L1.copy()
print(L2)  # Output: [5, 6, 7, 8, 9]

print(id(L1))  # Output: id di L1
print(id(L2))  # Output: id di L2, diverso da id di L1

print(L1[0])  # Output: 5
print(L2[0])  # Output: 5

print(id(L1[0]))  # Output: id di L1[0]
print(id(L2[0]))  # Output: id di L2[0], uguale a id di L1[0]
