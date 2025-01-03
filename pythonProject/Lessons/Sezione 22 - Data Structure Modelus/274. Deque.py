from collections import deque

# Creazione di un deque a partire da una lista
L = [1, 2, 3, 4, 5]
q = deque(L)
print(q)  # Output: deque([1, 2, 3, 4, 5])

# append(): Aggiunge un elemento alla fine del deque
q.append(6)
print(q)  # Output: deque([1, 2, 3, 4, 5, 6])

# appendleft(): Aggiunge un elemento all'inizio del deque
q.appendleft(7)
print(q)  # Output: deque([7, 1, 2, 3, 4, 5, 6])

# pop(): Rimuove e restituisce l'ultimo elemento
print(q.pop())  # Output: 6
print(q)        # Output: deque([7, 1, 2, 3, 4, 5])

# popleft(): Rimuove e restituisce il primo elemento
print(q.popleft())  # Output: 7
print(q)            # Output: deque([1, 2, 3, 4, 5])

# extend(): Aggiunge più elementi alla fine del deque
q.extend([10, 20, 30])
print(q)  # Output: deque([1, 2, 3, 4, 5, 10, 20, 30])

# extendleft(): Aggiunge più elementi all'inizio del deque (in ordine inverso)
q.extendleft([11, 22, 33])
print(q)  # Output: deque([33, 22, 11, 1, 2, 3, 4, 5, 10, 20, 30])

# rotate(): Ruota gli elementi del deque
q.rotate(2)  # Ruota di 2 posizioni a destra
print(q)  # Output: deque([20, 30, 33, 22, 11, 1, 2, 3, 4, 5, 10])

q.rotate(-3)  # Ruota di 3 posizioni a sinistra
print(q)  # Output: deque([22, 11, 1, 2, 3, 4, 5, 10, 20, 30, 33])

# count(): Conta le occorrenze di un elemento nel deque
print(q.count(11))  # Output: 1

# index(): Trova la posizione della prima occorrenza di un elemento
print(q.index(3))  # Output: 4

# insert(): Inserisce un elemento in una posizione specifica
q.insert(2, 99)  # Inserisce 99 alla posizione 2
print(q)  # Output: deque([22, 11, 99, 1, 2, 3, 4, 5, 10, 20, 30, 33])

# remove(): Rimuove la prima occorrenza di un elemento
q.remove(99)  # Rimuove il primo 99
print(q)  # Output: deque([22, 11, 1, 2, 3, 4, 5, 10, 20, 30, 33])

# reverse(): Inverte l'ordine degli elementi nel deque
q.reverse()
print(q)  # Output: deque([33, 30, 20, 10, 5, 4, 3, 2, 1, 11, 22])

# pop(): Rimuove l'ultimo elemento
print(q.pop())  # Output: 22
print(q)        # Output: deque([33, 30, 20, 10, 5, 4, 3, 2, 1, 11])

# popleft(): Rimuove il primo elemento
print(q.popleft())  # Output: 33
print(q)            # Output: deque([30, 20, 10, 5, 4, 3, 2, 1, 11])
