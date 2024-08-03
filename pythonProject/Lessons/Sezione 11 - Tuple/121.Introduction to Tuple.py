# Creazione di una tuple
t1 = ('jack', 45, 38.6, False, 5-6j, 'Jill', 45)

# Controllare il tipo di t1
type(t1)

# Creazione di tuple
t1 = (1, 2, 3, 4, 5)
t1 = (10,)  # Singolo valore in una tuple
t1 = tuple([1, 2, 3, 4, 5])

# Esempi di operazioni su tuple (immutabilità)
t1[0]  # Accesso a elementi
t1 = t1 + (6,)  # Creazione di una nuova tuple con aggiunta di un elemento

# Esempio di packing
t1 = 10, 20, 30, 40
type(t1)

# Esempio di unpacking
t2 = (10, 20, 30, 40)
a, b, c, d = t2
print(a, b, c, d)

# Unpacking con liste
t1 = (10, 20, 30, 40)
l1 = [1, 2, 3]
type(l1)
a, b, c = l1
print(a, b, c)
