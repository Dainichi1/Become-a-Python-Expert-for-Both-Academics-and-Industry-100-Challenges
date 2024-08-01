# List comprehension per creare una lista
l1 = [x for x in range(10)]
print(l1)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generator expression per creare un generatore
t1 = (x for x in range(10))
print(t1)  # Output: <generator object <genexpr> at 0x...>

# Tuple comprehension (usando una generator expression all'interno della funzione tuple)
t2 = tuple(x for x in range(10))
print(t2)  # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Creazione di una tuple con una comprehension con condizione
t3 = *(x for x in range(1, 10, 2)),
print(t3)  # Output: (1, 3, 5, 7, 9)

# Tuple comprehension su una stringa
t4 = *(x for x in 'python'),
print(t4)  # Output: ('p', 'y', 't', 'h', 'o', 'n')

# Creazione di un'altra tuple con condizione su una stringa
t5 = *(x for x in 'PyThOn' if x.islower()),
print(t5)  # Output: ('y', 'h', 'n')

# Creazione di una tuple con una comprehension moltiplicando gli elementi
t7 = tuple(x*2 for x in (1, 3, 5, 7, 9))
print(t7)  # Output: (2, 6, 10, 14, 18)

# Contare gli elementi di una tuple
t8 = (1, 2, 3, 4, 5, 4, 5, 6, 7)
count_4 = t8.count(4)
print(count_4)  # Output: 2

# Trovare l'indice di un elemento in una tuple
index_3 = t8.index(3)
print(index_3)  # Output: 2

# Tentativo di trovare l'indice di un elemento che non esiste
try:
    index_10 = t8.index(10)
except ValueError as e:
    print(e)  # Output: tuple.index(x): x not in tuple
