# Metodo index(x[, start[, end]])
# Restituisce l'indice del primo elemento uguale a x nella lista
# Se start e end sono specificati, cerca solo in quella porzione della lista

L1 = [5, 6, 7, 1, 2, 3, 6, 7, 9, 6]
print(L1.index(1))  # Output: 3
print(L1.index(7))  # Output: 2
print(L1.index(5))  # Output: 0
print(L1.index(6, 2))  # Output: 6
print(L1.index(6, 2, 7))  # Output: 6

# Metodo count(x)
# Restituisce il numero di volte che x appare nella lista

L1 = [5, 6, 7, 1, 2, 3, 6, 7, 9, 6]
print(L1.count(6))  # Output: 3
print(L1.count(5))  # Output: 1
print(L1.count(7))  # Output: 2

# Metodo reverse()
# Inverte gli elementi della lista

L1 = [5, 6, 7, 1, 2, 3, 6, 7, 9, 6]
L1.reverse()
print(L1)  # Output: [6, 9, 7, 6, 3, 2, 1, 7, 6, 5]

# Metodo sort(*, key=None, reverse=False)
# Ordina gli elementi della lista in ordine crescente

L1 = ['yy', 'JJ', 'mm', 'BB', 'aa', 'zz']
L1.sort()
print(L1)  # Output: ['BB', 'JJ', 'aa', 'mm', 'yy', 'zz']

L1.sort(key=str.lower)
print(L1)  # Output: ['aa', 'BB', 'JJ', 'mm', 'yy', 'zz']

# La funzione globale sorted() ordina una lista e restituisce una nuova lista ordinata

L1 = ['yy', 'JJ', 'mm', 'BB', 'aa', 'zz']
print(sorted(L1))  # Output: ['BB', 'JJ', 'aa', 'mm', 'yy', 'zz']
print(L1)  # Output: ['yy', 'JJ', 'mm', 'BB', 'aa', 'zz'] (lista originale non modificata)
