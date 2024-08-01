# Creazione di una tuple
t1 = ('jack', 45, 38.6, False, 5-6j, 'Jill', 45)

# Iterazione su una tuple usando un ciclo for
for x in t1:
    print(x)

# Iterazione su una tuple usando un ciclo for e range
for i in range(len(t1)):
    print(t1[i])

# Operatori nelle tuple
# Indexing
print(t1[1])  # Output: 45

# Slicing
print(t1[1:3])  # Output: (45, 38.6)

# Concatenazione
t2 = (1, 2, 3)
t3 = (4, 5, 6)
t4 = t2 + t3
print(t4)  # Output: (1, 2, 3, 4, 5, 6)

# Ripetizione
t5 = t2 * 2
print(t5)  # Output: (1, 2, 3, 1, 2, 3)

# Appartenenza (Membership)
print(5 in t3)  # Output: True
print(7 not in t3)  # Output: True

# Notare che le tuple sono immutabili
try:
    t1[1] = 100  # Questo genererà un errore
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
