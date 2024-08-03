# Creazione di un set
s = {1, 2, 3, 4}

# Metodo add() - aggiungere un elemento a un set
s.add(5)
print(s)  # Output: {1, 2, 3, 4, 5}

# Metodo copy() - clonare un set
s_copy = s.copy()
print(s_copy)  # Output: {1, 2, 3, 4, 5}

# Metodo update() - aggiungere più elementi a un set
s.update({6, 7})
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Metodo pop() - rimuovere un elemento casuale da un set
removed_element = s.pop()
print(removed_element)  # Output: un elemento rimosso casuale
print(s)  # Il set senza l'elemento rimosso

# Metodo discard() - rimuovere un elemento specifico senza errore se non esiste
s1 = {10, 20, 30, 40, 50, 60}
s1.discard(70)
print(s1)  # Output: {10, 20, 30, 40, 50, 60} (nessun errore se 70 non è presente)

# Metodo remove() - rimuovere un elemento specifico (genera un errore se non esiste)
try:
    s1.remove(70)
except KeyError as e:
    print(e)  # Output: KeyError: 70

# Metodo clear() - rimuove tutti gli elementi dal set, rendendolo vuoto
s1.clear()
print(s1)  # Output: set()
