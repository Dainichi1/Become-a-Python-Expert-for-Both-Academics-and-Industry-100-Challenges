# Creazione di un set
s1 = {1, 2, 3, 4, 'jack', 3.4, 'jack'}
print(s1)  # Output: {1, 2, 3.4, 4, 'jack'}

# Tentativo di accedere ad un elemento del set usando l'indice (genera un errore)
try:
    print(s1[0])
except TypeError as e:
    print(e)  # Output: 'set' object is not subscriptable

# Verifica del tipo di dato
print(type(s1))  # Output: <class 'set'>

# Creazione di un set usando la funzione set()
try:
    s2 = set(1, 2, 3, 4, 5)
except TypeError as e:
    print(e)  # Output: set expected at most 1 argument, got 5

# Operazioni sui set: discard, add
s4 = {20, 40, 10, 30}

# Rimuovere un elemento (se esiste) con discard
s4.discard(50)
print(s4)  # Output: {20, 40, 10, 30}

# Aggiungere un nuovo elemento con add
s4.add(100)
print(s4)  # Output: {20, 100, 40, 10, 30}

# Aggiungere un altro nuovo elemento
s4.add(120)
print(s4)  # Output: {20, 100, 40, 10, 120, 30}
